"""
Agent Service for Swarnav Tour & Travels.
Orchestrates Google Gemini (Gemini 2.5/1.5 Flash), tool execution,
multi-source RAG retrieval, and session memory management.
"""
import logging
import json
from typing import List, Dict, Any, Optional

from core.ai.ai_config import get_genai_client, GEMINI_MODEL, is_ai_configured
from core.ai.rag_engine import retrieve_context
from core.ai.agent_tools import (
    AVAILABLE_AGENT_TOOLS,
    get_tour_itinerary_details,
    calculate_yatra_price,
    check_travel_guidelines,
    save_booking_inquiry
)

logger = logging.getLogger(__name__)

SYSTEM_INSTRUCTION = """You are the official AI Pilgrimage Assistant for "Swarnav Tour & Travels" (સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સ), based in Surat, Gujarat.

Your mission is to provide warm, polite, culturally respectful, and highly accurate guidance to pilgrims planning sacred journeys.

CORE IDENTITY & GUIDELINES:
1. **Respectful Devotional Tone**:
   - Begin answers with warm devotional greetings when starting a conversation: "🙏 Jai Shri Krishna / Har Har Mahadev!" or "નમસ્તે / હર હર મહાદેવ!".
   - Embody Indian hospitality ("Atithi Devo Bhava") with patience, respect for elders, and helpfulness.

2. **Multilingual Fluency**:
   - Answer in the EXACT language the user communicates in:
     - If the user writes in Gujarati (ગુજરાતી), answer in natural, respectful Gujarati.
     - If the user writes in Hindi (हिंदी), answer in polite Devanagari Hindi.
     - If the user writes in English, answer in clear, articulate English.
     - If the user writes in Hinglish or Gujlish (e.g. "Kedarnath mate senior citizen doli male?"), answer with warm conversational clarity.

3. **Grounding & Accuracy**:
   - Use the retrieved knowledge base and tools to give precise details:
     - **Char Dham Yatra**: 13 Days / 12 Nights starting from ₹30,000 per person (Triple-sharing). Traditional sequence: Surat ➔ Haridwar ➔ Barkot (Yamunotri) ➔ Uttarkashi (Gangotri) ➔ Sonprayag (Kedarnath) ➔ Pipalkoti/Badrinath ➔ Haridwar ➔ Surat. Includes return train from Surat, mountain coaches, hotel stays, hygienic pure vegetarian Satvik meals (daily lunch & dinner), biometric registration, and dedicated tour coordinator.
     - **Panch Kedar**: 10 Days (₹26,500).
     - **Kashmir Paradise**: 7 Days (₹22,500).
     - **South India (Rameshwaram & Kerala)**: Rameshwaram Circuit 8 Days (₹24,000), Kerala 6 Days (₹19,500).
     - **East India (Jagannath Puri & Jharkhand)**: 11 Days (₹24,500) covering Puri, Konark, Kolkata, Gangasagar, Baidyanath Jyotirlinga, and Varanasi.
     - **Nepal**: Pashupatinath & Muktinath 8 Days (₹34,500).
   - **Senior Citizens**: Mention that Swarnav itineraries are paced gently, and our tour coordinator assists on-ground with Palki/Doli, Pony, and helicopter shuttle booking tokens at Kedarnath (16 km trek from Gaurikund) and Yamunotri (6 km trek).
   - **Food**: Pure vegetarian Satvik food prepared fresh; Jain food (without onion/garlic) arranged on prior notice.
   - **Departures**: Main coordinated departures are from Surat Railway Station, with connecting trains/flights arranged for pilgrims joining from Ahmedabad, Vadodara, Rajkot, Bhavnagar, Mumbai, etc.

4. **Agentic Action & Lead Capture**:
   - When users express interest in booking, asking to be contacted, or providing their phone number and group details, invoke the `save_booking_inquiry` tool.
   - When asked for day-by-day routes, elevations, or stays, use `get_tour_itinerary_details`.
   - When asked for cost breakdowns for group sizes, use `calculate_yatra_price`.
   - When asked for health/senior tips, use `check_travel_guidelines`.

5. **Format**:
   - Use clean Markdown with bolding, bullet points, and concise paragraphs.
   - Never make up false hotel names or arbitrary prices not found in the knowledge context.
"""


def _local_fallback_response(query: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Intelligent local fallback when Gemini API key is missing or offline.
    Uses RAG retrieval and local tool execution to answer accurately.
    """
    query_lower = query.lower()

    import re
    # Check if user is submitting a phone number / inquiry intent
    phone_match = re.search(r'(\+?\d{10,13})', query)
    if ("book" in query_lower or "call me" in query_lower or "contact" in query_lower or "mobile" in query_lower or "phone" in query_lower or "નંબર" in query or "फोन" in query) and phone_match:
        digits = phone_match.group(1)
        name_guess = "Devotee"
        for word in query.split():
            clean_w = word.strip(".,;:!?")
            if clean_w.isalpha() and clean_w.lower() not in ["my", "name", "is", "please", "call", "book", "tour", "yatra", "phone", "and", "for", "seats"]:
                name_guess = clean_w.capitalize()
                break

        res = save_booking_inquiry(name=name_guess, phone=digits, tour_slug="char-dham")
        return {
            "reply": (
                f"🙏 **Har Har Mahadev / Jai Shri Krishna!**\n\n"
                f"Thank you, {name_guess}. We have recorded your yatra inquiry **(Ref: #{res.get('inquiry_ref', 'NEW')})**.\n\n"
                f"Our senior tour coordinator will reach out to you directly at **{digits}** with complete batch schedules, berth details, and seat availability.\n\n"
                f"You can also immediately message us on WhatsApp with this inquiry reference by clicking the button below."
            ),
            "action_card": {
                "type": "lead_created",
                "inquiry_ref": res.get("inquiry_ref"),
                "whatsapp_link": res.get("whatsapp_link")
            },
            "suggested_questions": [
                "What documents are required for Char Dham registration?",
                "Can senior citizens get Doli or Helicopter for Kedarnath?",
                "What is the complete 13-day itinerary schedule?"
            ]
        }

    # Check for price calculation intent
    if "how much" in query_lower or "price" in query_lower or "cost" in query_lower or "rate" in query_lower or "ખર્ચ" in query or "ભાવ" in query or "કિંમત" in query or "ભાડું" in query or "फीस" in query:
        tour_slug = "char-dham"
        if "puri" in query_lower or "jagannath" in query_lower:
            tour_slug = "jagannath-puri"
        elif "nepal" in query_lower:
            tour_slug = "nepal-pashupatinath-muktinath"
        elif "south" in query_lower or "rameshwaram" in query_lower:
            tour_slug = "rameshwaram-circuit"
        elif "kashmir" in query_lower:
            tour_slug = "kashmir-paradise"
        elif "kedar" in query_lower and "panch" in query_lower:
            tour_slug = "panch-kedar"

        # Count travelers
        count = 1
        for w in query.split():
            if w.isdigit():
                count = int(w)
                break

        calc = calculate_yatra_price(tour_slug=tour_slug, number_of_pilgrims=count)
        return {
            "reply": (
                f"🙏 **Jai Shri Krishna / Har Har Mahadev!**\n\n"
                f"Here is the package pricing estimate for **{calc.get('tour_name')}**:\n\n"
                f"• **Duration:** {calc.get('duration')}\n"
                f"• **Estimated Rate:** {calc.get('estimated_rate_per_person')} per person ({calc.get('sharing_type')})\n"
                f"• **Total Estimated Cost for {count} Pilgrim(s):** **{calc.get('estimated_total')}**\n\n"
                f"**What's Included in this Package:**\n"
                f"• Surat to Haridwar return train tickets (or connecting options for Ahmedabad/Vadodara/Rajkot)\n"
                f"• Dedicated mountain group coach transport\n"
                f"• Hotel stays across all night stops\n"
                f"• Fresh, hygienic, pure vegetarian Satvik Lunch & Dinner daily\n"
                f"• Dedicated on-ground tour coordinator & biometric registration assistance\n\n"
                f"*Note: Would you like to check seat availability for an upcoming batch or arrange double-sharing rooms?*"
            ),
            "suggested_questions": [
                "Tell me about senior citizen facilities and doli/pony options",
                "What is the day-by-day route from Surat?",
                "How do I book seats for my family?"
            ]
        }

    # Retrieve RAG context
    rag_chunks = retrieve_context(query, top_k=3)
    if rag_chunks:
        top_chunk = rag_chunks[0]
        context_snippets = "\n\n".join([f"**{c.get('title')}**:\n{c.get('content')}" for c in rag_chunks[:2]])
        return {
            "reply": (
                f"🙏 **Jai Shri Krishna / Har Har Mahadev!**\n\n"
                f"Regarding your question, here are the verified details from Swarnav Tour & Travels:\n\n"
                f"{context_snippets}\n\n"
                f"Our primary departures are comfortably coordinated from **Surat Railway Station**, and we provide full support for connecting pilgrims from Ahmedabad, Vadodara, and across Gujarat.\n\n"
                f"Feel free to ask more details about specific days, packing checklists, or batch dates!"
            ),
            "suggested_questions": [
                "What is the Char Dham Yatra 13-day package price?",
                "How can senior citizens prepare for Kedarnath trek?",
                "What meals and hotels are provided during the yatra?"
            ]
        }

    return {
        "reply": (
            "🙏 **Jai Shri Krishna / Har Har Mahadev!**\n\n"
            "Welcome to **Swarnav Tour & Travels**. We organize premium, worry-free pilgrimages including:\n"
            "• **Char Dham Yatra (13 Days)** – Yamunotri, Gangotri, Kedarnath & Badrinath (₹30,000/person)\n"
            "• **Jagannath Puri & Eastern Divine Circuit (11 Days)** – Puri, Konark, Kolkata, Gangasagar, Baidyanath & Varanasi (₹24,500/person)\n"
            "• **Nepal Holy Shrines (8 Days)** – Pashupatinath & Muktinath Dham (₹34,500/person)\n"
            "• **South India Divine Circuits** – Rameshwaram (8 Days) & Kerala (6 Days)\n"
            "• **Panch Kedar & Kashmir Valley Tours**\n\n"
            "All departures are coordinated from **Surat, Gujarat** with satvik meals, comfortable hotels, and dedicated coordinators.\n\n"
            "What destination or details can I help you with today?"
        ),
        "suggested_questions": [
            "Char Dham 13-Day Itinerary & Price",
            "Kedarnath Helicopter and Doli Details",
            "Departure details for travelers from Gujarat"
        ]
    }


def execute_agent_chat(user_message: str, session_history: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
    """
    Main entry point for conversational agent.
    1. Retrieves RAG context.
    2. Sends query + grounding context + tools to Gemini.
    3. Executes function calls if returned by the model.
    4. Returns final markdown response, action cards, and suggestions.
    """
    session_history = session_history or []

    # Check if Gemini client is active
    client = get_genai_client()
    if not client:
        logger.info("Gemini API key not configured or client inactive. Using local RAG fallback engine.")
        return _local_fallback_response(user_message, session_history)

    try:
        from google.genai import types

        # 1. Retrieve RAG grounding context
        retrieved_chunks = retrieve_context(user_message, top_k=4)
        rag_context_text = ""
        if retrieved_chunks:
            rag_context_text = "\n\n--- RETRIEVED FACTUAL KNOWLEDGE (GROUNDING TRUTH) ---\n"
            for c in retrieved_chunks:
                rag_context_text += f"Source [{c.get('title', 'Knowledge Chunk')}]:\n{c.get('content', '')}\n\n"

        # 2. Build system instructions with RAG injected
        full_system_prompt = f"{SYSTEM_INSTRUCTION}\n\n{rag_context_text}"

        # 3. Format contents with history
        contents = []
        for turn in session_history[-6:]:
            role = "user" if turn.get("sender") == "user" else "model"
            contents.append(types.Content(
                role=role,
                parts=[types.Part.from_text(text=turn.get("text", ""))]
            ))

        contents.append(types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_message)]
        ))

        # 4. Generate content with function calling tools
        config = types.GenerateContentConfig(
            system_instruction=full_system_prompt,
            temperature=0.3,
            tools=AVAILABLE_AGENT_TOOLS,
        )

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=contents,
            config=config,
        )

        action_card = None
        executed_tool_results = []

        # 5. Check if model requested tool execution (Function Calling loop)
        if response.function_calls:
            tool_parts = []
            for func_call in response.function_calls:
                func_name = func_call.name
                func_args = dict(func_call.args) if func_call.args else {}
                logger.info("Agent invoked tool: %s with args: %s", func_name, func_args)

                tool_result = {}
                if func_name == "get_tour_itinerary_details":
                    tool_result = get_tour_itinerary_details(**func_args)
                elif func_name == "calculate_yatra_price":
                    tool_result = calculate_yatra_price(**func_args)
                elif func_name == "check_travel_guidelines":
                    tool_result = check_travel_guidelines(**func_args)
                elif func_name == "save_booking_inquiry":
                    tool_result = save_booking_inquiry(**func_args)
                    if tool_result.get("status") == "success":
                        action_card = {
                            "type": "lead_created",
                            "inquiry_ref": tool_result.get("inquiry_ref"),
                            "whatsapp_link": tool_result.get("whatsapp_link"),
                            "phone": tool_result.get("phone")
                        }

                executed_tool_results.append({
                    "tool": func_name,
                    "args": func_args,
                    "result": tool_result
                })

                tool_parts.append(types.Part.from_function_response(
                    name=func_name,
                    response={"result": tool_result}
                ))

            # Send tool outputs back to Gemini for final grounded synthesis
            turn_contents = list(contents)
            # Add the model's call parts
            turn_contents.append(response.candidates[0].content)
            # Add the user/function response parts
            turn_contents.append(types.Content(role="user", parts=tool_parts))

            final_response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=turn_contents,
                config=types.GenerateContentConfig(
                    system_instruction=full_system_prompt,
                    temperature=0.3
                )
            )
            final_reply_text = final_response.text or "Here are the verified details for your pilgrimage request."
        else:
            final_reply_text = response.text or "🙏 Namaste! How can I assist you with your sacred journey today?"

        # 6. Generate contextual suggested follow-ups
        suggested_questions = [
            "What is the Char Dham 13-day package price?",
            "Can senior citizens get Doli or Helicopter for Kedarnath?",
            "How do we book departures from Surat / Gujarat?"
        ]

        if "kedarnath" in user_message.lower():
            suggested_questions = [
                "What are the rates for Doli and Pony at Kedarnath?",
                "Tell me about Day 7 trek route from Sonprayag",
                "How do I book my seats for the next batch?"
            ]
        elif "puri" in user_message.lower() or "jagannath" in user_message.lower():
            suggested_questions = [
                "What is the complete 11-day route for Jagannath Puri?",
                "Which temples are covered in Kolkata and Varanasi?",
                "How do I inquire for a family group booking?"
            ]
        elif "price" in user_message.lower() or "cost" in user_message.lower() or "ભાવ" in user_message:
            suggested_questions = [
                "What items and meals are included in the price?",
                "Are there special discounts for senior citizens or families?",
                "I want to book my seats via WhatsApp"
            ]

        return {
            "reply": final_reply_text,
            "action_card": action_card,
            "suggested_questions": suggested_questions,
            "tools_used": [t["tool"] for t in executed_tool_results]
        }

    except Exception as exc:
        logger.exception("Error in execute_agent_chat: %s", exc)
        return _local_fallback_response(user_message, session_history)
