import datetime


def business_info(request):
    """
    Centralized business details for Swarnav Tour & Travels.
    Includes live active_tours status dictionary synced from database.
    """
    active_tours = {
        'char_dham': True,
        'kashmir_paradise': True,
        'rameshwaram_circuit': True,
        'kerala_tour': True,
        'jagannath_puri': True,
        'panch_kedar': False,
        'jharkhand_tour': False,
        'nepal_pashupatinath_muktinath': False,
    }
    tours_map = {}
    try:
        from yatras.models import TourPackage
        for t in TourPackage.objects.all():
            key = t.slug.replace('-', '_')
            active_tours[key] = t.is_active
            tours_map[key] = t
            tours_map[t.slug] = t
    except Exception:
        pass

    return {
        'BUSINESS_NAME': 'Swarnav Tour & Travels',
        'BRAND_NAME': 'Swarnav',
        'BUSINESS_TAGLINE': 'Spiritual Pilgrimages & Nature Journeys Across India & Nepal',
        'PHONE_NUMBER': '+91 95868 25353',
        'PHONE_RAW': '+919586825353',
        'WHATSAPP_NUMBER': '+91 95868 25353',
        'WHATSAPP_LINK': 'https://wa.me/919586825353',
        'EMAIL': 'info@swarnavtravels.com',
        'OFFICE_ADDRESS': 'Ring Road, Surat, Gujarat - 395002',
        'PRIMARY_REGION': 'Surat, Gujarat',
        'OPERATING_HOURS': 'Daily: 7:00 AM – 9:30 PM (IST)',
        'CURRENT_YEAR': datetime.date.today().year,
        'active_tours': active_tours,
        'tours_map': tours_map,
    }


