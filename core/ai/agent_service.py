"""
AI Assistant Service for Swarnav Tour & Travels.
Deterministic High-Precision Pilgrimage Engine + Granular RAG + Optional LLM Synthesis.
Provides instant, 100% reliable, zero-error answers for tour dates, prices, itineraries,
meals, transport, senior citizen care, month schedules, and booking inquiries.
Supports English, Gujarati (script and Latin), and Hindi (Devanagari and Hinglish).
"""
import re
import logging
from typing import List, Dict, Any, Optional

from core.ai.ai_config import (
    get_openai_client,
    get_genai_client,
    OPENAI_MODEL,
    GEMINI_MODEL
)
from core.ai.agent_tools import save_booking_inquiry
from core.ai.rag_engine import retrieve_context

logger = logging.getLogger(__name__)

PHONE_NUMBER = "+91 97274 23555"
WHATSAPP_NUMBER = "+91 96241 68555"
WHATSAPP_LINK = "https://wa.me/919624168555"

# Tour lookup configuration with priority keywords
TOUR_LOOKUP = [
    {
        "slug": "panch-kedar",
        "keywords": [
            "panch kedar", "panchkedar", "punch kedar", "punchkedar", "panch-kedar", "punch-kedar",
            "tungnath", "rudranath", "madhyamaheshwar", "kalpeshwar",
            "પંચ કેદાર", "પંચકેદાર", "તુંગનાથ", "રુદ્રનાથ", "पंच केदार", "पंचकेदार", "तुंगनाथ"
        ]
    },
    {
        "slug": "kashmir-paradise",
        "keywords": [
            "kashmir", "vaishno devi", "vaishnodevi", "katra", "gulmarg", "sonmarg", "pahalgam",
            "dal lake", "shikara", "srinagar",
            "કાશ્મીર", "વૈષ્ણોદેવી", "કટરા", "ગુલમર્ગ", "कश्मीर", "वैष्णो देवी", "कटरा", "गुलमर्ग"
        ]
    },
    {
        "slug": "jagannath-puri",
        "keywords": [
            "puri", "jagannath", "jagannath puri", "jagannathpuri", "konark", "bhubaneswar",
            "જગન્નાથ", "પુરી", "કોણાર્ક", "જગન્નાથપુરી", "जगन्नाथ", "पुरी", "कोणार्क"
        ]
    },
    {
        "slug": "nepal-pashupatinath-muktinath",
        "keywords": [
            "nepal", "pashupatinath", "muktinath", "pokhara", "kathmandu",
            "નેપાળ", "પશુપતિનાથ", "મુક્તિનાથ", "नेपाल", "पशुपतिनाथ", "मुक्तिनाथ"
        ]
    },
    {
        "slug": "rameshwaram-circuit",
        "keywords": [
            "rameshwaram", "rameswaram", "madurai", "kanyakumari", "dhanushkodi", "tiruchendur",
            "trivandrum", "padmanabhaswamy", "south india",
            "રામેશ્વરમ", "દક્ષિણ ભારત", "કન્યાકુમારી", "મદુરાઈ", "रामेश्वरम", "दक्षिण भारत", "कन्याकुमारी", "मदुरै"
        ]
    },
    {
        "slug": "kerala-tour",
        "keywords": [
            "kerala", "munnar", "thekkady", "alleppey", "kochi", "cochin",
            "કેરળ", "કેરાલા", "મુન્નાર", "केरल", "मुन्नार", "अल्लेप्पी"
        ]
    },
    {
        "slug": "jharkhand-tour",
        "keywords": [
            "jharkhand", "shikharji", "sammed shikharji", "parasnath",
            "ઝારખંડ", "શિખરજી", "સમ્મેદ શિખરજી", "झारखंड", "शिखरजी", "सम्मेद शिखरजी"
        ]
    },
    {
        "slug": "char-dham",
        "keywords": [
            "char dham", "chardham", "char-dham", "chardhaam", "chardam",
            "yamunotri", "gangotri", "badrinath", "kedarnath",
            "ચારધામ", "યમુનોત્રી", "ગંગોત્રી", "બદ્રીનાથ", "કેદારનાથ",
            "चारधाम", "यमुनोत्री", "गंगोत्री", "बद्रीनाथ", "केदारनाथ"
        ]
    }
]

MONTHS_MAP = {
    "december": ["december", "dec", "ડિસેમ્બર", "દિસેમ્બર", "दिसंबर"],
    "november": ["november", "nov", "નવેમ્બર", "नवंबर"],
    "may": ["may", "મે", "मई"],
    "june": ["june", "જૂન", "जून"],
    "october": ["october", "oct", "ઓક્ટોબર", "अक्टूबर"],
    "january": ["january", "jan", "જાન્યુઆરી", "जनवरी"],
    "february": ["february", "feb", "ફેબ્રુઆરી", "फरवरी"],
    "march": ["march", "mar", "માર્ચ", "मार्च"],
    "april": ["april", "apr", "એપ્રિલ", "अप्रैल"],
    "july": ["july", "જુલાઈ", "जुलाई"],
    "august": ["august", "aug", "ઓગસ્ટ", "अगस्त"],
    "september": ["september", "sep", "સપ્ટેમ્બર", "सितंबर"]
}


def _detect_language(text: str, requested_lang: Optional[str] = None) -> str:
    """Detect language of user message: gu_script, hi_script, gu_roman, hi_roman, or en."""
    # 1. Script checks take highest precedence
    if re.search(r'[\u0a80-\u0aff]', text):
        return "gu_script"
    if re.search(r'[\u0900-\u097f]', text):
        return "hi_script"

    # 2. If explicit language was requested by user clicking language pills
    if requested_lang:
        req_clean = requested_lang.lower().strip()
        if req_clean in ["gu", "gujarati", "gu_script"]:
            return "gu_script"
        elif req_clean in ["hi", "hindi", "hi_script"]:
            return "hi_script"
        elif req_clean in ["en", "english"]:
            return "en"

    # 3. Analyze words in Latin text
    words = set(re.findall(r'[a-zA-Z]+', text.lower()))

    # Unambiguous Gujarati Roman words (excluding English collisions like 'pan', 'ma', 'to')
    gu_distinct = {
        "tame", "tamare", "tamaro", "tamari", "chhe", "che", "nathi", "mate",
        "amaro", "amari", "amare", "aavse", "karvu", "joie", "joiye", "ketla", "ketlo",
        "janavo", "rahya", "chho", "kyare", "hase", "haju", "kem", "su", "shu", "aavi", "bhav"
    }

    # Unambiguous Hindi Roman words (excluding English collisions like 'me', 'he', 'par', 'hum', 'to', 'is', 'se')
    hi_distinct = {
        "kya", "kab", "kitna", "kitni", "kitne", "hai", "hoga", "hogi",
        "chahiye", "bataiye", "batao", "hume", "kaise", "milega", "milegi",
        "karega", "karenge", "rahega", "kripya", "dhanyawad", "konsi", "kaunsi",
        "mein", "kahan", "kaha", "bata", "aapka", "kare"
    }

    # Common English words (strictly English indicator words without Hindi/Gujarati grammar collisions)
    en_distinct = {
        "what", "which", "when", "where", "how", "who", "why", "is", "are", "the",
        "give", "tell", "show", "details", "contact", "phone", "number", "office",
        "address", "price", "cost", "dates", "date", "tour", "tours", "package",
        "packages", "yatra", "itinerary", "food", "meals", "meal", "hotels",
        "hotel", "room", "train", "tickets", "booking", "book", "provide",
        "available", "schedule", "please", "can", "you", "about", "next",
        "batch", "batches", "start", "starting", "from", "for", "with", "all"
    }

    gu_matches = len(words & gu_distinct)
    hi_matches = len(words & hi_distinct)

    if gu_matches > 0 and gu_matches >= hi_matches:
        return "gu_roman"
    if hi_matches > 0:
        return "hi_roman"
    return "en"


def _detect_month(query: str) -> Optional[str]:
    """Detect if user query mentions a specific month."""
    q_lower = query.lower()
    for month_key, synonyms in MONTHS_MAP.items():
        if any(re.search(r'\b' + re.escape(syn) + r'\b', q_lower) or syn in q_lower for syn in synonyms):
            return month_key
    return None


def _get_static_package(slug: str) -> Optional[Dict[str, Any]]:
    """Safely retrieve static package definition fallback from yatras.data."""
    try:
        if slug == "rameshwaram-circuit":
            from yatras.data.rameshwaram import RAMESHWARAM_PACKAGE
            return RAMESHWARAM_PACKAGE
        elif slug == "char-dham":
            from yatras.data.char_dham import CHAR_DHAM_PACKAGE
            return CHAR_DHAM_PACKAGE
        elif slug == "kashmir-paradise":
            from yatras.data.kashmir import KASHMIR_PACKAGE
            return KASHMIR_PACKAGE
        elif slug == "jagannath-puri":
            from yatras.data.puri_eastern import PURI_PACKAGE
            return PURI_PACKAGE
        elif slug == "kerala-tour":
            from yatras.data.kerala import KERALA_PACKAGE
            return KERALA_PACKAGE
    except Exception as exc:
        logger.debug("Static package import for %s skipped: %s", slug, exc)
    return None


def _find_tour_package(query: str):
    """Find matching TourPackage model instance or slug dictionary."""
    from yatras.models import TourPackage

    q_lower = query.lower().replace("-", " ")

    # Check Panch Kedar variations first
    if any(k in q_lower for k in [
        "punchkedar", "punch kedar", "punch-kedar", "panchkedar", "panch kedar", "panch-kedar",
        "tungnath", "rudranath", "madhyamaheshwar", "kalpeshwar", "પંચ કેદાર", "પંચકેદાર", "पंच केदार", "पंचकेदार"
    ]):
        tour = TourPackage.objects.filter(slug="panch-kedar").first()
        if tour:
            return tour, "panch-kedar"
        return None, "panch-kedar"

    # Match registered tour circuits in priority order
    for entry in TOUR_LOOKUP:
        for kw in entry["keywords"]:
            if kw in q_lower:
                tour = TourPackage.objects.filter(slug=entry["slug"]).first()
                return tour, entry["slug"]

    return None, None


def _get_tour_itinerary_summary(tour, slug: str, specific_day: Optional[int] = None, lang: str = "en") -> str:
    """Get concise day-by-day itinerary summary from DB or static data."""
    from yatras.models import ItineraryDay

    tour_name = tour.name if tour else slug.replace("-", " ").title()
    duration_display = tour.duration_display if tour else "Complete Tour"

    if tour:
        days_qs = ItineraryDay.objects.filter(tour=tour).order_by('day_number')
        if specific_day is not None:
            day = days_qs.filter(day_number=specific_day).first()
            if day:
                if lang in ["hi_roman", "hi_script"]:
                    return f"{tour_name} Day {day.day_number}: {day.starting_point} से {day.destination} ({day.title})। रात्रि विश्राम: {day.night_stay}। {day.intro}"
                elif lang in ["gu_roman", "gu_script"]:
                    return f"{tour_name} Day {day.day_number}: {day.starting_point} થી {day.destination} ({day.title}). રાત્રિ રોકાણ: {day.night_stay}. {day.intro}"
                return f"Day {day.day_number} of {tour_name}: {day.starting_point} to {day.destination} ({day.title}). Night stay at {day.night_stay}. {day.intro}"

        if days_qs.exists():
            if lang in ["hi_roman", "hi_script"]:
                lines = [f"{tour_name} का {duration_display} यात्रा मार्ग:"]
            elif lang in ["gu_roman", "gu_script"]:
                lines = [f"{tour_name} નો {duration_display} યાત્રા રૂટ:"]
            else:
                lines = [f"The {duration_display} itinerary of {tour_name}:"]

            for d in days_qs:
                lines.append(f"• Day {d.day_number}: {d.starting_point} to {d.destination} ({d.title})")
            return "\n".join(lines)

    # Fallback to static itinerary days for specific tours (like Rameshwaram)
    if slug == "rameshwaram-circuit":
        try:
            from yatras.data.rameshwaram import RAMESHWARAM_ITINERARY_DAYS
            if specific_day is not None and 1 <= specific_day <= len(RAMESHWARAM_ITINERARY_DAYS):
                d = RAMESHWARAM_ITINERARY_DAYS[specific_day - 1]
                return f"Day {specific_day} of Rameshwaram Tour: {d.get('title')}. Stay at {d.get('night_stay')}."
            lines = ["Rameshwaram & South Divine 12-Day Itinerary:"]
            for i, d in enumerate(RAMESHWARAM_ITINERARY_DAYS, 1):
                lines.append(f"• Day {i}: {d.get('title')} (Night: {d.get('night_stay')})")
            return "\n".join(lines)
        except Exception:
            pass

    return f"Detailed day-by-day itinerary for {tour_name} is available in our brochure. Please connect with our team on WhatsApp ({WHATSAPP_NUMBER}) to receive the complete PDF."


def _handle_month_query(month: str, lang: str) -> Dict[str, Any]:
    """Handle queries asking which tours/yatras are scheduled for a specific month."""
    month_cap = month.capitalize()

    if month == "december":
        if lang in ["hi_roman", "hi_script"]:
            reply = (
                f"**दिसंबर (December)** में स्वर्णाव टूर एंड ट्रेवल्स की मुख्य यात्राएं:\n\n"
                f"1. **कश्मीर टूर (Kashmir Paradise & Vaishno Devi)**: **दिसंबर 2026** में कन्फर्म विंटर बैच रवाना होगा (श्रीनगर, गुलमर्ग बर्फबारी/स्नो, पहलगाम, डल झील शिकारा और मां वैष्णो देवी दर्शन)।\n"
                f"2. **रामेश्वरम व दक्षिण भारत यात्रा (Rameshwaram Tour)**: दिसंबर में सूरत से **मंथली शेड्यूल ग्रुप प्रस्थान** उपलब्ध है।\n\n"
                f"दिसंबर बैच की सीट आरक्षण और तारीख की पुष्टि के लिए आप सीधे **{PHONE_NUMBER}** या WhatsApp (**{WHATSAPP_NUMBER}**) पर संपर्क कर सकते हैं।"
            )
        elif lang == "gu_script":
            reply = (
                f"**ડિસેમ્બર (December)** મહિનામાં સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સની મુખ્ય યાત્રાઓ:\n\n"
                f"૧. **કાશ્મીર અને વૈષ્ણોદેવી ટૂર**: **ડિસેમ્બર ૨૦૨૬** માં કન્ફર્મ વિન્ટર બેચ સુરતથી રવાના થશે (બરફબારી/સ્નો, ગુલમર્ગ, સોનમર્ગ, પહેલગામ અને વૈષ્ણોદેવી દર્શન).\n"
                f"૨. **રામેશ્વરમ અને દક્ષિણ ભારત યાત્રા**: ડિસેમ્બર માટે સુરતથી **દર મહિને નિયમિત ગ્રૂપ ટૂર** ઉપલબ્ધ છે.\n\n"
                f"ડિસેમ્બર બેચની સીટ બુકિંગ માટે આપ સીધા **{PHONE_NUMBER}** પર અથવા WhatsApp (**{WHATSAPP_NUMBER}**) દ્વારા સંપર્ક કરી શકો છો."
            )
        elif lang == "gu_roman":
            reply = (
                f"**December** mahina ma Swarnav Tour & Travels ni mukhya yatras:\n\n"
                f"1. **Kashmir Tour & Vaishno Devi**: **December 2026** ma confirmed winter snow batch ravaana thase (Gulmarg, Pahalgam, Dal Lake Shikara ane Vaishno Devi darshan).\n"
                f"2. **Rameshwaram & South Divine Tour**: December mate Surat thi **Monthly Scheduled Departures** available che.\n\n"
                f"December batch ma seat booking mate tame **{PHONE_NUMBER}** par call athva WhatsApp (**{WHATSAPP_NUMBER}**) kari shako cho."
            )
        else:
            reply = (
                f"Departures scheduled for **December**:\n\n"
                f"1. **Kashmir Tour (Paradise on Earth & Vaishno Devi)**: Confirmed winter batch in **December 2026** (snow season in Gulmarg, Sonmarg, Pahalgam, Dal Lake Shikara, and Katra Vaishno Devi).\n"
                f"2. **Rameshwaram & South Divine Tour**: **Monthly Scheduled Departures** leaving from Surat Railway Station in December.\n\n"
                f"To confirm seats or check specific calendar departure dates for December, connect directly with our coordination team at **{PHONE_NUMBER}** or via WhatsApp (**{WHATSAPP_NUMBER}**)."
            )
        return {
            "reply": reply,
            "suggested_questions": [
                "What is the Kashmir December tour package price?",
                "What is the date for Rameshwaram tour?",
                "Connect on WhatsApp"
            ]
        }

    elif month == "november":
        if lang in ["hi_roman", "hi_script"]:
            reply = (
                f"**नवंबर (November)** में हमारी मुख्य यात्राएं:\n\n"
                f"1. **चारधाम यात्रा (Char Dham Yatra)**: कन्फर्म बैच **1st Nov – 13th Nov** (यमुनोत्री, गंगोत्री, केदारनाथ, बद्रीनाथ)।\n"
                f"2. **जगन्नाथ पुरी व पूर्वी दिव्य यात्रा**: कन्फर्म बैच **November 2026** (पुरी, कोणार्क, गंगासागर, वाराणसी)।\n"
                f"3. **रामेश्वरम व दक्षिण भारत यात्रा**: सूरत से नवंबर में मंथली ग्रुप प्रस्थान उपलब्ध है।\n\n"
                f"सीट आरक्षण के लिए आप सीधे **{PHONE_NUMBER}** या WhatsApp (**{WHATSAPP_NUMBER}**) पर संपर्क कर सकते हैं।"
            )
        elif lang in ["gu_script", "gu_roman"]:
            reply = (
                f"**નવેમ્બર (November)** મહિનામાં સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સની યાત્રાઓ:\n\n"
                f"૧. **ચારધામ યાત્રા**: કન્ફર્મ બેચ **1st Nov – 13th Nov** (કેદારનાથ, બદ્રીનાથ, યમુનોત્રી, ગંગોત્રી).\n"
                f"૨. **જગન્નાથ પુરી અને પૂર્વીય યાત્રા**: કન્ફર્મ બેચ **November 2026** (પુરી, કોણાર્ક, વારાણસી).\n"
                f"૩. **રામેશ્વરમ અને દક્ષિણ ભારત યાત્રા**: સુરતથી નિયમિત મંથલી ગ્રૂપ પ્રસ્થાન ઉપલબ્ધ છે.\n\n"
                f"તાજી વિગતો માટે આપ **{PHONE_NUMBER}** પર સંપર્ક કરી શકો છો."
            )
        else:
            reply = (
                f"Departures scheduled for **November**:\n\n"
                f"1. **Char Dham Yatra**: Confirmed batch **1st Nov – 13th Nov** (Kedarnath, Badrinath, Yamunotri, Gangotri).\n"
                f"2. **Jagannath Puri & Eastern Divine**: Confirmed batch **November 2026** (Puri, Konark, Varanasi).\n"
                f"3. **Rameshwaram & South Divine Tour**: Monthly scheduled departures from Surat Railway Station.\n\n"
                f"For seat availability in November batches, connect with us at **{PHONE_NUMBER}**."
            )
        return {
            "reply": reply,
            "suggested_questions": [
                "What is the Char Dham package price?",
                "What is the date for Rameshwaram tour?",
                "Connect on WhatsApp"
            ]
        }

    elif month in ["may", "june"]:
        if lang in ["hi_roman", "hi_script"]:
            reply = (
                f"**मई/जून (Summer Season)** में हमारी मुख्य यात्राएं:\n\n"
                f"1. **नेपाल पशुपतिनाथ व मुक्तिनाथ यात्रा**: कन्फर्म बैच **May 2027**।\n"
                f"2. **चारधाम यात्रा व पंच केदार**: कपाट खुलने पर मई-जून में समर स्पेशल बैच संचालित होते हैं।\n"
                f"3. **रामेश्वरम व दक्षिण भारत यात्रा**: हर महीने नियमित ग्रुप प्रस्थान उपलब्ध रहते हैं।\n\n"
                f"अधिक जानकारी के लिए **{PHONE_NUMBER}** पर संपर्क करें।"
            )
        else:
            reply = (
                f"Departures for **May / June (Summer Season)**:\n\n"
                f"1. **Nepal Pashupatinath & Muktinath Holy Yatra**: Confirmed batch in **May 2027**.\n"
                f"2. **Char Dham Yatra & Panch Kedar**: Sacred summer opening batches.\n"
                f"3. **Rameshwaram & South Divine Tour**: Regular monthly departures from Surat.\n\n"
                f"For summer booking inquiries, contact us at **{PHONE_NUMBER}**."
            )
        return {
            "reply": reply,
            "suggested_questions": [
                "What is the Nepal tour package price?",
                "What is the Char Dham tour itinerary?",
                "Connect on WhatsApp"
            ]
        }

    # Other months
    if lang in ["hi_roman", "hi_script"]:
        reply = (
            f"**{month_cap}** के लिए:\n\n"
            f"• **रामेश्वरम व दक्षिण भारत यात्रा** के लिए सूरत से **प्रतिमाह नियमित ग्रुप टूर (Monthly Scheduled Departures)** आयोजित किए जाते हैं।\n"
            f"• किसी भी महीने में परिवार या ग्रुप के लिए कस्टमाइज्ड स्पेशल पैकेज भी तैयार किए जाते हैं।\n\n"
            f"{month_cap} में कन्फर्म तारीख व सीट उपलब्धता के लिए आप सीधे **{PHONE_NUMBER}** या WhatsApp (**{WHATSAPP_NUMBER}**) पर संपर्क कर सकते हैं।"
        )
    elif lang in ["gu_script", "gu_roman"]:
        reply = (
            f"**{month_cap}** મહિના માટે:\n\n"
            f"• **રામેશ્વરમ અને દક્ષિણ ભારત યાત્રા** માટે સુરતથી **દર મહિને નિયમિત ગ્રૂપ ટૂર (Monthly Departures)** ઉપલબ્ધ છે.\n"
            f"• કોઈપણ મહિનામાં ફેમિલી કે સીનિયર સિટીઝન ગ્રૂપ માટે કસ્ટમ પ્રવાસ પણ આયોજિત કરી શકાય છે.\n\n"
            f"{month_cap} માં સીટ ઉપલબ્ધતા માટે આપ સીધા **{PHONE_NUMBER}** પર સંપર્ક કરી શકો છો."
        )
    else:
        reply = (
            f"For **{month_cap}**:\n\n"
            f"• **Rameshwaram & South Divine Tour** offers **Monthly Scheduled Departures** leaving every month from Surat Railway Station.\n"
            f"• Customized family packages and senior citizen group departures can be arranged in any calendar month.\n\n"
            f"To check exact dates for {month_cap}, please connect with our coordinator at **{PHONE_NUMBER}** or via WhatsApp (**{WHATSAPP_NUMBER}**)."
        )
    return {
        "reply": reply,
        "suggested_questions": [
            "What is the date for Rameshwaram tour?",
            "What is the price of Kashmir tour?",
            "Connect on WhatsApp"
        ]
    }


def _handle_tour_list_query(lang: str) -> Dict[str, Any]:
    """Handle queries asking what tours/yatras Swarnav provides/offers."""
    if lang in ["hi_roman", "hi_script"]:
        reply = (
            f"**स्वर्णाव टूर एंड ट्रेवल्स (Swarnav Tour & Travels)** मुख्य रूप से इन 8 पवित्र यात्राओं व टूर पैकेजों का संचालन करता है:\n\n"
            f"1. **चारधाम यात्रा (Char Dham Yatra)** - 13 दिन (यमुनोत्री, गंगोत्री, केदारनाथ, बद्रीनाथ)\n"
            f"2. **रामेश्वरम व दक्षिण भारत यात्रा (Rameshwaram & South Divine)** - 12 दिन (मदुरै, रामेश्वरम, धनुષકોડી, कन्याकुमारी, त्रिवेंद्रम)\n"
            f"3. **कश्मीर व वैष्णो देवी टूर (Kashmir & Vaishno Devi)** - 8-11 दिन (श्रीनगर, गुलमर्ग, सोनमर्ग, पहलगाम, कटरा)\n"
            f"4. **जगन्नाथ पुरी व पूर्वी दिव्य यात्रा (Jagannath Puri & Eastern Divine)** - 11 दिन (पुरी, कोणार्क, गंगासागर, वाराणसी)\n"
            f"5. **पंच केदार यात्रा (Panch Kedar Yatra)** - 16 दिन (केदारनाथ, तुंगनाथ, रुद्रनाथ, मध्यमहेश्वर, कल्पेश्वर)\n"
            f"6. **नेपाल पशुपतिनाथ व मुक्तिनाथ यात्रा (Nepal Holy Yatra)** (काठमांडू, पोखरा, पशुपतिनाथ)\n"
            f"7. **केरल टूर (Kerala Tour - God’s Own Country)** - 8 दिन (मुन्नार, थेक्कडी, अल्लेप्पी)\n"
            f"8. **झारखंड सम्मेद शिखरजी यात्रा (Jharkhand Yatra)**\n\n"
            f"✨ **विशेषताएं**: सभी यात्राएं **सूरत रेलवे स्टेशन (गुजरात)** से कन्फर्म AC ट्रेन टिकट, होटल आवास और शुद्ध सात्विक भोजन के साथ शुरू होती हैं।\n\n"
            f"आप किस यात्रा की तारीख या पैकेज मूल्य जानना चाहते हैं?"
        )
    elif lang == "gu_script":
        reply = (
            f"**સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સ (Swarnav Tour & Travels)** મુખ્યત્વે આ ૮ પવિત્ર યાત્રાઓ અને ટૂર પેકેજનું આયોજન કરે છે:\n\n"
            f"૧. **ચારધામ યાત્રા (Char Dham Yatra)** - ૧૩ દિવસ (યમુનોત્રી, ગંગોત્રી, કેદારનાથ, બદ્રીનાથ)\n"
            f"૨. **રામેશ્વરમ અને દક્ષિણ ભારત યાત્રા (Rameshwaram & South Divine)** - ૧૨ દિવસ (મદુરાઈ, રામેશ્વરમ, ધનુષકોડી, કન્યાકુમારી, ત્રિવેન્દ્રમ)\n"
            f"૩. **કાશ્મીર અને વૈષ્ણોદેવી ટૂર (Kashmir & Vaishno Devi)** - ૮-૧૧ દિવસ (શ્રીનગર, ગુલમર્ગ, સોનમર્ગ, પહેલગામ, કટરા)\n"
            f"૪. **જગન્નાથ પુરી અને પૂર્વીય યાત્રા (Jagannath Puri & Eastern Divine)** - ૧૧ દિવસ (પુરી, કોણાર્ક, ગંગાસાગર, વારાણસી)\n"
            f"૫. **પંચ કેદાર યાત્રા (Panch Kedar Yatra)** - ૧૬ દિવસ (તુંગનાથ, રુદ્રનાથ, મધ્યમહેશ્વર, કલ્પેશ્વર, કેદારનાથ)\n"
            f"૬. **નેપાળ પશુપતિનાથ અને મુક્તિનાથ યાત્રા (Nepal Holy Yatra)**\n"
            f"૭. **કેરળ ટૂર (Kerala Tour - God’s Own Country)** - ૮ દિવસ (મુન્નાર, થેક્કડી, એલેપ્પી)\n"
            f"૮. **ઝારખંડ સમ્મેદ શિખરજી યાત્રા (Jharkhand Yatra)**\n\n"
            f"✨ **મુખ્ય સુવિધાઓ**: સુરત રેલવે સ્ટેશનથી કન્ફર્મ AC ટ્રેન ટિકિટ, હોટેલ રોકાણ અને દૈનિક શુદ્ધ સાત્વિક ભોજન સામેલ છે.\n\n"
            f"આપ કઈ યાત્રાની તારીખ અથવા પેકેજ ભાવ જાણવા માંગો છો?"
        )
    elif lang == "gu_roman":
        reply = (
            f"**Swarnav Tour & Travels** mukhyatve aa 8 pavitra yatras organize kare che:\n\n"
            f"1. **Char Dham Yatra** - 13 Divas (Yamunotri, Gangotri, Kedarnath, Badrinath)\n"
            f"2. **Rameshwaram & South Divine** - 12 Divas (Madurai, Rameshwaram, Dhanushkodi, Kanyakumari, Trivandrum)\n"
            f"3. **Kashmir & Vaishno Devi** - 8-11 Divas (Srinagar, Gulmarg, Pahalgam, Katra)\n"
            f"4. **Jagannath Puri & Eastern Divine** - 11 Divas (Puri, Konark, Gangasagar, Varanasi)\n"
            f"5. **Panch Kedar Yatra** - 16 Divas\n"
            f"6. **Nepal Pashupatinath & Muktinath**\n"
            f"7. **Kerala Tour** - 8 Divas (Munnar, Thekkady, Alleppey)\n"
            f"8. **Jharkhand Sammed Shikharji Yatra**\n\n"
            f"Badhi j yatras **Surat Railway Station** thi confirmed AC train tickets, hotel rokan ane shuddh Satvik bhojan sathe aayojit thay che. Tame kai yatra vishe janva mango cho?"
        )
    else:
        reply = (
            f"**Swarnav Tour & Travels** offers personalized, all-inclusive pilgrimage and tour packages across India:\n\n"
            f"1. **Char Dham Yatra** (13 Days - Yamunotri, Gangotri, Kedarnath, Badrinath)\n"
            f"2. **Rameshwaram & South Divine Tour** (12 Days - Madurai, Rameshwaram, Dhanushkodi, Kanyakumari, Trivandrum)\n"
            f"3. **Kashmir Tour & Vaishno Devi** (8–11 Days - Srinagar, Gulmarg, Sonmarg, Pahalgam, Katra)\n"
            f"4. **Jagannath Puri & Eastern Divine Pilgrimage** (11 Days - Puri, Konark, Gangasagar, Varanasi)\n"
            f"5. **Panch Kedar Yatra** (16 Days - Tungnath, Rudranath, Madhyamaheshwar, Kalpeshwar, Kedarnath)\n"
            f"6. **Nepal Pashupatinath & Muktinath Holy Yatra**\n"
            f"7. **Kerala Tour (God’s Own Country)** (8 Days - Munnar, Thekkady, Alleppey)\n"
            f"8. **Jharkhand Spiritual Yatra (Sammed Shikharji)**\n\n"
            f"✨ **Package Inclusions**: Round-trip confirmed AC train travel from Surat Railway Station, hotel accommodations, pure Satvik meals, and guided darshan.\n\n"
            f"Which yatra or dates would you like more information about?"
        )
    return {
        "reply": reply,
        "suggested_questions": [
            "What is the date for Char Dham tour?",
            "What is the date for Rameshwaram tour?",
            "What is the package price of Kashmir tour?"
        ]
    }


def _handle_contact_query(lang: str, tour_name: Optional[str] = None) -> Dict[str, Any]:
    """Handle queries asking for contact details, phone number, WhatsApp, office address, or email."""
    tour_prefix = f"for **{tour_name}** and all yatras" if tour_name else "for inquiries and bookings"
    tour_prefix_gu = f"**{tour_name}** સહિત તમામ યાત્રાઓ માટે" if tour_name else "પૂછપરછ અને સીટ બુકિંગ માટે"
    tour_prefix_hi = f"**{tour_name}** सहित सभी यात्राओं के लिए" if tour_name else "पूछताछ एवं सीट आरक्षण के लिए"

    if lang == "gu_script":
        reply = (
            f"**સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સ — સંપર્ક વિગતો** ({tour_prefix_gu}):\n\n"
            f"📞 **ફોન / કૉલ**: **{PHONE_NUMBER}**\n"
            f"💬 **WhatsApp**: **{WHATSAPP_NUMBER}** ([WhatsApp પર ચેટ કરો]({WHATSAPP_LINK}))\n"
            f"📧 **ઈમેલ**: swarnavtours01@gmail.com\n"
            f"🏢 **મુખ્ય કાર્યાલય (Office)**: રિંગ રોડ, સુરત, ગુજરાત - 395002\n"
            f"⏰ **ઓફિસ સમય**: સવારે 7:00 થી રાત્રે 9:30 (દરરોજ)\n"
            f"🚆 **પ્રસ્થાન કેન્દ્ર**: સુરત રેલવે સ્ટેશન, ગુજરાત\n\n"
            f"કોઈપણ યાત્રાના બુકિંગ અથવા તાજી વિગતો માટે આપ સીધા અમારા વરિષ્ઠ કો-ઓર્ડિનેટરનો સંપર્ક કરી શકો છો."
        )
    elif lang in ["hi_roman", "hi_script"]:
        reply = (
            f"**स्वर्णाव टूर एंड ट्रेवल्स — संपर्क सूत्र (Contact Details)** ({tour_prefix_hi}):\n\n"
            f"📞 **फ़ोन / कॉल**: **{PHONE_NUMBER}**\n"
            f"💬 **WhatsApp**: **{WHATSAPP_NUMBER}** ([WhatsApp पर चैट करें]({WHATSAPP_LINK}))\n"
            f"📧 **ईमेल**: swarnavtours01@gmail.com\n"
            f"🏢 **कार्यालय (Office)**: रिंग रोड, सूरत, गुजरात - 395002\n"
            f"⏰ **कार्य समय**: प्रतिदिन सुबह 7:00 से रात 9:30 तक\n"
            f"🚆 **प्रस्थान केंद्र**: सूरत रेलवे स्टेशन, गुजरात\n\n"
            f"सीट आरक्षण या किसी भी यात्रा की विस्तृत जानकारी के लिए आप सीधे हमारे वरिष्ठ को-ऑर्डिनेटर से संपर्क कर सकते हैं।"
        )
    elif lang == "gu_roman":
        reply = (
            f"**Swarnav Tour & Travels — Contact Details** ({tour_prefix}):\n\n"
            f"📞 **Phone / Call**: **{PHONE_NUMBER}**\n"
            f"💬 **WhatsApp**: **{WHATSAPP_NUMBER}** ([Chat on WhatsApp]({WHATSAPP_LINK}))\n"
            f"📧 **Email**: swarnavtours01@gmail.com\n"
            f"🏢 **Head Office**: Ring Road, Surat, Gujarat - 395002\n"
            f"⏰ **Timings**: Daily 7:00 AM – 9:30 PM (IST)\n"
            f"🚆 **Departure Station**: Surat Railway Station, Gujarat\n\n"
            f"Yatra booking ane mahiti mate tame sidha amara tour coordinator sathe contact kari shako cho."
        )
    else:
        reply = (
            f"**Swarnav Tour & Travels — Official Contact Details** ({tour_prefix}):\n\n"
            f"📞 **Phone / Call**: **{PHONE_NUMBER}**\n"
            f"💬 **WhatsApp**: **{WHATSAPP_NUMBER}** ([Chat directly on WhatsApp]({WHATSAPP_LINK}))\n"
            f"📧 **Email**: swarnavtours01@gmail.com\n"
            f"🏢 **Head Office**: Ring Road, Surat, Gujarat - 395002\n"
            f"⏰ **Operating Hours**: Daily 7:00 AM – 9:30 PM (IST)\n"
            f"🚆 **Departure Hub**: Surat Railway Station, Gujarat\n\n"
            f"Our senior tour coordinators are available daily to assist with customized family packages, departure dates, and reservations."
        )

    return {
        "reply": reply,
        "suggested_questions": [
            "Which tours do you provide?",
            "What is the date for Char Dham tour?",
            "What is the date for Rameshwaram tour?"
        ]
    }


def _handle_greeting_query(lang: str) -> Dict[str, Any]:
    """Handle conversational greetings politely and guide user to key questions."""
    if lang == "gu_script":
        reply = (
            f"નમસ્તે! 🙏 **સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સ** માં આપનું હાર્દિક સ્વાગત છે.\n\n"
            f"હું આપને આ તમામ વિગતોમાં મદદ કરી શકું છું:\n"
            f"• **યાત્રાની આગામી કન્ફર્મ તારીખો** (ચારધામ, કાશ્મીર, રામેશ્વરમ, જગન્નાથ પુરી, નેપાળ, કેરળ)\n"
            f"• **પેકેજ ભાવ અને સુવિધાઓ** (સુરતથી કન્ફર્મ AC ટ્રેન, શુદ્ધ સાત્વિક ભોજન, હોટેલ રોકાણ)\n"
            f"• **દિવસ મુજબ યાત્રા પ્લાન (રૂટ અને દર્શન)**\n"
            f"• **સીટ બુકિંગ અને કો-ઓર્ડિનેટર સહાય** (**{PHONE_NUMBER}**)\n\n"
            f"આપ કઈ યાત્રા અથવા વિષય વિશે માહિતી મેળવવા માંગો છો?"
        )
    elif lang in ["hi_roman", "hi_script"]:
        reply = (
            f"नमस्ते! 🙏 **स्वर्णाव टूर एंड ट्रेवल्स** में आपका हार्दिक स्वागत है।\n\n"
            f"मैं आपकी इन विषयों में तुरंत सहायता कर सकता हूँ:\n"
            f"• **आगामी यात्राओं की कन्फर्म तारीखें** (चारधाम, कश्मीर, रामेश्वरम, जगन्नाथ पुरी, नेपाल, केरल)\n"
            f"• **पैकेज दरें एवं सुविधाएं** (सूरत से AC ट्रेन, सात्विक भोजन, होटल आवास)\n"
            f"• **दिवसवार यात्रा मार्ग एवं दर्शन विवरण**\n"
            f"• **सीट बुकिंग एवं सहायता** (**{PHONE_NUMBER}**)\n\n"
            f"आप किस पावन तीर्थ यात्रा के बारे में जानना चाहते हैं?"
        )
    elif lang == "gu_roman":
        reply = (
            f"Namaste! 🙏 **Swarnav Tour & Travels** ma aapnu swagat che.\n\n"
            f"Hu tamne yatra dates, package price, itinerary ane booking ma help kari shaku chu.\n"
            f"Tame kai yatra (Char Dham, Rameshwaram, Kashmir, Jagannath Puri) vishe janva mango cho?"
        )
    else:
        reply = (
            f"Namaste! 🙏 Welcome to **Swarnav Tour & Travels**.\n\n"
            f"I can assist you with:\n"
            f"• **Upcoming Departure Dates** (Char Dham, Kashmir, Rameshwaram, Jagannath Puri, Nepal, Kerala)\n"
            f"• **All-Inclusive Package Pricing** (Confirmed AC Train from Surat, Satvik Meals, Hotels)\n"
            f"• **Day-by-Day Route & Darshan Itineraries**\n"
            f"• **Direct Booking & Coordinator Support** (**{PHONE_NUMBER}**)\n\n"
            f"Which pilgrimage or destination would you like to explore today?"
        )

    return {
        "reply": reply,
        "suggested_questions": [
            "Which tours do you provide?",
            "What is the date for Char Dham tour?",
            "What is the date for Rameshwaram tour?"
        ]
    }


def _handle_booking_process_query(lang: str) -> Dict[str, Any]:
    """Handle queries asking how to book, registration steps, or reservation process."""
    if lang == "gu_script":
        reply = (
            f"**સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સમાં યાત્રા બુક કરવાની સરળ પ્રક્રિયા**:\n\n"
            f"૧. **યાત્રા અને તારીખ પસંદ કરો**: આપની મનપસંદ યાત્રા (ચારધામ, રામેશ્વરમ, કાશ્મીર, જગન્નાથ પુરી વગેરે) પસંદ કરો.\n"
            f"૨. **કો-ઓર્ડિનેટરનો સંપર્ક કરો**: અમારા વરિષ્ઠ કો-ઓર્ડિનેટર સાથે **{PHONE_NUMBER}** પર કૉલ અથવા WhatsApp (**{WHATSAPP_NUMBER}**) દ્વારા સીધી વાત કરો.\n"
            f"૩. **ટોકન એડવાન્સ**: યાત્રીઓના નામ આપીને કન્ફર્મ AC ટ્રેન બર્થ અને હોટેલ રૂમ સુરક્ષિત કરવા માટે ટોકન એડવાન્સ જમા કરાવો.\n"
            f"૪. **ચેટમાં નંબર આપો**: આપ આ ચેટમાં આપનો ૧૦-અંકનો મોબાઈલ નંબર પણ લખી શકો છો, અમારી ટીમ તુરંત આપનો સંપર્ક કરશે."
        )
    elif lang in ["hi_roman", "hi_script"]:
        reply = (
            f"**स्वर्णाव टूर एंड ट्रेवल्स में बुकिंग की सरल प्रक्रिया**:\n\n"
            f"1. **यात्रा और तारीख चुनें**: अपनी पसंद की तीर्थ यात्रा (चारधाम, रामेश्वरम, कश्मीर, जगन्नाथ पुरी आदि) का चयन करें।\n"
            f"2. **हमसे संपर्क करें**: हमारे वरिष्ठ को-ऑर्डिनेटर को सीधे **{PHONE_NUMBER}** पर कॉल या WhatsApp (**{WHATSAPP_NUMBER}**) करें।\n"
            f"3. **टोकन एडवांस**: तीर्थयात्रियों के नाम दर्ज कराकर कन्फर्म AC ट्रेन सीट और होटल रिजर्व करने हेतु टोकन जमा करें।\n"
            f"4. **चैट में नंबर छोड़ें**: आप इस चैट में अपना 10-अंकों का मोबाइल नंबर भी लिख सकते हैं, हमारी टीम तुरंत कॉल करेगी।"
        )
    else:
        reply = (
            f"**How to Book Your Pilgrimage with Swarnav Tour & Travels**:\n\n"
            f"1. **Select Tour & Dates**: Choose your desired pilgrimage (e.g., Char Dham, Rameshwaram, Kashmir, Jagannath Puri).\n"
            f"2. **Connect with Us**: Call our senior coordinator at **{PHONE_NUMBER}** or WhatsApp **{WHATSAPP_NUMBER}** ([Chat on WhatsApp]({WHATSAPP_LINK})).\n"
            f"3. **Token Booking**: Submit pilgrim names and an advance token to secure your confirmed AC railway berths and hotel rooms.\n"
            f"4. **Instant Callback**: You can also enter your 10-digit mobile number in this chat, and our coordinator will call you back promptly."
        )

    return {
        "reply": reply,
        "suggested_questions": [
            "Which tours do you provide?",
            "What is the date for Char Dham tour?",
            "Connect on WhatsApp"
        ]
    }


def _handle_inclusions_query(lang: str) -> Dict[str, Any]:
    """Handle queries asking what is included / facilities provided across packages."""
    if lang == "gu_script":
        reply = (
            f"**સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સની તમામ યાત્રાઓમાં સામેલ મુખ્ય સુવિધાઓ**:\n\n"
            f"🚆 **ટ્રેન મુસાફરી**: સુરત રેલવે સ્ટેશનથી રાઉન્ડ-ટ્રીપ કન્ફર્મ ૩-ટાયર AC ટ્રેન ટિકિટ.\n"
            f"🏨 **હોટેલ રોકાણ**: મંદિરોની નજીક સ્વચ્છ અને સુરક્ષિત હોટેલ રૂમ્સ (ડબલ/ટ્રિપલ શેરિંગ).\n"
            f"🍲 **શુદ્ધ સાત્વિક ભોજન**: દૈનિક તાજું બનાવેલું શુદ્ધ શાકાહારી ભોજન (કાંદા-લસણ વગરનું જૈન ભોજન ઉપલબ્ધ).\n"
            f"🚌 **સ્થાનિક મુસાફરી**: તમામ દર્શન અને સાઇટસીઇંગ માટે ડેડિકેટેડ AC વાહન/બસ.\n"
            f"🙏 **દર્શન સહાય**: સ્થળ પર હાજર રહેતા અનુભવી ટૂર મેનેજર અને વડીલો માટે વિશેષ સહાય."
        )
    elif lang in ["hi_roman", "hi_script"]:
        reply = (
            f"**स्वर्णाव टूर एंड ट्रेवल्स के सभी पैकेजों में शामिल प्रमुख सुविधाएं**:\n\n"
            f"🚆 **ट्रेन यात्रा**: सूरत रेलवे स्टेशन से राउंड-ट्रिप कन्फर्म 3-Tier AC ट्रेन टिकट।\n"
            f"🏨 **होटल व्यवस्था**: प्रमुख मंदिरों के निकट स्वच्छ, आरामदायक होटल आवास (डबल/ट्रिपल शेयरिंग)।\n"
            f"🍲 **शुद्ध सात्विक भोजन**: प्रतिदिन शुद्ध शाकाहारी सात्विक दोपहर व रात का भोजन (जैन भोजन उपलब्ध)।\n"
            f"🚌 **स्थानीय परिवहन**: दर्शन व स्थानीय भ्रमण के लिए समर्पित AC बस/ट्रेवलर।\n"
            f"🙏 **दर्शन एवं वरिष्ठ सहायता**: ऑन-ग्राउंड टूर मैनेजर, मंदिर दर्शन में मार्गदर्शन और बुजुर्गों की सेवा।"
        )
    else:
        reply = (
            f"**Standard Package Inclusions across all Swarnav Tours**:\n\n"
            f"🚆 **Train Travel**: Round-trip confirmed 3-Tier AC train tickets starting & ending at Surat Railway Station.\n"
            f"🏨 **Hotel Accommodations**: Sanitized, comfortable hotel stays (double/triple sharing) near pilgrimage shrines.\n"
            f"🍲 **Pure Satvik Meals**: Freshly prepared pure vegetarian lunch & dinner daily (special Jain food without onion/garlic on advance notice).\n"
            f"🚌 **Local Transportation**: Dedicated AC coaches / Tempo Travellers for all sightseeing and temple transits.\n"
            f"🙏 **Darshan Assistance**: Dedicated on-ground tour managers for smooth temple queues and senior citizen assistance.\n\n"
            f"For package pricing of a specific tour, ask (e.g. *What is the price of Char Dham?*)."
        )

    return {
        "reply": reply,
        "suggested_questions": [
            "Which tours do you provide?",
            "What is the price of Char Dham?",
            "What is the date for Rameshwaram tour?"
        ]
    }


def _handle_hotel_query(lang: str) -> Dict[str, Any]:
    """Handle queries asking about hotels, room accommodations, or room sharing."""
    if lang == "gu_script":
        reply = (
            f"**હોટેલ અને રોકાણ વ્યવસ્થા (Hotel & Accommodation)**:\n\n"
            f"સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સની તમામ યાત્રાઓમાં મંદિરોની નજીક આવેલા શ્રેષ્ઠ અને સ્વચ્છ હોટેલોમાં રોકાણ કરાવવામાં આવે છે.\n\n"
            f"• **રૂમ સુવિધા**: AC રૂમ્સ, સ્વચ્છ બેડિંગ અને અટેચ્ડ બાથરૂમ સાથે ૨૪ કલાક ગરમ પાણીની સુવિધા.\n"
            f"• **શેરિંગ**: સામાન્ય રીતે ટ્રિપલ (૩ વ્યક્તિ) શેરિંગ અથવા ફેમિલી ડબલ શેરિંગ ઉપલબ્ધ છે."
        )
    elif lang in ["hi_roman", "hi_script"]:
        reply = (
            f"**होटल एवं आवास व्यवस्था (Hotel & Stay)**:\n\n"
            f"स्वर्णाव टूर एंड ट्रेवल्स की सभी यात्राओं में मुख्य मंदिरों के पास स्थित स्वच्छ, सुरक्षित व आरामदायक होटलों में रुकने की व्यवस्था होती है।\n\n"
            f"• **कमरे की सुविधाएं**: AC कमरे, स्वच्छ बिस्तर, अटैच्ड वेस्टर्न/इंडियन बाथरूम और 24 घंटे गर्म पानी की सुविधा।\n"
            f"• **कमरा शेयरिंग**: मानक पैकेज में ट्रिपल (3 व्यक्ति) या डबल शेयरिंग विकल्प उपलब्ध हैं।"
        )
    else:
        reply = (
            f"**Hotel & Accommodation Standards**:\n\n"
            f"Across all Swarnav pilgrimage tours, accommodations are arranged in pre-inspected, clean, and family-friendly hotels located close to major temples.\n\n"
            f"• **Room Amenities**: AC rooms with sanitized bedding, attached bathrooms, and round-the-clock hot water.\n"
            f"• **Sharing**: Standard packages are based on triple sharing, with double sharing upgrades available upon request."
        )

    return {
        "reply": reply,
        "suggested_questions": [
            "What is the price of Char Dham?",
            "What is the date for Rameshwaram tour?",
            "Connect on WhatsApp"
        ]
    }


def _handle_cancellation_query(lang: str) -> Dict[str, Any]:
    """Handle queries asking about cancellation, refund, or reschedule policy."""
    if lang == "gu_script":
        reply = (
            f"**કેન્સલેશન અને રીફંડ પોલિસી (Cancellation & Refund Policy)**:\n\n"
            f"યાત્રા રદ્દ કરવા અથવા તારીખ બદલવા અંગેની વિગતો માટે આપ સીધા અમારા વરિષ્ઠ કો-ઓર્ડિનેટરનો **{PHONE_NUMBER}** પર સંપર્ક કરી શકો છો.\n\n"
            f"ટ્રેન ટિકિટ કેન્સલેશન IRCTC ના નિયમો અનુસાર થાય છે અને હોટેલ એડવાન્સ બાબતે અમારી ટીમ સંપૂર્ણ સહયોગ પૂરો પાડે છે."
        )
    elif lang in ["hi_roman", "hi_script"]:
        reply = (
            f"**रद्दीकरण एवं रिफंड नीति (Cancellation & Refund Policy)**:\n\n"
            f"यात्रा रद्द करने या तारीख में बदलाव से संबंधित नियमों के लिए आप सीधे हमारे मुख्य को-ऑर्डिनेटर से **{PHONE_NUMBER}** पर संपर्क कर सकते हैं।\n\n"
            f"ट्रेन टिकट रद्दीकरण भारतीय रेलवे (IRCTC) के नियमों के अनुसार होता है तथा होटल कैंसलेशन में हमारी टीम हरसंभव सहयोग करती है।"
        )
    else:
        reply = (
            f"**Cancellation & Reschedule Policy**:\n\n"
            f"For cancellation requests, refunds, or date rescheduling, please reach out directly to our senior coordination team at **{PHONE_NUMBER}**.\n\n"
            f"Railway ticket cancellations adhere to official IRCTC cancellation rules, and our ground team coordinates flexible adjustments whenever possible."
        )

    return {
        "reply": reply,
        "suggested_questions": [
            "Which tours do you provide?",
            "What is the date for Char Dham tour?",
            "Connect on WhatsApp"
        ]
    }


def _handle_general_fallback(lang: str) -> Dict[str, Any]:
    """Graceful fallback when query is not recognized, guiding user rather than dumping 8 tours."""
    if lang == "gu_script":
        reply = (
            f"સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સ આપને યાત્રાઓની કન્ફર્મ તારીખો, પેકેજ ભાવ, રૂટ, શુદ્ધ સાત્વિક ભોજન અને સિનિયર સિટીઝન સુવિધાઓ વિશે સંપૂર્ણ માહિતી આપે છે.\n\n"
            f"આપ કઈ યાત્રા વિશે જાણવા માંગો છો (દા.ત. **ચારધામ, રામેશ્વરમ, કાશ્મીર, જગન્નાથ પુરી, નેપાળ, કેરળ કે પંચ કેદાર**)?\n\n"
            f"વધુ માહિતી અથવા સીટ બુકિંગ માટે આપ સીધા અમારા વરિષ્ઠ કો-ઓર્ડિનેટરનો **{PHONE_NUMBER}** પર અથવા WhatsApp (**{WHATSAPP_NUMBER}**) દ્વારા સંપર્ક કરી શકો છો."
        )
    elif lang in ["hi_roman", "hi_script"]:
        reply = (
            f"स्वर्णाव टूर एंड ट्रेवल्स की सभी पवित्र तीर्थ यात्राओं की तारीख, पैकेज दर, यात्रा मार्ग, सात्विक भोजन और बुकिंग की पूरी जानकारी उपलब्ध है।\n\n"
            f"कृपया बताएं कि आप किस यात्रा के बारे में जानकारी चाहते हैं (जैसे **चारधाम, रामेश्वरम, कश्मीर, जगन्नाथ पुरी, नेपाल, केरल या पंच केदार**)?\n\n"
            f"आप सीधे हमारे मुख्य को-ऑर्डिनेटर से **{PHONE_NUMBER}** पर या WhatsApp (**{WHATSAPP_NUMBER}**) द्वारा संपर्क कर सकते हैं।"
        )
    else:
        reply = (
            f"I am here to assist you with all details regarding Swarnav Tour & Travels pilgrimage packages, "
            f"including confirmed departure dates, package pricing, itineraries, Satvik food, hotel stays, and booking procedures.\n\n"
            f"Could you please specify which yatra you are interested in (e.g. **Char Dham, Rameshwaram, Kashmir, Jagannath Puri, Nepal, Kerala, Panch Kedar**)?\n\n"
            f"You can also contact our senior coordinator directly at **{PHONE_NUMBER}** (Call) or **{WHATSAPP_NUMBER}** (WhatsApp)."
        )

    return {
        "reply": reply,
        "suggested_questions": [
            "Which tours do you provide?",
            "What is the date for Char Dham tour?",
            "What is the date for Rameshwaram tour?"
        ]
    }


def _generate_precise_response(query: str, requested_lang: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate direct, verified answers based on live DB facts, static package data,
    month schedule lookup, and RAG knowledge base.
    """
    lang = _detect_language(query, requested_lang=requested_lang)
    q_lower = query.lower().strip()

    # 1. Lead Capture Intent (User provided phone number)
    phone_match = re.search(r'(\+?\d{10,13})', query)
    if ("book" in q_lower or "call" in q_lower or "contact" in q_lower or "mobile" in q_lower or "phone" in q_lower or "નંબર" in query or "ફોન" in query or "फोन" in query) and phone_match:
        digits = phone_match.group(1)
        name_guess = "Devotee"
        for word in query.split():
            clean_w = word.strip(".,;:!?")
            if clean_w.isalpha() and clean_w.lower() not in ["my", "name", "is", "please", "call", "book", "tour", "yatra", "phone", "and", "for", "seats", "number"]:
                name_guess = clean_w.capitalize()
                break

        res = save_booking_inquiry(name=name_guess, phone=digits, tour_slug="char-dham")
        if lang == "gu_script":
            reply = f"ધન્યવાદ {name_guess}. આપની પૂછપરછ સફળતાપૂર્વક નોંધાઈ ગઈ છે. અમારા વરિષ્ઠ ટૂર કોઓર્ડિનેટર ટૂંક સમયમાં {digits} પર આપનો સંપર્ક કરશે."
        elif lang in ["hi_roman", "hi_script"]:
            reply = f"Dhanyawad {name_guess}. Aapki inquiry darj kar li gayi he. Hamare senior tour coordinator jald hi {digits} par aapse sampark karenge."
        else:
            reply = f"Thank you {name_guess}. Your booking inquiry has been recorded. Our senior tour coordinator will connect with you shortly at **{digits}**."

        return {
            "reply": reply,
            "action_card": res.get("action_card") if isinstance(res, dict) else None,
            "suggested_questions": ["What is the package price?", "What is the day-by-day itinerary?"]
        }

    # Identify if a specific tour is mentioned in the query
    tour, matched_slug = _find_tour_package(query)
    tour_name = tour.name if tour else (_get_static_package(matched_slug).get("name") if matched_slug and _get_static_package(matched_slug) else (matched_slug.replace("-", " ").title() if matched_slug else None))

    # 2. Contact Details / Office Address / Phone / WhatsApp / Reach Us
    is_contact_query = any(k in q_lower for k in [
        "contact", "phone", "mobile", "call", "whatsapp", "number", "email",
        "address", "office", "location", "reach you", "talk to", "customer care", "helpline", "support",
        "સંપર્ક", "ફોન", "કોલ", "મોબાઇલ", "મોબાઈલ", "નંબર", "વોટ્સએપ", "ઓફિસ", "સરનામું", "સરનામુ", "વાત કરવી",
        "संपर्क", "फोन", "कॉल", "नंबर", "मोबाइल", "व्हाट्सएप", "ऑफिस", "पता", "कार्यालय", "कहाँ है", "बात करनी",
        "sampark", "office kahan", "address kya", "phone number"
    ])
    has_date_price = any(k in q_lower for k in ["date", "dates", "when", "તારીખ", "તારીખો", "तारीख", "kab", "departure", "price", "cost", "ભાવ", "કિંમત"])
    if is_contact_query and not (has_date_price and not any(ck in q_lower for ck in ["contact", "phone", "call", "number", "address", "office", "whatsapp", "સંપર્ક", "ફોન", "संपर्क", "फोन"])):
        return _handle_contact_query(lang, tour_name=tour_name)

    # 3. Conversational Greetings
    greeting_patterns = [
        "hi", "hello", "hey", "namaste", "namaskar", "pranam", "kem cho", "kemcho", "halo",
        "jai shree krishna", "radhe radhe", "har har mahadev", "ram ram", "good morning", "good evening",
        "નમસ્તે", "નમસ્કાર", "કેમ છો", "જય શ્રી કૃષ્ણ", "રાધે રાધે", "હર હર મહાદેવ",
        "नमस्ते", "नमस्कार", "जय श्री कृष्णा", "प्रणाम", "राम राम"
    ]
    is_greeting_query = any(re.search(r'\b' + re.escape(k) + r'\b', q_lower) for k in greeting_patterns) or q_lower in greeting_patterns
    if is_greeting_query and len(q_lower) <= 30 and not matched_slug and not is_contact_query:
        return _handle_greeting_query(lang)

    # 4. How to Book / Booking Process / Payment / Registration
    is_booking_process_query = any(k in q_lower for k in [
        "how to book", "booking process", "how can i book", "how do i book", "how to register",
        "reservation process", "booking kaise", "kem rite book", "booking steps", "how to reserve",
        "બુકિંગ કેવી રીતે", "કેવી રીતે બુક", "બુકિંગ પ્રક્રિયા", "ટોકન", "રજીસ્ટ્રેશન કેવી રીતે",
        "बुकिंग कैसे", "बुकिंग प्रक्रिया", "कैसे बुक करें", "रजिस्ट्रेशन कैसे"
    ])
    if is_booking_process_query and not matched_slug:
        return _handle_booking_process_query(lang)

    # 5. Inclusions / Facilities Query
    is_inclusions_query = any(k in q_lower for k in [
        "what is included", "what is include", "what are included", "package inclusion", "inclusions", "facilities",
        "amenities", "su su aave", "kya kya shamil", "કઈ કઈ સુવિધાઓ", "સુવિધાઓ", "શું સામેલ છે",
        "क्या क्या शामिल है", "सुविधाएं", "पैकेज में क्या", "what does package include"
    ])
    if is_inclusions_query and not matched_slug:
        return _handle_inclusions_query(lang)

    # 6. Cancellation / Refund
    is_cancellation_query = any(k in q_lower for k in [
        "cancel", "cancellation", "refund", "reschedule", "money back",
        "રદ્દ", "રીફંડ", "रिफंड", "कैंसिल", "रद्द"
    ])
    if is_cancellation_query and not matched_slug:
        return _handle_cancellation_query(lang)

    # 7. Hotels / Room Sharing
    is_hotel_query = any(k in q_lower for k in [
        "hotel", "room", "stay", "ac room", "sharing", "triple sharing", "double sharing",
        "હોટેલ", "રોકાણ", "રૂમ", "होटल", "कमरा", "ठहरना"
    ])
    if is_hotel_query and not matched_slug:
        return _handle_hotel_query(lang)

    # 8. Calendar Month Queries (e.g. "december me konsi tour he ?")
    month_detected = _detect_month(query)
    if month_detected and not matched_slug:
        return _handle_month_query(month_detected, lang)

    # 9. Tour List Queries (e.g. "which tour you provide ?")
    is_tour_list_query = any(k in q_lower for k in [
        "which tour", "what tour", "which yatra", "what yatra", "all tour", "all yatra",
        "list of tour", "list of yatra", "available tour", "available yatra", "types of tour",
        "tour provide", "tours provide", "tours you provide", "tour you provide", "tours offer", "tour offer",
        "konsi tour", "kaunsi tour", "konsi yatra", "kaunsi yatra", "kaun kaun si", "kon kon si",
        "kai kai tour", "kayi tour", "kai tour", "kai yatra", "kayi yatra", "tame kai",
        "konsi konsi", "konsa package", "konse package", "which package", "packages provide",
        "what are the tours", "what packages do you have", "what tours are available",
        "તમે કઈ ટૂર કરાવો છો", "કઈ કઈ ટૂર", "કઈ ટૂર", "બધી ટૂર"
    ])
    if is_tour_list_query and not matched_slug:
        return _handle_tour_list_query(lang)

    # 10. If no specific tour was matched, check other general non-tour queries:
    if not matched_slug:
        # General Food / Meals query
        if any(k in q_lower for k in ["food", "meal", "satvik", "jain", "breakfast", "dinner", "lunch", "khana", "bhojan", "ભોજન", "જમવાનું", "સાત્વિક", "જૈન", "खाना"]):
            if lang in ["hi_roman", "hi_script"]:
                reply = (
                    f"**भोजन व्यवस्था (Food Details)**:\n\n"
                    f"स्वर्णाव टूर एंड ट्रेवल्स की सभी यात्राओं में प्रतिदिन **शुद्ध शाकाहारी सात्विक दोपहर व रात का भोजन** (Lunch & Dinner) प्रदान किया जाता है, जो गुजराती और उत्तर भारतीय स्वाद के अनुसार तैयार होता है।\n\n"
                    f"प्याज और लहसुन रहित **शुद्ध जैन भोजन** भी अग्रिम सूचना पर विशेष रूप से उपलब्ध कराया जाता है।"
                )
            elif lang in ["gu_script", "gu_roman"]:
                reply = (
                    f"**ભોજન વ્યવસ્થા (Food Details)**:\n\n"
                    f"સ્વર્ણવ ટૂર એન્ડ ટ્રાવેલ્સની તમામ યાત્રાઓ દરમિયાન દૈનિક **શુદ્ધ શાકાહારી સાત્વિક ભોજન** (બપોરે અને રાત્રે) પીરસવામાં આવે છે, જે ગુજરાતી સ્વાદ અનુસાર તાજું બનાવવામાં આવે છે.\n\n"
                    f"કાંદા અને લસણ વગરનું **શુદ્ધ જૈન ભોજન** પણ અગાઉથી જણાવવા પર વિશેષ રૂપે ઉપલબ્ધ છે."
                )
            else:
                reply = (
                    f"**Meals & Dining Standard**:\n\n"
                    f"Across all Swarnav pilgrimage tours, freshly cooked **pure vegetarian Satvik lunch and dinner** are provided daily, prepared to suit Gujarati and North Indian tastes.\n\n"
                    f"Strictly **Jain meals (prepared without onion and garlic)** are arranged upon prior notice."
                )
            return {
                "reply": reply,
                "suggested_questions": ["What is the price of Char Dham tour?", "What is the date for Rameshwaram tour?", "Connect on WhatsApp"]
            }

        # General Senior Citizen / Palki / Doli query
        if any(k in q_lower for k in ["senior", "elderly", "parents", "doli", "palki", "pony", "horse", "helicopter", "heli", "ghoda", "વડીલો", "ડોળી", "પાલખી", "ઘોડા", "હેલિકોપ્ટર", "बुजुर्ग", "डोली", "पालकी"]):
            if lang in ["hi_roman", "hi_script"]:
                reply = (
                    f"**वरिष्ठ नागरिकों (Senior Citizens) के लिए व्यवस्था**:\n\n"
                    f"हमारी सभी यात्राओं का शेड्यूल वरिष्ठ तीर्थयात्रियों के स्वास्थ्य और आराम को ध्यान में रखकर धीमी गति से तैयार किया गया है।\n\n"
                    f"केदारनाथ व यमुनोत्री जैसे तीर्थों पर **पालकी/डोली, घोड़ा एवं आईआरसीटीसी हेलीकॉप्टर टोकन आरक्षण** में हमारे ऑन-ग्राउंड टूर मैनेजर पूर्ण सहयोग प्रदान करते हैं।"
                )
            elif lang in ["gu_script", "gu_roman"]:
                reply = (
                    f"**વરિષ્ઠ નાગરિકો (Senior Citizens) માટે સુવિધાઓ**:\n\n"
                    f"અમારી તમામ યાત્રાઓ વડીલો માટે અત્યંત આરામદાયક ગતિથી આયોજિત કરવામાં આવે છે.\n\n"
                    f"કેદારનાથ અને યમુનોત્રી ખાતે **પાલખી/ડોળી, ઘોડા અને હેલિકોપ્ટર ટોકન બુકિંગ** માટે અમારા ટૂર કોઓર્ડિનેટર સ્થળ પર હાજર રહીને સંપૂર્ણ મદદ કરે છે."
                )
            else:
                reply = (
                    f"**Senior Citizen Care & Trek Assistance**:\n\n"
                    f"All Swarnav pilgrimage itineraries are thoughtfully designed with comfortable pacing for elderly devotees.\n\n"
                    f"For high-altitude shrines such as Kedarnath and Yamunotri, our on-ground tour managers personally assist with local **Doli/Palki, Pony, and IRCTC helicopter booking tokens**."
                )
            return {
                "reply": reply,
                "suggested_questions": ["What is the date for Char Dham tour?", "What is the date for Rameshwaram tour?", "Connect on WhatsApp"]
            }

        # General Origin / Surat / Transport query
        if any(k in q_lower for k in ["surat", "train", "start from", "origin", "pickup", "coach", "bus", "સુરત", "ટ્રેન", "શરૂઆત", "ક્યાંથી", "ट्रेन", "सूरत", "कहाँ से"]):
            if lang in ["hi_roman", "hi_script"]:
                reply = (
                    f"**प्रस्थान बिंदु एवं यात्रा व्यवस्था**:\n\n"
                    f"स्वर्णाव टूर एंड ट्रेवल्स की सभी मुख्य यात्राएं **सूरत रेलवे स्टेशन (गुजरात)** से शुरू और समाप्त होती हैं।\n\n"
                    f"इसमें राउंड-ट्रिप कन्फर्म AC ट्रेन टिकट और स्थानीय दर्शन के लिए लग्जरी AC वाहन शामिल हैं। अहमदाबाद, वडोदरा, राजकोट, मुंबई या अन्य शहरों से सूरत कनेक्ट करने में भी हमारी टीम सहायता करती है।"
                )
            else:
                reply = (
                    f"**Origin & Transport Logistics**:\n\n"
                    f"All Swarnav pilgrimage tours officially begin and conclude at **Surat Railway Station, Gujarat** with confirmed round-trip AC train tickets and luxury pushback coaches for temple sightseeing.\n\n"
                    f"Connecting transfers to and from Surat can be arranged for devotees arriving from Ahmedabad, Vadodara, Rajkot, Mumbai, or anywhere in India."
                )
            return {
                "reply": reply,
                "suggested_questions": ["Which tours are available?", "What is the date for Rameshwaram tour?", "Connect on WhatsApp"]
            }

        # General Price query without tour
        if any(k in q_lower for k in ["price", "cost", "bhav", "kharch", "rate", "fees", "kitna", "ભાવ", "ખર્ચ", "કિંમત", "पैकेज दर"]):
            reply = (
                f"Our pilgrimage tour packages generally start from **₹30,000 per person**, which includes confirmed round-trip AC train travel from Surat, comfortable hotel accommodations (triple sharing), daily freshly cooked pure Satvik meals, and organized temple sightseeing.\n\n"
                f"Please tell us which yatra you are interested in (e.g. Char Dham, Rameshwaram, Kashmir, Jagannath Puri) for the exact package breakdown."
            )
            return {
                "reply": reply,
                "suggested_questions": ["What is the price of Char Dham?", "What is the price of Rameshwaram tour?", "What is the price of Kashmir tour?"]
            }

        # If informational, try RAG with intelligent formatting
        rag_chunks = retrieve_context(query, top_k=2)
        if rag_chunks:
            top_chunk = rag_chunks[0]
            tour_slug_chunk = top_chunk.get("tour_slug", "")
            title_chunk = top_chunk.get("title", "")
            content_chunk = top_chunk.get("content", "").strip()

            clean_lines = []
            for line in content_chunk.split("\n"):
                line = line.strip()
                if not line or line.startswith("Tour:") or line.startswith("Current Booking Status:") or line.startswith("Booking Advisory:"):
                    continue
                if line.startswith("Upcoming Confirmed Batch:"):
                    clean_lines.append(f"• **Schedule**: {line.replace('Upcoming Confirmed Batch:', '').strip()}")
                else:
                    clean_lines.append(line)

            if clean_lines:
                formatted_reply = f"**{title_chunk}**:\n\n" + "\n".join(clean_lines[:6])
                return {
                    "reply": formatted_reply,
                    "suggested_questions": [
                        "What is the date for Char Dham tour?",
                        "What is the date for Rameshwaram tour?",
                        "What is the package price of Kashmir tour?"
                    ]
                }

        # Graceful fallback guiding the user
        return _handle_general_fallback(lang)

    # 11. A specific tour WAS matched!
    static_pkg = _get_static_package(matched_slug) if matched_slug else None
    tour_name = tour.name if tour else (static_pkg.get("name") if static_pkg else matched_slug.replace("-", " ").title())
    tour_date = getattr(tour, "tour_date", "").strip() if tour else ""
    is_active = getattr(tour, "is_active", False) if tour else False
    starting_price = (tour.starting_price if tour and tour.starting_price else (static_pkg.get("starting_price") if static_pkg else "₹30,000")) or "₹30,000"
    duration_display = (tour.duration_display if tour and tour.duration_display else (static_pkg.get("duration_display") if static_pkg else "12 Days / 11 Nights")) or "12 Days"
    departures_summary = (static_pkg.get("departures_summary") if static_pkg else "Monthly Scheduled Departures") or "Monthly Scheduled Departures"

    # Intent detection for the specific tour
    is_date_query = any(k in q_lower for k in [
        "date", "dates", "when", "start date", "starting date", "next tour", "next batch", "batch", "schedule", "kab", "departure",
        "તારીખ", "ક્યારે", "શરૂ", "શેડ્યૂલ", "તારીખો", "तारीख", "कब", "shuru", "tarikh", "dates for", "final date"
    ])
    is_price_query = any(k in q_lower for k in [
        "package", "price", "pricing", "cost", "how much", "rate", "fees", "kitna", "kitni", "kya price", "bhav", "kharch",
        "ખર્ચ", "ભાવ", "કિંમત", "ભાડું", "દામ", "फीस", "लागत", "दाम", "કિંમત કેટલી"
    ])
    is_itinerary_query = any(k in q_lower for k in [
        "itinerary", "itenarary", "route", "plan", "days", "schedule of", "places covered", "attractions", "sightseeing",
        "રૂટ", "પ્લાન", "શેડ્યૂલ", "સ્થળો", "यात्रा मार्ग", "रूट"
    ])
    is_food_query = any(k in q_lower for k in [
        "food", "meal", "meals", "satvik", "jain", "breakfast", "dinner", "lunch", "khana", "bhojan",
        "ભોજન", "જમવાનું", "સાત્વિક", "જૈન", "खाना", "सात्विक", "जैन"
    ])
    is_senior_query = any(k in q_lower for k in [
        "senior", "elderly", "parents", "doli", "palki", "pony", "horse", "helicopter", "heli", "ghoda",
        "વડીલો", "ડોળી", "પાલખી", "ઘોડા", "હેલિકોપ્ટર", "बुजुर्ग", "डोली", "पालकी", "घोड़ा"
    ])
    is_origin_transport_query = any(k in q_lower for k in [
        "surat", "train", "start from", "origin", "flight", "transport", "pickup", "coach", "bus",
        "સુરત", "ટ્રેન", "શરૂઆત", "ક્યાંથી", "ट्रेन", "सूरत", "कहाँ से"
    ])

    day_match = re.search(r'\bday\s*(\d+)\b', q_lower)
    specific_day = int(day_match.group(1)) if day_match else None

    def get_chips(current_intent: str) -> List[str]:
        chips = []
        if current_intent != "date":
            chips.append(f"What is the date for {tour_name}?")
        if current_intent != "price":
            chips.append(f"What is the price of {tour_name}?")
        if current_intent != "itinerary":
            chips.append(f"What is the route for {tour_name}?")
        chips.append("Connect on WhatsApp")
        return chips[:3]

    # Specific Tour Date Query
    if is_date_query:
        if matched_slug == "kerala-tour":
            if lang == "gu_script":
                reply = (
                    f"**કેરળ ટૂર (Kerala Tour - God’s Own Country)** ની આગામી તારીખ હજુ કન્ફર્મ થઈ નથી.\n\n"
                    f"વધુ માહિતી મેળવવા માટે કૃપા કરીને **{PHONE_NUMBER}** પર અથવા WhatsApp (**{WHATSAPP_NUMBER}**) દ્વારા સંપર્ક કરો."
                )
            elif lang == "gu_roman":
                reply = (
                    f"**Kerala Tour** ni next tour date haju confirm thay nathi.\n\n"
                    f"Vadhu mahiti mate kripya **{PHONE_NUMBER}** par athva WhatsApp (**{WHATSAPP_NUMBER}**) par contact karo."
                )
            elif lang in ["hi_roman", "hi_script"]:
                reply = (
                    f"**केरल टूर (Kerala Tour - God’s Own Country)** की अगली प्रस्थान तारीख अभी कन्फर्म नहीं हुई है।\n\n"
                    f"अधिक जानकारी प्राप्त करने के लिए कृपया **{PHONE_NUMBER}** पर या WhatsApp (**{WHATSAPP_NUMBER}**) द्वारा संपर्क करें।"
                )
            else:
                reply = (
                    f"Next Kerala tour date is not confirmed yet. Please contact on **{PHONE_NUMBER}** to get more information."
                )
            return {"reply": reply, "suggested_questions": ["What is the price of Kerala Tour?", "What is the route for Kerala Tour?", "Connect on WhatsApp"]}

        elif tour_date:
            if lang == "gu_script":
                reply = f"**{tour_name}** ની આગામી કન્ફર્મ તારીખ **{tour_date}** છે. સુરત રેલવે સ્ટેશનથી પ્રસ્થાન અને કન્ફર્મ AC ટ્રેન ટિકિટ તથા હોટેલ રોકાણની વ્યવસ્થા સામેલ છે."
            elif lang == "gu_roman":
                reply = f"**{tour_name}** ni next confirmed date **{tour_date}** che. Surat thi train ane stay vyavastha shamil che."
            elif lang in ["hi_roman", "hi_script"]:
                reply = f"**{tour_name}** की अगली कन्फर्म प्रस्थान तारीख **{tour_date}** है। सूरत से प्रस्थान व वापसी की संपूर्ण AC ट्रेन व होटल व्यवस्था शामिल है।"
            else:
                reply = f"The next confirmed departure for **{tour_name}** is **{tour_date}**. The tour begins and concludes at Surat Railway Station with confirmed round-trip AC train travel and quality accommodations."
            return {"reply": reply, "suggested_questions": get_chips("date")}

        elif matched_slug == "rameshwaram-circuit":
            if lang == "gu_script":
                reply = (
                    f"**{tour_name}** માટે સુરત રેલવે સ્ટેશનથી **દર મહિને નિયમિત ગ્રૂપ ટૂર (Monthly Scheduled Departures)** આયોજિત કરવામાં આવે છે.\n\n"
                    f"આગામી કન્ફર્મ પ્રસ્થાન તારીખ અને સીટ ઉપલબ્ધતા માટે આપ સીધા અમારા કો-ઓર્ડિનેટરનો **{PHONE_NUMBER}** પર અથવા WhatsApp (**{WHATSAPP_NUMBER}**) દ્વારા સંપર્ક કરી શકો છો."
                )
            elif lang == "gu_roman":
                reply = (
                    f"**{tour_name}** mate Surat thi **Monthly Scheduled Departures** (dar mahine group batches) aayojit thay che.\n\n"
                    f"Aagami confirmed tarikh ane seat booking mate tame seedha amara coordinator **{PHONE_NUMBER}** athva WhatsApp (**{WHATSAPP_NUMBER}**) par sampark kari shako cho."
                )
            elif lang in ["hi_roman", "hi_script"]:
                reply = (
                    f"**{tour_name}** के लिए सूरत रेलवे स्टेशन से **प्रतिमाह नियमित ग्रुप टूर (Monthly Scheduled Departures)** आयोजित किए जाते हैं।\n\n"
                    f"आगामी कन्फर्म प्रस्थान तारीख और सीट उपलब्धता की जानकारी के लिए आप हमारे को-ઓર્ડિનેટર से **{PHONE_NUMBER}** या WhatsApp (**{WHATSAPP_NUMBER}**) पर संपर्क कर सकते हैं।"
                )
            else:
                reply = (
                    f"**{tour_name}** offers **Monthly Scheduled Departures** starting and ending at Surat Railway Station.\n\n"
                    f"Regular group batches depart every month. For the upcoming confirmed calendar departure dates and seat reservations, please connect directly with our coordination team at **{PHONE_NUMBER}** or via WhatsApp (**{WHATSAPP_NUMBER}**)."
                )
            return {"reply": reply, "suggested_questions": get_chips("date")}

        else:
            if lang == "gu_script":
                reply = (
                    f"**{tour_name}** ની આગામી તારીખ હજુ કન્ફર્મ થઈ નથી.\n\n"
                    f"વધુ માહિતી મેળવવા માટે કૃપા કરીને **{PHONE_NUMBER}** પર અથવા WhatsApp (**{WHATSAPP_NUMBER}**) દ્વારા સંપર્ક કરો."
                )
            elif lang in ["hi_roman", "hi_script"]:
                reply = (
                    f"**{tour_name}** की अगली प्रस्थान तारीख अभी कन्फर्म नहीं हुई है।\n\n"
                    f"अधिक जानकारी प्राप्त करने के लिए कृपया सीधे **{PHONE_NUMBER}** पर संपर्क करें।"
                )
            else:
                reply = (
                    f"The next departure date for **{tour_name}** is not confirmed yet.\n\n"
                    f"Please contact on **{PHONE_NUMBER}** to get more information."
                )
            return {"reply": reply, "suggested_questions": get_chips("date")}

    # Specific Tour Price Query
    if is_price_query:
        if lang == "gu_script":
            reply = (
                f"**{tour_name}** નો શરૂઆતી પેકેજ ભાવ **{starting_price}** પ્રતિ વ્યક્તિ ({duration_display}) છે.\n\n"
                f"આ પેકેજમાં સુરતથી કન્ફર્મ AC ટ્રેન ટિકિટ, હોટેલ રોકાણ (ટ્રિપલ શેરિંગ), દૈનિક શુદ્ધ સાત્વિક ભોજન અને ગાઈડેડ દર્શનનો સમાવેશ થાય છે."
            )
        elif lang == "gu_roman":
            reply = (
                f"**{tour_name}** no starting package bhav **{starting_price}** prati vyakti ({duration_display}) che.\n\n"
                f"Surat thi round-trip AC train tickets, hotel stay, Satvik bhojan ane darshan vyavastha shamil che."
            )
        elif lang in ["hi_roman", "hi_script"]:
            reply = (
                f"**{tour_name}** का प्रारंभिक पैकेज मूल्य **{starting_price}** प्रति व्यक्ति ({duration_display}) है।\n\n"
                f"इसमें सूरत से राउंड-ट्रिप कन्फर्म AC ट्रेन टिकट, होटल आवास, दैनिक शुद्ध सात्विक भोजन और सभी स्थानीय दर्शन शामिल हैं।"
            )
        else:
            reply = (
                f"The starting package price for **{tour_name}** is **{starting_price}** per person ({duration_display}).\n\n"
                f"This includes confirmed round-trip AC train travel from Surat, comfortable hotel accommodations, daily freshly cooked pure Satvik meals, and organized temple darshans."
            )

        return {"reply": reply, "suggested_questions": get_chips("price")}

    # Specific Tour Itinerary Query
    if is_itinerary_query or specific_day is not None:
        summary = _get_tour_itinerary_summary(tour, matched_slug, specific_day=specific_day, lang=lang)
        return {"reply": summary, "suggested_questions": get_chips("itinerary")}

    # Specific Tour Food Query
    if is_food_query:
        if lang == "gu_script":
            reply = (
                f"**{tour_name}** દરમિયાન દૈનિક શુદ્ધ સાત્વિક ભોજન (બપોરે અને રાત્રે) પીરસવામાં આવે છે.\n\n"
                f"કાંદા અને લસણ વગરનું શુદ્ધ જૈન ભોજન પણ અગાઉથી જણાવવા પર ઉપલબ્ધ કરાવવામાં આવે છે."
            )
        elif lang in ["hi_roman", "hi_script"]:
            reply = (
                f"**{tour_name}** में प्रतिदिन शुद्ध शाकाहारी सात्विक दोपहर व रात्रि भोजन की व्यवस्था की जाती है।\n\n"
                f"प्याज-लहसुन रहित शुद्ध जैन भोजन भी अग्रिम सूचना पर उपलब्ध है।"
            )
        else:
            reply = (
                f"For **{tour_name}**, freshly cooked pure vegetarian Satvik lunch and dinner are served daily.\n\n"
                f"Special Jain meals (strictly without onion and garlic) are also happily arranged upon advance notice."
            )
        return {"reply": reply, "suggested_questions": get_chips("food")}

    # Specific Tour Senior Citizens Query
    if is_senior_query:
        if lang == "gu_script":
            reply = (
                f"**{tour_name}** નું આયોજન વરિષ્ઠ નાગરિકો (Senior Citizens) માટે અત્યંત આરામદાયક અને અનુકૂળ રીતે કરવામાં આવે છે.\n\n"
                f"ઊંચાઈવાળા યાત્રાધામો (જેમ કે કેદારનાથ/યમુનોત્રી) ખાતે પાલખી/ડોળી, ઘોડા અને IRCTC હેલિકોપ્ટર ટોકન બુકિંગમાં અમારા ટૂર મેનેજર સીધી સહાય પૂરી પાડે છે."
            )
        elif lang in ["hi_roman", "hi_script"]:
            reply = (
                f"**{tour_name}** वरिष्ठ नागरिकों (Senior Citizens) के लिए अत्यंत सुगम और आरामदायक गति से संचालित की जाती है।\n\n"
                f"केदारनाथ व यमुनोत्री जैसे तीर्थों पर पालकी/डोली, घोड़ा और हेलीकॉप्टर टोकन व्यवस्था में हमारे अनुभवी टूर मैनेजर पूर्ण सहयोग प्रदान करते हैं।"
            )
        else:
            reply = (
                f"**{tour_name}** is thoughtfully paced for senior citizens and elderly pilgrims.\n\n"
                f"For high-altitude shrines such as Kedarnath and Yamunotri, our dedicated tour managers personally assist with local Doli/Palki, Pony, and official IRCTC helicopter shuttle token booking."
            )
        return {"reply": reply, "suggested_questions": get_chips("senior")}

    # Specific Tour Transport / Origin Query
    if is_origin_transport_query:
        if lang == "gu_script":
            reply = (
                f"**{tour_name}** ની શરૂઆત અને સમાપન **સુરત રેલવે સ્ટેશન (ગુજરાત)** થી થાય છે.\n\n"
                f"યાત્રીઓ માટે કન્ફર્મ AC ટ્રેન ટિકિટ અને સ્થાનિક મુસાફરી માટે સેનિટાઈઝ્ડ AC લક્ઝરી કોચ સામેલ છે. અમદાવાદ, વડોદરા, રાજકોટ કે અન્ય શહેરોથી સુરત પહોંચવા માટે પણ સહાય ઉપલબ્ધ છે."
            )
        elif lang in ["hi_roman", "hi_script"]:
            reply = (
                f"**{tour_name}** का प्रस्थान और समापन **सूरत रेलवे स्टेशन (गुजरात)** से होता है।\n\n"
                f"इसमें राउंड-ट्रिप कन्फर्म AC ट्रेन टिकट्स और स्थानीय यात्रा हेतु लग्जरी AC बस/ट्रेवलर की सुविधा शामिल है। गुजरात के किसी भी शहर से सूरत कनेक्ट करने में हमारी टीम मदद करती है।"
            )
        else:
            reply = (
                f"**{tour_name}** officially commences and concludes at **Surat Railway Station, Gujarat**.\n\n"
                f"Round-trip confirmed AC train tickets and dedicated sanitized AC coach/Tempo Traveller transportation for all interstate and temple transits are fully organized. Connecting transit from Ahmedabad, Vadodara, Rajkot, or Mumbai to Surat is also arranged upon request."
            )
        return {"reply": reply, "suggested_questions": get_chips("origin")}

    # Specific Tour General Overview
    if tour_date:
        date_str = f"Next Confirmed Batch: **{tour_date}**"
    elif matched_slug == "rameshwaram-circuit":
        date_str = "Departures: **Monthly Scheduled Departures**"
    elif matched_slug == "kerala-tour":
        date_str = "Departures: **Date not confirmed yet (Inquiries Open)**"
    else:
        date_str = f"Departures: **{departures_summary}**"

    if lang == "gu_script":
        reply = (
            f"**{tour_name}** ({duration_display}):\n"
            f"• શરૂઆતી પેકેજ ભાવ: **{starting_price}** પ્રતિ વ્યક્તિ\n"
            f"• પ્રસ્થાન: {date_str}\n"
            f"• પ્રસ્થાન સ્થળ: સુરત રેલવે સ્ટેશન\n\n"
            f"સંપૂર્ણ બ્રોશર અથવા સીટ બુકિંગ માટે આપ **{PHONE_NUMBER}** પર અથવા WhatsApp (**{WHATSAPP_NUMBER}**) દ્વારા અમારો સંપર્ક કરી શકો છો."
        )
    elif lang in ["hi_roman", "hi_script"]:
        reply = (
            f"**{tour_name}** ({duration_display}):\n"
            f"• स्टार्टिंग पैकेज मूल्य: **{starting_price}** प्रति व्यक्ति\n"
            f"• शेड्यूल: {date_str}\n"
            f"• प्रस्थान: सूरत रेलवे स्टेशन\n\n"
            f"विस्तृत ब्रोशर या सीट आरक्षण के लिए आप सीधे **{PHONE_NUMBER}** या WhatsApp (**{WHATSAPP_NUMBER}**) पर संपर्क कर सकते हैं।"
        )
    else:
        reply = (
            f"**{tour_name}** ({duration_display}):\n"
            f"• Starting Package: **{starting_price}** per person\n"
            f"• Schedule: {date_str}\n"
            f"• Starting Point: Surat Railway Station\n\n"
            f"For customized family bookings or brochure PDF, connect directly with our coordination team at **{PHONE_NUMBER}**."
        )

    return {"reply": reply, "suggested_questions": get_chips("overview")}


def execute_agent_chat(user_message: str, session_history: Optional[List[Dict[str, str]]] = None, requested_lang: Optional[str] = None) -> Dict[str, Any]:
    """
    Main entry point for Swarnav AI Pilgrimage Assistant.
    Guarantees a verified, error-free answer using the deterministic factual engine,
    and optionally refines phrasing if an active cloud LLM key is configured.
    """
    user_msg_clean = (user_message or "").strip()
    if not user_msg_clean:
        return {
            "reply": "Please enter a question regarding our pilgrimage tours (e.g. Char Dham, Rameshwaram, Kashmir, Jagannath Puri).",
            "suggested_questions": [
                "Which tours do you provide?",
                "What is the date for Rameshwaram tour?",
                "What is the price of Kashmir tour?"
            ]
        }

    # Step 1: Generate the rock-solid factual response
    try:
        factual_result = _generate_precise_response(user_msg_clean, requested_lang=requested_lang)
    except Exception as exc:
        logger.exception("Unexpected error in _generate_precise_response: %s", exc)
        factual_result = {
            "reply": (
                f"Swarnav Tour & Travels offers personalized pilgrimage services for Char Dham, "
                f"Rameshwaram, Kashmir, Jagannath Puri, and Nepal. For immediate inquiries, please call **{PHONE_NUMBER}** or WhatsApp **{WHATSAPP_NUMBER}**."
            ),
            "suggested_questions": [
                "Which tours do you provide?",
                "What is the date for Rameshwaram tour?",
                "What is the price of Kashmir tour?"
            ]
        }

    # Step 2: If a cloud LLM is configured (OpenAI or Gemini), attempt graceful synthesis
    openai_client = get_openai_client()
    if openai_client:
        try:
            prompt = (
                f"You are the official pilgrimage AI assistant for Swarnav Tour & Travels.\n"
                f"Devotee's Question: \"{user_msg_clean}\"\n"
                f"Verified Factual Data: \"{factual_result['reply']}\"\n\n"
                f"INSTRUCTIONS:\n"
                f"1. Answer concisely based strictly on the verified factual data above.\n"
                f"2. Match the language (English, Gujarati, or Hindi) of the devotee's question.\n"
                f"3. Do not add fictitious contact numbers or unverified dates.\n"
                f"4. Keep markdown bolding (**important facts**) intact."
            )

            resp = openai_client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=300
            )
            llm_text = resp.choices[0].message.content.strip() if resp.choices else ""
            if llm_text:
                factual_result["reply"] = llm_text
                factual_result["provider"] = "openai"
        except Exception as err:
            logger.debug("Cloud LLM optional synthesis skipped (%s); returning verified local response.", err)

    return factual_result
