"""
Agent Tools for Swarnav Tour & Travels AI Assistant.
Callable functions provided to Gemini for querying itineraries, dynamic cost calculations,
checking senior citizen / trek advisories, and recording verified booking leads into Django.
"""
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


def get_tour_itinerary_details(tour_slug: str, day_number: Optional[int] = None) -> Dict[str, Any]:
    """
    Get verified day-by-day itinerary, schedule, altitude, hotel, and darshan tips for a tour.
    Args:
        tour_slug: Slug of the tour package (e.g. 'char-dham', 'panch-kedar', 'jagannath-puri', 'kashmir-paradise', 'nepal-pashupatinath-muktinath', 'rameshwaram-circuit', 'kerala-tour').
        day_number: Optional specific day number (e.g. 7 for Kedarnath trek). If omitted, returns overview of all days.
    """
    from yatras.models import TourPackage, ItineraryDay

    try:
        tour = TourPackage.objects.filter(slug__iexact=tour_slug).first()
        if not tour:
            tour = TourPackage.objects.filter(name__icontains=tour_slug).first()
        if not tour:
            return {"status": "error", "message": f"Tour '{tour_slug}' not found in database."}

        days_qs = ItineraryDay.objects.filter(tour=tour).order_by('day_number')
        if day_number:
            day = days_qs.filter(day_number=day_number).first()
            if not day:
                return {
                    "status": "error",
                    "message": f"Day {day_number} not found for {tour.name}. Tour duration is {tour.duration_days} days."
                }
            return {
                "status": "success",
                "tour": tour.name,
                "day_number": day.day_number,
                "title": day.title,
                "route": day.route_summary,
                "altitude": day.altitude,
                "stay": f"{day.night_stay} ({day.hotel_type})",
                "hotel_name": day.hotel_name,
                "meals": day.meals,
                "intro": day.intro,
                "schedule": day.schedule,
                "darshan_tips": day.darshan_tips,
                "scenic_points": day.scenic_points
            }
        else:
            summary_days = []
            for d in days_qs:
                summary_days.append({
                    "day": d.day_number,
                    "title": d.title,
                    "route": d.route_summary,
                    "stay": d.night_stay,
                    "altitude": d.altitude
                })
            return {
                "status": "success",
                "tour": tour.name,
                "total_days": tour.duration_days,
                "itinerary_days": summary_days
            }
    except Exception as exc:
        logger.exception("Error in get_tour_itinerary_details: %s", exc)
        return {"status": "error", "message": str(exc)}


def calculate_yatra_price(tour_slug: str = "char-dham", number_of_pilgrims: int = 1, room_sharing: str = "triple") -> Dict[str, Any]:
    """
    Calculate estimated package cost for a given number of travelers and room sharing type.
    Args:
        tour_slug: The tour slug (e.g. 'char-dham', 'jagannath-puri', 'nepal-pashupatinath-muktinath').
        number_of_pilgrims: Count of adult travelers (default 1).
        room_sharing: Accommodation preference ('triple', 'double', 'single').
    """
    from yatras.models import TourPackage

    try:
        tour = TourPackage.objects.filter(slug__iexact=tour_slug).first()
        if not tour:
            tour = TourPackage.objects.filter(name__icontains=tour_slug).first()

        # Default base rates
        base_rate_map = {
            "char-dham": 30000,
            "panch-kedar": 26500,
            "kashmir-paradise": 22500,
            "rameshwaram-circuit": 24000,
            "kerala-tour": 19500,
            "jagannath-puri": 24500,
            "nepal-pashupatinath-muktinath": 34500,
            "jharkhand-tour": 14500
        }

        slug_clean = tour.slug if tour else tour_slug.lower()
        base_per_person = base_rate_map.get(slug_clean, 30000)

        sharing_multiplier = 1.0
        sharing_desc = "Triple-sharing (Standard)"
        if "double" in room_sharing.lower() or "twin" in room_sharing.lower():
            sharing_multiplier = 1.15
            sharing_desc = "Double/Twin-sharing (+15% room surcharge)"
        elif "single" in room_sharing.lower():
            sharing_multiplier = 1.35
            sharing_desc = "Single occupancy room"

        rate_per_person = int(base_per_person * sharing_multiplier)
        total_estimate = rate_per_person * max(1, number_of_pilgrims)

        return {
            "status": "success",
            "tour_name": tour.name if tour else tour_slug,
            "duration": tour.duration_display if tour else "Standard Yatra",
            "pilgrims_count": number_of_pilgrims,
            "sharing_type": sharing_desc,
            "estimated_rate_per_person": f"₹{rate_per_person:,}",
            "estimated_total": f"₹{total_estimate:,}",
            "key_inclusions": [
                "Surat to Haridwar return train tickets (or origin connectivity)",
                "Dedicated mountain group transport across Uttarakhand",
                "Hotel stays across all night stops",
                "Hygienic, pure vegetarian Satvik Lunch & Dinner daily",
                "Char Dham bio-metric / yatra registration assistance",
                "Dedicated experienced tour coordinator throughout the circuit"
            ],
            "note": "Final exact pricing confirmed upon booking depending on train berth class and departure batch date."
        }
    except Exception as exc:
        logger.exception("Error in calculate_yatra_price: %s", exc)
        return {"status": "error", "message": str(exc)}


def check_travel_guidelines(tour_slug: str = "char-dham", topic: str = "senior_citizen") -> Dict[str, Any]:
    """
    Get authoritative guidelines on senior citizen care, Kedarnath helicopter/palki/pony, health fitness, packing, and registration.
    Args:
        tour_slug: Tour identifier (default 'char-dham').
        topic: Specific area: 'senior_citizen', 'helicopter_pony', 'medical', 'packing', or 'registration'.
    """
    from yatras.models import TravelGuide, TourPackage

    try:
        tour = TourPackage.objects.filter(slug__iexact=tour_slug).first()
        tg = TravelGuide.objects.filter(tour=tour).first() if tour else None

        guidance = {
            "senior_citizen_and_palki": (
                "For senior citizens on high-altitude Dhams (Kedarnath & Yamunotri): "
                "1. Kedarnath (16 km trek): Options include Palki / Doli (approx ₹8,000–₹12,000 round trip operated by local porters under district regulation), "
                "Pony / Kandi (approx ₹4,000–₹6,000), or Helicopter Shuttle from Phata/Guptkashi/Sirsi (operated via official IRCTC Heli Yatra portal). "
                "2. Yamunotri (6 km trek from Janki Chatti): Palki / Doli or Pony is available. "
                "3. Our on-ground tour coordinator assists senior pilgrims in obtaining tokens and arranging verified pony/doli operators. "
                "4. Frequent rest pauses and paced journeys are incorporated into all Swarnav itineraries."
            ),
            "medical_advisory": (
                "1. Medical Checkup: Consult a doctor for a routine heart and blood pressure fitness checkup before travel. "
                "2. Acclimatization: Drink plenty of warm water, take ginger/tulsi tea, and walk at a steady, measured pace. "
                "3. Personal Medicine: Carry a 15-day supply of daily medicines plus cold/altitude medication."
            ),
            "packing_checklist": (
                "Essential Packing for Garhwal Himalayas: Heavy woolens, thermal innerwear (2-3 pairs), windproof/waterproof jacket, "
                "sturdy walking shoes with rubber grip, woolen socks & gloves, rain poncho/umbrella, power bank, Aadhaar card copies, and cash for remote halts."
            ),
            "registration": (
                "Mandatory Uttarakhand Tourism Registration: All pilgrims must be registered on the official portal (registrationandtouristcare.uk.gov.in). "
                "Swarnav Tour & Travels handles and coordinates biometric registration support for all confirmed group members."
            )
        }

        if tg:
            return {
                "status": "success",
                "tour": tour.name,
                "senior_citizen_tips": tg.senior_citizen_tips or guidance["senior_citizen_and_palki"],
                "medical_advisory": tg.medical_advisory or guidance["medical_advisory"],
                "packing_list": tg.packing_list or guidance["packing_checklist"],
                "registration_process": tg.registration_process or guidance["registration"]
            }

        return {
            "status": "success",
            "tour": tour_slug,
            "guidelines": guidance
        }
    except Exception as exc:
        logger.exception("Error in check_travel_guidelines: %s", exc)
        return {"status": "error", "message": str(exc)}


def save_booking_inquiry(
    name: str,
    phone: str,
    tour_slug: str = "char-dham",
    pilgrims_count: int = 1,
    departure_city: str = "",
    travel_month: str = ""
) -> Dict[str, Any]:
    """
    Save a new customer pilgrimage booking inquiry into the Django database,
    triggers notification email to admin, and generates a pre-filled WhatsApp link.
    Args:
        name: Full name of the pilgrim / inquirer.
        phone: 10-digit mobile or WhatsApp phone number.
        tour_slug: The selected tour package code.
        pilgrims_count: Number of travelers (default 1).
        departure_city: City from which pilgrim will travel (e.g. Surat, Ahmedabad, Rajkot, Mumbai).
        travel_month: Preferred travel month (e.g. May 2025, Autumn Batch, etc.).
    """
    from core.models import Inquiry
    from core.email_utils import send_admin_inquiry_notification
    from core.views import build_whatsapp_url

    try:
        clean_phone = "".join(c for c in phone if c.isdigit() or c == "+")
        if len(clean_phone) < 8:
            return {
                "status": "error",
                "message": "Please provide a valid 10-digit mobile or WhatsApp number so our team can coordinate with you."
            }

        tour_choice = tour_slug.lower()
        if tour_choice not in dict(Inquiry.TOUR_CHOICES):
            # Match substring
            matched = False
            for code, _ in Inquiry.TOUR_CHOICES:
                if code in tour_choice or tour_choice in code:
                    tour_choice = code
                    matched = True
                    break
            if not matched:
                tour_choice = "char-dham"

        inquiry = Inquiry.objects.create(
            name=name.strip(),
            phone=clean_phone,
            tour=tour_choice,
            total_pilgrims=pilgrims_count or 1,
            departure_city=departure_city.strip(),
            message=f"Created via Swarnav AI Assistant. Preferred Month: {travel_month or 'Not specified'}",
            status="new",
            consent_given=True
        )

        # Trigger admin notification email
        try:
            send_admin_inquiry_notification(inquiry)
        except Exception as e:
            logger.warning("Could not send admin email notification: %s", e)

        # Build official WhatsApp link with prefilled reference
        wa_link = build_whatsapp_url(inquiry)
        ref_id = f"SW-INQ-{inquiry.id:04d}"

        return {
            "status": "success",
            "inquiry_id": inquiry.id,
            "inquiry_ref": ref_id,
            "name": inquiry.name,
            "phone": inquiry.phone,
            "tour": inquiry.get_tour_display(),
            "pilgrims_count": inquiry.total_pilgrims,
            "whatsapp_link": wa_link,
            "message": (
                f"Jai Shri Krishna / Har Har Mahadev! Your inquiry #{ref_id} has been recorded successfully in our system. "
                f"Our senior tour coordinator will reach out to you at {clean_phone}. "
                f"You can also tap the direct WhatsApp link below to chat with us immediately."
            )
        }
    except Exception as exc:
        logger.exception("Error saving inquiry via AI Assistant: %s", exc)
        return {"status": "error", "message": f"Could not record inquiry due to: {str(exc)}"}


# Registry of available tools for Gemini Agent
AVAILABLE_AGENT_TOOLS = [
    get_tour_itinerary_details,
    calculate_yatra_price,
    check_travel_guidelines,
    save_booking_inquiry
]
