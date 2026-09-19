import datetime

def business_info(request):
    """
    Centralized business details for Swarnav Tour & Travels.
    """
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
    }

