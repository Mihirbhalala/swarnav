"""
Granular Hybrid RAG Engine for Swarnav Tour & Travels AI Assistant.
Combines semantic embeddings (OpenAI text-embedding-3-small or Gemini text-embedding-004)
with high-precision lexical token matching and intent-targeted micro-chunking.
Prevents giant text dumps and delivers concise, direct answers.
"""
import os
import re
import json
import math
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

from core.ai.ai_config import (
    get_openai_client,
    get_genai_client,
    OPENAI_EMBEDDING_MODEL,
    GEMINI_EMBEDDING_MODEL,
    BASE_DIR
)

logger = logging.getLogger(__name__)

INDEX_DIR = BASE_DIR / "core" / "ai" / "data"
INDEX_FILE = INDEX_DIR / "knowledge_index.json"

_IN_MEMORY_INDEX: Optional[List[Dict[str, Any]]] = None


# Tour aliases mapping for normalization
TOUR_ALIASES = {
    "char-dham": [
        "chardham", "char dham", "char-dham", "kedarnath", "badrinath", "yamunotri", "gangotri",
        "ચારધામ", "ચાર ધામ", "કેદારનાથ", "બદ્રીનાથ", "યમુનોત્રી", "ગંગોત્રી",
        "चारधाम", "चार धाम", "केदारनाथ", "बद्रीनाथ", "यमुनोत्री", "गंगोत्री"
    ],
    "panch-kedar": [
        "panch kedar", "panchkedar", "tungnath", "rudranath", "madhyamaheshwar", "kalpeshwar",
        "પંચ કેદાર", "પંચકેદાર", "તુંગનાથ", "पंच केदार", "पंचकेदार", "तुंगनाथ"
    ],
    "kashmir-paradise": [
        "kashmir", "vaishno devi", "vaishnodevi", "katra", "gulmarg", "sonmarg", "pahalgam",
        "કાશ્મીર", "વૈષ્ણોદેવી", "કાટરા", "ગુલમર્ગ", "कश्मीर", "वैष्णो देवी", "कटरा"
    ],
    "jagannath-puri": [
        "puri", "jagannath", "jagannath puri", "konark", "gangasagar", "baidyanath", "varanasi",
        "જગન્નાથ", "પુરી", "કોણાર્ક", "વારાણસી", "जगन्नाथ", "पुरी", "कोणार्क", "वाराणसी"
    ],
    "nepal-pashupatinath-muktinath": [
        "nepal", "pashupatinath", "muktinath", "pokhara", "kathmandu",
        "નેપાળ", "પશુપતિનાથ", "મુક્તિનાથ", "नेपाल", "पशुपतिनाथ", "मुक्तिनाथ"
    ],
    "rameshwaram-circuit": [
        "rameshwaram", "rameswaram", "madurai", "kanyakumari", "dhanushkodi", "tiruchendur", "south india",
        "રામેશ્વરમ", "મદુરાઈ", "કન્યાકુમારી", "દક્ષિણ ભારત", "रामेश्वरम", "मदुरै", "कन्याकुमारी"
    ],
    "kerala-tour": [
        "kerala", "munnar", "thekkady", "alleppey", "backwaters", "kovalam", "kochi",
        "કેરળ", "મુન્નાર", "એલેપ્પી", "કેરાલા", "केरल", "मुन्नार", "एलेप्पी"
    ],
    "jharkhand-tour": [
        "jharkhand", "shikharji", "sammed shikharji", "deoghar", "parasnath",
        "ઝારખંડ", "શિખરજી", "ઝારખંડ ટૂર", "झारखंड", "शिखरजी"
    ]
}

# Intent keywords mapping
INTENT_KEYWORDS = {
    "pricing": [
        "price", "pricing", "package", "cost", "rate", "how much", "charges", "fees", "starting package",
        "દર", "ભાવ", "કિંમત", "ખર્ચ", "ભાડું", "પેકેજ", "કિતના", "दाम", "लागत", "फीस", "मूल्य"
    ],
    "dates": [
        "date", "dates", "start date", "starting date", "when", "start", "batch", "upcoming batch", "schedule",
        "departure date", "open", "month", "season", "તારીખ", "ક્યારે શરૂ", "શરૂઆત", "બેચ", "કયા મહિને",
        "तारीख", "कब शुरू", "प्रारंभ", "तारीखें", "शुरुआत"
    ],
    "transport": [
        "train", "flight", "bus", "coach", "travel", "pickup", "drop", "origin", "from where", "departure",
        "surat", "ahmedabad", "reach", "ટ્રેન", "બસ", "સુરત", "ક્યાંથી", "ઉપડશે", "ट्रेन", "सूरत", "कहाँ से"
    ],
    "food": [
        "food", "meal", "meals", "satvik", "jain", "dinner", "lunch", "breakfast", "veg", "vegetarian",
        "જમવાનું", "ભોજન", "સાત્વિક", "જૈન", "ખોરાક", "खाना", "भोजन", "सात्विक", "जैन"
    ],
    "stay": [
        "hotel", "stay", "room", "rooms", "accommodation", "sharing", "triple", "double", "night stay",
        "હોટેલ", "રોકાણ", "રૂમ", "શેરિંગ", "होटल", "कमरा", "रुकना"
    ],
    "senior": [
        "senior", "senior citizen", "elderly", "parents", "doli", "palki", "pony", "horse", "helicopter", "heli",
        "trek", "walking", "altitude", "વડીલો", "ડોળી", "પાલખી", "ઘોડો", "હેલિકોપ્ટર", "ટ્રેક", "पालकी", "डोली", "घोड़ा", "हेलीकॉप्टर"
    ],
    "inclusions": [
        "included", "inclusion", "inclusions", "excluded", "exclusion", "covers", "what is included",
        "શું સમાવેશ", "શું મળશે", "क्या शामिल", "सुविधाएं"
    ]
}


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


def detect_tour_from_query(query: str) -> Optional[str]:
    """Detect which tour package is referenced in the query."""
    q_clean = query.lower().replace("-", " ")
    for slug, aliases in TOUR_ALIASES.items():
        for alias in aliases:
            if alias in q_clean:
                return slug
    return None


def detect_intents_from_query(query: str) -> List[str]:
    """Detect topics/intents present in the query."""
    q_lower = query.lower()
    matched_intents = []
    for intent, kws in INTENT_KEYWORDS.items():
        if any(kw in q_lower for kw in kws):
            matched_intents.append(intent)
    return matched_intents


def build_knowledge_chunks() -> List[Dict[str, Any]]:
    """
    Build highly granular, discrete knowledge chunks from Django DB models.
    Each chunk is dedicated to a single topic (e.g. price, batch dates, transport, food).
    """
    from yatras.models import (
        TourPackage, ItineraryDay, DhamDestination,
        PackageDetail, StayAndTravel, TravelGuide, PolicyAndFaq
    )

    chunks = []

    for tour in TourPackage.objects.all():
        slug = tour.slug
        name = tour.name

        # 1. PRICING & DURATION CHUNK
        price_content = (
            f"Tour: {name}\n"
            f"Duration: {tour.duration_display} ({tour.duration_days} Days / {tour.duration_nights} Nights)\n"
            f"Starting Package Rate: {tour.starting_price} ({tour.price_note or 'per person on Triple-sharing basis'})\n"
            f"Double-sharing Option: Available with a standard surcharge for private twin/double rooms."
        )
        chunks.append({
            "id": f"{slug}_pricing",
            "tour_slug": slug,
            "tour_name": name,
            "category": "pricing",
            "title": f"{name} - Package Price & Duration",
            "content": price_content,
            "keywords": ["price", "package", "cost", "starting price", "starting package", "rate", "duration", "days", "nights", slug, name.lower()]
        })

        # 2. DATES & BATCHES CHUNK
        batch_date = tour.tour_date or tour.status_label or "Departures Open for Inquiry"
        dates_content = (
            f"Tour: {name}\n"
            f"Upcoming Confirmed Batch: {batch_date}\n"
            f"Current Booking Status: {tour.get_status_display()} ({tour.status_label or 'Active'})\n"
            f"Booking Advisory: Fixed batch seats are limited; advance booking token is recommended to secure berths."
        )
        chunks.append({
            "id": f"{slug}_dates",
            "tour_slug": slug,
            "tour_name": name,
            "category": "dates",
            "title": f"{name} - Starting Dates & Batch Schedule",
            "content": dates_content,
            "keywords": ["date", "starting date", "batch", "schedule", "when", "departure date", "open", "month", slug, name.lower()]
        })

        # 3. ORIGIN & TRANSPORT CHUNK
        origin_content = (
            f"Tour: {name}\n"
            f"Starting & Ending Origin: {tour.origin or 'Starts & Ends at Surat, Gujarat'}\n"
            f"Train Transport: Confirmed round-trip train travel included from Surat to destination gateway.\n"
            f"Mountain / Local Coach: Dedicated group touring coach provided for the entire pilgrimage route.\n"
            f"Gujarat Connectivity: Connecting trains or flights arranged for pilgrims joining from Ahmedabad, Vadodara, Rajkot, Bhavnagar, Mumbai, etc."
        )
        chunks.append({
            "id": f"{slug}_transport",
            "tour_slug": slug,
            "tour_name": name,
            "category": "transport",
            "title": f"{name} - Origin Surat & Transport Logistics",
            "content": origin_content,
            "keywords": ["transport", "train", "coach", "bus", "origin", "surat", "ahmedabad", "gujarat", "departure point", slug]
        })

        # 4. SATVIK MEALS & FOOD CHUNK
        meals_text = tour.meals_summary or "Hygienic pure vegetarian Satvik meals (daily lunch and dinner) included as per schedule."
        food_content = (
            f"Tour: {name}\n"
            f"Food Details: {meals_text}\n"
            f"Satvik Standard: Freshly cooked pure vegetarian food suited for pilgrims.\n"
            f"Jain Food: Specially prepared Jain meals (without onion/garlic) arranged upon prior notice."
        )
        chunks.append({
            "id": f"{slug}_food",
            "tour_slug": slug,
            "tour_name": name,
            "category": "food",
            "title": f"{name} - Satvik Meals & Jain Food",
            "content": food_content,
            "keywords": ["food", "meal", "satvik", "jain", "lunch", "dinner", "vegetarian", slug]
        })

        # 5. HOTEL & STAY CHUNK
        stay_text = tour.accommodation_summary or "Verified, clean economy hotel stays & mountain guest houses at all night stops with warm water facilities."
        stay_content = (
            f"Tour: {name}\n"
            f"Accommodation: {stay_text}\n"
            f"Room Options: Standard package based on Triple-sharing; Double-sharing / Twin rooms available upon request."
        )
        chunks.append({
            "id": f"{slug}_stay",
            "tour_slug": slug,
            "tour_name": name,
            "category": "stay",
            "title": f"{name} - Hotels & Accommodation",
            "content": stay_content,
            "keywords": ["hotel", "stay", "room", "accommodation", "triple sharing", "double sharing", slug]
        })

        # 6. INCLUSIONS & EXCLUSIONS CHUNK
        pd = PackageDetail.objects.filter(tour=tour).first()
        inc_list = pd.inclusions[:5] if pd and pd.inclusions else [
            "Surat to destination round-trip train transport",
            "Dedicated group tourist coach for all transfers & sightseeing",
            "Hotel accommodations across all night stops",
            "Daily hygienic pure vegetarian Satvik meals (Lunch & Dinner)",
            "Yatra biometric registration assistance & dedicated tour coordinator"
        ]
        inc_content = (
            f"Tour: {name}\n"
            f"Key Inclusions:\n• " + "\n• ".join(inc_list) + "\n"
            f"Exclusions: Personal expenses (shopping, laundry, tips), helicopter/pony/palki charges, personal medical needs."
        )
        chunks.append({
            "id": f"{slug}_inclusions",
            "tour_slug": slug,
            "tour_name": name,
            "category": "inclusions",
            "title": f"{name} - Package Inclusions & Exclusions",
            "content": inc_content,
            "keywords": ["inclusions", "exclusions", "included", "what is included", slug]
        })

        # 7. SENIOR CITIZEN & SPECIAL ASSISTANCE CHUNK
        tg = TravelGuide.objects.filter(tour=tour).first()
        senior_notes = (
            "Swarnav itineraries are paced gently for senior citizens. "
            "For high-altitude treks like Kedarnath (16 km) and Yamunotri (6 km), our on-ground tour coordinator "
            "assists devotees with verified local Palki / Doli (approx ₹8,000–₹12,000 round trip), Pony (approx ₹4,000–₹6,000), "
            "or official IRCTC Helicopter shuttle booking tokens from Phata/Guptkashi/Sirsi."
        )
        chunks.append({
            "id": f"{slug}_senior",
            "tour_slug": slug,
            "tour_name": name,
            "category": "senior",
            "title": f"{name} - Senior Citizen Care, Doli & Helicopter",
            "content": f"Tour: {name}\nSenior Care & Trek Assistance: {senior_notes}",
            "keywords": ["senior", "senior citizen", "elderly", "doli", "palki", "pony", "horse", "helicopter", "heli", "trek", slug]
        })

        # 8. SACRED SHRINES & HIGH-LEVEL OVERVIEW
        shrines_content = (
            f"Tour: {name}\n"
            f"Region: {tour.region}\n"
            f"Sacred Shrines: {tour.subtitle}\n"
            f"Key Summary: {tour.brief_guide or 'Divine pilgrimage guided end-to-end by experienced Swarnav yatra escorts.'}"
        )
        chunks.append({
            "id": f"{slug}_overview",
            "tour_slug": slug,
            "tour_name": name,
            "category": "overview",
            "title": f"{name} - Sacred Shrines Overview",
            "content": shrines_content,
            "keywords": ["overview", "shrines", "temples", "darshan", slug, name.lower()]
        })

    # 9. GRANULAR DAY-BY-DAY ITINERARY CHUNKS (For specific Day X queries only)
    for day in ItineraryDay.objects.select_related('tour').all():
        day_content = (
            f"Tour: {day.tour.name}\n"
            f"Day {day.day_number}: {day.title}\n"
            f"Route: {day.route_summary}\n"
            f"Transit: {day.starting_point} ➔ {day.destination}\n"
            f"Night Stay: {day.night_stay} ({day.hotel_type})\n"
            f"Meals: {day.meals}\n"
            f"Key Activity: {day.intro}"
        )
        chunks.append({
            "id": f"{day.tour.slug}_day_{day.day_number}",
            "tour_slug": day.tour.slug,
            "tour_name": day.tour.name,
            "day_number": day.day_number,
            "category": "itinerary_day",
            "title": f"{day.tour.name} - Day {day.day_number}: {day.title}",
            "content": day_content,
            "keywords": [f"day {day.day_number}", f"day{day.day_number}", day.title.lower(), day.tour.slug]
        })

    logger.info("Compiled %d fine-grained knowledge micro-chunks for RAG index", len(chunks))
    return chunks


def build_and_save_index(force_embeddings: bool = True) -> int:
    """
    Builds granular knowledge chunks, generates vector embeddings,
    and caches to disk.
    """
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    chunks = build_knowledge_chunks()

    openai_client = get_openai_client()
    genai_client = get_genai_client() if not openai_client else None

    if force_embeddings and (openai_client or genai_client):
        logger.info("Generating vector embeddings for %d micro-chunks...", len(chunks))
        for chunk in chunks:
            text_to_embed = f"{chunk['title']}\n{chunk['content']}"
            embedding = []
            if openai_client:
                try:
                    resp = openai_client.embeddings.create(
                        model=OPENAI_EMBEDDING_MODEL,
                        input=text_to_embed
                    )
                    embedding = resp.data[0].embedding
                except Exception as e:
                    logger.warning("OpenAI embedding error for chunk %s: %s", chunk["id"], e)
            elif genai_client:
                try:
                    resp = genai_client.models.embed_content(
                        model=GEMINI_EMBEDDING_MODEL,
                        contents=text_to_embed
                    )
                    if hasattr(resp, "embeddings") and resp.embeddings:
                        embedding = resp.embeddings[0].values
                    elif hasattr(resp, "embedding") and resp.embedding:
                        embedding = resp.embedding.values
                except Exception as e:
                    logger.warning("Gemini embedding error for chunk %s: %s", chunk["id"], e)

            chunk["embedding"] = embedding

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    global _IN_MEMORY_INDEX
    _IN_MEMORY_INDEX = chunks
    logger.info("Saved %d granular knowledge micro-chunks to %s", len(chunks), INDEX_FILE)
    return len(chunks)


def load_index() -> List[Dict[str, Any]]:
    """Load granular index from file or memory, auto-building if missing."""
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

    build_and_save_index(force_embeddings=False)
    return _IN_MEMORY_INDEX or []


def retrieve_context(query: str, top_k: int = 2) -> List[Dict[str, Any]]:
    """
    Fine-Grained Retrieval:
    1. Detects target tour (e.g. Char Dham, Kashmir, Jagannath Puri).
    2. Detects target intent (e.g. pricing, dates, food, transport, senior citizen, specific day).
    3. Computes vector similarity if embeddings exist.
    4. Combines with intent-matching & keyword boost to return ONLY the 1-2 most relevant micro-chunks.
    """
    chunks = load_index()
    if not chunks:
        return []

    target_tour = detect_tour_from_query(query)
    target_intents = detect_intents_from_query(query)

    # Check for specific day query (e.g., "Day 7", "Day 3")
    day_match = re.search(r'\bday\s*(\d+)\b', query.lower())
    target_day = int(day_match.group(1)) if day_match else None

    # Check if query vector can be computed
    query_vector = None
    openai_client = get_openai_client()
    genai_client = get_genai_client() if not openai_client else None

    if openai_client:
        try:
            resp = openai_client.embeddings.create(
                model=OPENAI_EMBEDDING_MODEL,
                input=query
            )
            query_vector = resp.data[0].embedding
        except Exception as e:
            logger.debug("Failed computing OpenAI query embedding: %s", e)
    elif genai_client:
        try:
            resp = genai_client.models.embed_content(
                model=GEMINI_EMBEDDING_MODEL,
                contents=query
            )
            if hasattr(resp, "embeddings") and resp.embeddings:
                query_vector = resp.embeddings[0].values
        except Exception as e:
            logger.debug("Failed computing Gemini query embedding: %s", e)

    query_tokens = [w for w in re.split(r'\W+', query.lower()) if len(w) > 2]

    scored = []
    for c in chunks:
        score = 0.0
        c_tour = c.get("tour_slug")
        c_cat = c.get("category", "")
        c_day = c.get("day_number")

        # 1. Tour match bonus / penalty
        if target_tour:
            if c_tour == target_tour:
                score += 3.0
            else:
                score -= 4.0  # Strongly suppress chunks from wrong tours

        # 2. Specific day match
        if target_day is not None:
            if c_cat == "itinerary_day" and c_day == target_day:
                score += 5.0
            elif c_cat == "itinerary_day":
                score -= 3.0
        else:
            # If user didn't ask for a specific day, suppress individual day chunks
            if c_cat == "itinerary_day":
                score -= 2.0

        # 3. Intent match bonus
        for intent in target_intents:
            if c_cat == intent:
                score += 2.5
            elif intent == "pricing" and c_cat in ["pricing", "inclusions"]:
                score += 2.0
            elif intent == "dates" and c_cat == "dates":
                score += 2.5

        # 4. Dense Vector Cosine Similarity
        if query_vector and c.get("embedding"):
            sim = cosine_similarity(query_vector, c["embedding"])
            score += sim * 2.5

        # 5. Keyword Overlap
        text_corpus = (c.get("title", "") + " " + c.get("content", "") + " " + " ".join(c.get("keywords", []))).lower()
        matches = sum(1 for tok in query_tokens if tok in text_corpus)
        if matches:
            score += min(2.0, matches * 0.4)

        if score > 0.5:
            scored.append((score, c))

    scored.sort(key=lambda x: x[0], reverse=True)

    # Return top K micro-chunks
    # If both pricing and dates were asked (e.g. "starting date and starting package"), ensure we return both!
    if "pricing" in target_intents and "dates" in target_intents and target_tour:
        pricing_chunk = next((c for s, c in scored if c.get("category") == "pricing"), None)
        dates_chunk = next((c for s, c in scored if c.get("category") == "dates"), None)
        selected = []
        if pricing_chunk:
            selected.append(pricing_chunk)
        if dates_chunk and dates_chunk not in selected:
            selected.append(dates_chunk)
        if selected:
            return selected[:top_k]

    return [chunk for score, chunk in scored[:top_k]]
