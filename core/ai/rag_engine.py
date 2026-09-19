"""
Hybrid RAG Engine for Swarnav Tour & Travels.
Combines Dense Vector Embeddings (Gemini text-embedding-004) with Keyword/BM25 Matching
over Django models (TourPackage, ItineraryDay, TravelGuide, etc.) and Docx files.
"""
import os
import json
import math
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

from core.ai.ai_config import get_genai_client, EMBEDDING_MODEL, BASE_DIR

logger = logging.getLogger(__name__)

INDEX_DIR = BASE_DIR / "core" / "ai" / "data"
INDEX_FILE = INDEX_DIR / "knowledge_index.json"

_IN_MEMORY_INDEX: Optional[List[Dict[str, Any]]] = None


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """Compute cosine similarity between two numeric vectors."""
    if not v1 or not v2 or len(v1) != len(v2):
        return 0.0
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


def compute_keyword_score(query_tokens: List[str], chunk_text: str, chunk_title: str) -> float:
    """Compute normalized lexical keyword overlap score."""
    text_lower = (chunk_title + " " + chunk_text).lower()
    if not query_tokens:
        return 0.0
    matches = 0
    for token in query_tokens:
        if token in text_lower:
            matches += 2 if token in chunk_title.lower() else 1
    return min(1.0, matches / (len(query_tokens) + 1))


def extract_docx_chunks(docx_path: Path) -> List[Dict[str, Any]]:
    """Extract and section text from source Word documents."""
    chunks = []
    if not docx_path.exists():
        return chunks

    try:
        import docx
        doc = docx.Document(docx_path)
        current_heading = "Char Dham Master Overview"
        current_paragraphs = []

        for p in doc.paragraphs:
            text = p.text.strip()
            if not text:
                continue
            # Detect day or section headings
            if text.lower().startswith("day ") or text.lower().startswith("char dham") or text.isupper():
                if current_paragraphs:
                    chunks.append({
                        "id": f"docx_{len(chunks)+1}",
                        "tour_slug": "char-dham",
                        "category": "itinerary_source_doc",
                        "title": current_heading,
                        "content": "\n".join(current_paragraphs)
                    })
                    current_paragraphs = []
                current_heading = text
            else:
                current_paragraphs.append(text)

        if current_paragraphs:
            chunks.append({
                "id": f"docx_{len(chunks)+1}",
                "tour_slug": "char-dham",
                "category": "itinerary_source_doc",
                "title": current_heading,
                "content": "\n".join(current_paragraphs)
            })
    except Exception as exc:
        logger.warning("Error reading docx file %s: %s", docx_path, exc)

    return chunks


def build_knowledge_chunks() -> List[Dict[str, Any]]:
    """
    Extract structured, comprehensive knowledge chunks across all tours,
    itinerary days, travel guidelines, and policy models.
    """
    from yatras.models import (
        TourPackage, ItineraryDay, DhamDestination,
        PackageDetail, StayAndTravel, TravelGuide, PolicyAndFaq
    )

    chunks = []

    # 1. Extract Tour Packages Overview
    for tour in TourPackage.objects.all():
        highlights_str = "\n• " + "\n• ".join(tour.highlights) if tour.highlights else ""
        content = (
            f"Tour Name: {tour.name}\n"
            f"Subtitle: {tour.subtitle}\n"
            f"Region: {tour.region}\n"
            f"Duration: {tour.duration_display} ({tour.duration_days} Days / {tour.duration_nights} Nights)\n"
            f"Starting Price: {tour.starting_price} ({tour.price_note})\n"
            f"Origin & Return: {tour.origin} (Primary coordination from Surat, Gujarat with onward connectivity)\n"
            f"Status: {tour.get_status_display()} ({tour.status_label})\n"
            f"Overview: {tour.brief_guide}\n"
            f"Key Highlights:{highlights_str}\n"
            f"Meals Note: {tour.meals_summary}\n"
            f"Transport Note: {tour.transport_summary}\n"
            f"Gujarat Support: {tour.gujarat_support_note}"
        )
        chunks.append({
            "id": f"tour_{tour.slug}_overview",
            "tour_slug": tour.slug,
            "tour_name": tour.name,
            "category": "tour_overview",
            "title": f"{tour.name} - Complete Overview & Pricing",
            "content": content
        })

    # 2. Extract Key Destinations & Dhams
    for dham in DhamDestination.objects.select_related('tour').all():
        content = (
            f"Dham / Destination: {dham.name}\n"
            f"Tour: {dham.tour.name}\n"
            f"Spiritual Significance: {dham.significance}\n"
            f"Description: {dham.description}\n"
            f"Key Highlight: {dham.highlight}"
        )
        chunks.append({
            "id": f"dham_{dham.tour.slug}_{dham.order}",
            "tour_slug": dham.tour.slug,
            "tour_name": dham.tour.name,
            "category": "destination_dham",
            "title": f"{dham.name} ({dham.tour.name})",
            "content": content
        })

    # 3. Extract Itinerary Days
    for day in ItineraryDay.objects.select_related('tour').all():
        schedule_parts = []
        if isinstance(day.schedule, dict):
            for time_slot, activity in day.schedule.items():
                schedule_parts.append(f"- {time_slot.capitalize()}: {activity}")
        schedule_str = "\n".join(schedule_parts) if schedule_parts else "Scheduled transit & darshan"

        tips_str = "\n• " + "\n• ".join(day.darshan_tips) if day.darshan_tips else "Follow tour coordinator instructions."
        scenic_str = ", ".join(day.scenic_points) if day.scenic_points else "Scenic Himalayan routes"

        content = (
            f"Tour: {day.tour.name}\n"
            f"Day {day.day_number}: {day.title}\n"
            f"Route: {day.route_summary}\n"
            f"Starting Point: {day.starting_point} ➔ Destination: {day.destination}\n"
            f"Altitude: {day.altitude or 'Standard mountain altitude'}\n"
            f"Night Stay Hotel: {day.night_stay} ({day.hotel_type} - {day.hotel_name})\n"
            f"Meals Included: {day.meals}\n"
            f"Day Description: {day.intro}\n"
            f"Detailed Schedule:\n{schedule_str}\n"
            f"Darshan & Practical Tips:{tips_str}\n"
            f"Key Points & Scenic Attractions: {scenic_str}"
        )
        chunks.append({
            "id": f"itinerary_{day.tour.slug}_day_{day.day_number}",
            "tour_slug": day.tour.slug,
            "tour_name": day.tour.name,
            "day_number": day.day_number,
            "category": "itinerary_day",
            "title": f"{day.tour.name} - Day {day.day_number}: {day.title}",
            "content": content
        })

    # 4. Extract Inclusions, Exclusions & Pricing
    for pd in PackageDetail.objects.select_related('tour').all():
        inc_str = "\n• " + "\n• ".join(pd.inclusions) if pd.inclusions else ""
        exc_str = "\n• " + "\n• ".join(pd.exclusions) if pd.exclusions else ""
        guidelines_str = "\n• " + "\n• ".join(pd.booking_guidelines) if pd.booking_guidelines else ""

        content = (
            f"Tour: {pd.tour.name}\n"
            f"Package Inclusions:{inc_str}\n"
            f"Package Exclusions:{exc_str}\n"
            f"Booking & Payment Guidelines:{guidelines_str}"
        )
        chunks.append({
            "id": f"package_detail_{pd.tour.slug}",
            "tour_slug": pd.tour.slug,
            "tour_name": pd.tour.name,
            "category": "pricing_inclusions",
            "title": f"{pd.tour.name} - Inclusions, Exclusions & Guidelines",
            "content": content
        })

    # 5. Extract Stay, Travel & Transport Guidelines
    for st in StayAndTravel.objects.select_related('tour').all():
        content = (
            f"Tour: {st.tour.name}\n"
            f"Accommodation Guidelines: {json.dumps(st.hotel_options, ensure_ascii=False)}\n"
            f"Mountain Vehicle Guidelines: {json.dumps(st.vehicle_guidelines, ensure_ascii=False)}\n"
            f"Luggage / Baggage Rules: {json.dumps(st.baggage_rules, ensure_ascii=False)}\n"
            f"Satvik Meals & Food Guidelines: {json.dumps(st.meal_guidelines, ensure_ascii=False)}"
        )
        chunks.append({
            "id": f"stay_travel_{st.tour.slug}",
            "tour_slug": st.tour.slug,
            "tour_name": st.tour.name,
            "category": "logistics",
            "title": f"{st.tour.name} - Hotels, Transport, Baggage & Food",
            "content": content
        })

    # 6. Extract Travel Guide, Senior Citizen & Health Guidelines
    for tg in TravelGuide.objects.select_related('tour').all():
        senior_str = "\n• " + "\n• ".join(tg.senior_citizen_tips) if tg.senior_citizen_tips else ""
        medical_str = "\n• " + "\n• ".join(tg.medical_advisory) if tg.medical_advisory else ""
        packing_str = "\n• " + "\n• ".join(tg.packing_list) if tg.packing_list else ""
        weather_str = "\n• " + "\n• ".join(tg.weather) if tg.weather else ""

        content = (
            f"Tour: {tg.tour.name}\n"
            f"Weather & Best Season:{weather_str}\n"
            f"Essential Packing Checklist:{packing_str}\n"
            f"Medical & High Altitude Fitness Advisory:{medical_str}\n"
            f"Senior Citizen Trek & Doli / Pony / Helicopter Care:{senior_str}"
        )
        chunks.append({
            "id": f"travel_guide_{tg.tour.slug}",
            "tour_slug": tg.tour.slug,
            "tour_name": tg.tour.name,
            "category": "travel_guide",
            "title": f"{tg.tour.name} - Weather, Packing, Health & Senior Care",
            "content": content
        })

    # 7. Extract FAQs & Policies
    for pf in PolicyAndFaq.objects.select_related('tour').all():
        faq_lines = []
        if isinstance(pf.faqs, list):
            for item in pf.faqs:
                if isinstance(item, dict):
                    q = item.get("q") or item.get("question", "")
                    a = item.get("a") or item.get("answer", "")
                    faq_lines.append(f"Q: {q}\nA: {a}")
                elif isinstance(item, str):
                    faq_lines.append(item)
        faq_str = "\n\n".join(faq_lines)

        content = (
            f"Tour: {pf.tour.name}\n"
            f"Frequently Asked Questions (FAQs):\n{faq_str}\n\n"
            f"Cancellation Terms: {json.dumps(pf.cancellation_policy, ensure_ascii=False)}\n"
            f"Payment Schedule: {json.dumps(pf.payment_terms, ensure_ascii=False)}"
        )
        chunks.append({
            "id": f"policy_faq_{pf.tour.slug}",
            "tour_slug": pf.tour.slug,
            "tour_name": pf.tour.name,
            "category": "faq_policy",
            "title": f"{pf.tour.name} - FAQs and Cancellation Terms",
            "content": content
        })

    # 8. Unstructured Document Chunks
    docx_file = BASE_DIR / "source_content" / "Char Dham Yatra.docx"
    docx_chunks = extract_docx_chunks(docx_file)
    chunks.extend(docx_chunks)

    logger.info("Compiled %d knowledge chunks for RAG index", len(chunks))
    return chunks


def build_and_save_index(force_embeddings: bool = True) -> int:
    """
    Builds the knowledge index, generates embeddings via Gemini,
    and caches the result to disk.
    """
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    chunks = build_knowledge_chunks()

    client = get_genai_client() if force_embeddings else None

    if client:
        logger.info("Generating embeddings for %d chunks using %s...", len(chunks), EMBEDDING_MODEL)
        for i, chunk in enumerate(chunks):
            try:
                # Embed title + content
                text_to_embed = f"{chunk['title']}\n\n{chunk['content']}"
                resp = client.models.embed_content(
                    model=EMBEDDING_MODEL,
                    contents=text_to_embed,
                )
                if hasattr(resp, "embeddings") and resp.embeddings:
                    chunk["embedding"] = resp.embeddings[0].values
                elif hasattr(resp, "embedding") and resp.embedding:
                    chunk["embedding"] = resp.embedding.values
            except Exception as e:
                logger.warning("Error generating embedding for chunk %s: %s", chunk["id"], e)
                chunk["embedding"] = []

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    global _IN_MEMORY_INDEX
    _IN_MEMORY_INDEX = chunks
    logger.info("Saved %d indexed knowledge items to %s", len(chunks), INDEX_FILE)
    return len(chunks)


def load_index() -> List[Dict[str, Any]]:
    """Load index from file or memory, auto-building if missing."""
    global _IN_MEMORY_INDEX
    if _IN_MEMORY_INDEX is not None:
        return _IN_MEMORY_INDEX

    if INDEX_FILE.exists():
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as f:
                _IN_MEMORY_INDEX = json.load(f)
                return _IN_MEMORY_INDEX
        except Exception as e:
            logger.error("Failed reading index file %s: %s", INDEX_FILE, e)

    # If file doesn't exist, build without remote embeddings initially for fast cold-start
    build_and_save_index(force_embeddings=False)
    return _IN_MEMORY_INDEX or []


def retrieve_context(query: str, top_k: int = 4, tour_slug: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Hybrid Search combining:
    1. Dense vector cosine similarity (if query embedding can be calculated)
    2. BM25 / token matching
    3. Metadata filtering (by tour_slug or day number)
    """
    chunks = load_index()
    if not chunks:
        return []

    client = get_genai_client()
    query_vector = None

    if client:
        try:
            resp = client.models.embed_content(
                model=EMBEDDING_MODEL,
                contents=query,
            )
            if hasattr(resp, "embeddings") and resp.embeddings:
                query_vector = resp.embeddings[0].values
            elif hasattr(resp, "embedding") and resp.embedding:
                query_vector = resp.embedding.values
        except Exception as e:
            logger.debug("Failed computing query embedding: %s", e)

    query_tokens = [t.lower() for t in query.replace("?", " ").replace(",", " ").split() if len(t) > 2]

    scored_chunks = []
    for c in chunks:
        # Optional filter by tour
        if tour_slug and c.get("tour_slug") and c.get("tour_slug") != tour_slug:
            continue

        vector_score = 0.0
        if query_vector and c.get("embedding"):
            vector_score = max(0.0, cosine_similarity(query_vector, c["embedding"]))

        keyword_score = compute_keyword_score(query_tokens, c.get("content", ""), c.get("title", ""))

        # Check for day match in query
        day_boost = 0.0
        if c.get("day_number"):
            day_str = f"day {c['day_number']}"
            if day_str in query.lower():
                day_boost = 0.35

        # Hybrid weighting
        if query_vector:
            final_score = (vector_score * 0.60) + (keyword_score * 0.40) + day_boost
        else:
            final_score = keyword_score + day_boost

        if final_score > 0.05:
            scored_chunks.append((final_score, c))

    scored_chunks.sort(key=lambda x: x[0], reverse=True)
    return [chunk for score, chunk in scored_chunks[:top_k]]
