from django.shortcuts import render
from django.http import Http404
from .data.char_dham import (
    CHAR_DHAM_PACKAGE,
    ITINERARY_DAYS,
    PACKAGE_DETAILS,
    STAY_AND_TRAVEL,
    TRAVEL_GUIDE,
    POLICIES,
    CHAR_DHAM_NAV_TABS
)
from .data.puri_eastern import (
    PURI_PACKAGE,
    PURI_ITINERARY_DAYS,
    PURI_PACKAGE_DETAILS,
    PURI_STAY_AND_TRAVEL,
    PURI_TRAVEL_GUIDE,
    PURI_POLICIES,
    PURI_NAV_TABS
)

# --------------------------------------------------------------------------
# Char Dham Yatra Views
# --------------------------------------------------------------------------
def _get_char_dham_base_context(active_slug, current_page_label, prev_nav, next_nav):
    return {
        'package': CHAR_DHAM_PACKAGE,
        'nav_tabs': CHAR_DHAM_NAV_TABS,
        'active_tab': active_slug,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': 'Char Dham', 'url_name': 'yatras:char_dham_overview'},
            {'label': current_page_label, 'url_name': None} if active_slug != 'overview' else None
        ],
        'prev_page': prev_nav,
        'next_page': next_nav,
    }

def char_dham_overview(request):
    """Main overview landing page for Char Dham Yatra."""
    context = _get_char_dham_base_context(
        active_slug='overview',
        current_page_label='Overview',
        prev_nav=None,
        next_nav={'name': 'Itinerary', 'url_name': 'yatras:char_dham_itinerary'}
    )
    context.update({
        'page_title': 'Char Dham Yatra 13 Days Pilgrimage from Surat | Swarnav',
        'meta_description': 'Explore the sacred 13-day Char Dham Yatra by Swarnav from Surat across Yamunotri, Gangotri, Kedarnath, and Badrinath with arranged travel and stay.',
        'itinerary_summary': ITINERARY_DAYS[:4],
    })
    return render(request, 'yatras/char_dham/overview.html', context)

def char_dham_itinerary(request):
    """Detailed day-by-day 13-day itinerary."""
    context = _get_char_dham_base_context(
        active_slug='itinerary',
        current_page_label='13-Day Itinerary',
        prev_nav={'name': 'Overview', 'url_name': 'yatras:char_dham_overview'},
        next_nav={'name': 'Package Details', 'url_name': 'yatras:char_dham_package_details'}
    )
    context.update({
        'page_title': '13-Day Detailed Itinerary | Char Dham Yatra | Swarnav',
        'meta_description': 'Day-by-day spiritual itinerary for the 13-day Char Dham Yatra from Surat covering Haridwar, Yamunotri, Gangotri, Kedarnath, and Badrinath.',
        'itinerary_days': ITINERARY_DAYS,
    })
    return render(request, 'yatras/char_dham/itinerary.html', context)

def char_dham_day_detail(request, day_number):
    """Route-detail page for an individual day of the Char Dham itinerary."""
    if day_number < 1 or day_number > len(ITINERARY_DAYS):
        raise Http404(f"Itinerary Day {day_number} does not exist in the 13-day Char Dham schedule.")
    
    day_data = ITINERARY_DAYS[day_number - 1]
    prev_day = ITINERARY_DAYS[day_number - 2] if day_number > 1 else None
    next_day = ITINERARY_DAYS[day_number] if day_number < len(ITINERARY_DAYS) else None

    context = {
        'package': CHAR_DHAM_PACKAGE,
        'nav_tabs': CHAR_DHAM_NAV_TABS,
        'active_tab': 'itinerary',
        'day': day_data,
        'prev_day': prev_day,
        'next_day': next_day,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': 'Char Dham', 'url_name': 'yatras:char_dham_overview'},
            {'label': '13-Day Itinerary', 'url_name': 'yatras:char_dham_itinerary'},
            {'label': f"Day {day_number}: {day_data['title']}", 'url_name': None}
        ],
        'page_title': f"Day {day_number}: {day_data['title']} | Char Dham Itinerary | Swarnav",
        'meta_description': f"Detailed route guide for Day {day_number} of Swarnav's Char Dham Yatra: {day_data['route_summary']}. Sightseeing, meals, accommodation, and travel guidelines.",
    }
    return render(request, 'yatras/char_dham/day_detail.html', context)

def char_dham_package_details(request):
    """Inclusions, exclusions, conditional services and notes."""
    context = _get_char_dham_base_context(
        active_slug='package-details',
        current_page_label='Package Details',
        prev_nav={'name': 'Itinerary', 'url_name': 'yatras:char_dham_itinerary'},
        next_nav={'name': 'Stay & Travel', 'url_name': 'yatras:char_dham_stay_and_travel'}
    )
    context.update({
        'page_title': 'Package Inclusions & Exclusions | Char Dham Yatra | Swarnav',
        'meta_description': 'Complete details of what is included and excluded in Swarnav’s 13-day Char Dham package, including train transport, meals, and coordinator support.',
        'package_details': PACKAGE_DETAILS,
    })
    return render(request, 'yatras/char_dham/package_details.html', context)

def char_dham_stay_and_travel(request):
    """Accommodation, meals, and transportation arrangements."""
    context = _get_char_dham_base_context(
        active_slug='stay-and-travel',
        current_page_label='Stay & Travel',
        prev_nav={'name': 'Package Details', 'url_name': 'yatras:char_dham_package_details'},
        next_nav={'name': 'Travel Guide', 'url_name': 'yatras:char_dham_travel_guide'}
    )
    context.update({
        'page_title': 'Accommodation & Transport Guide | Char Dham Yatra | Swarnav',
        'meta_description': 'Information regarding economy hotel triple-sharing accommodation, meal plans, train journeys from Surat, and mountain road transportation.',
        'stay_and_travel': STAY_AND_TRAVEL,
    })
    return render(request, 'yatras/char_dham/stay_and_travel.html', context)

def char_dham_travel_guide(request):
    """Health guidelines, required documents, weather advice and packing list."""
    context = _get_char_dham_base_context(
        active_slug='travel-guide',
        current_page_label='Travel Guide',
        prev_nav={'name': 'Stay & Travel', 'url_name': 'yatras:char_dham_stay_and_travel'},
        next_nav={'name': 'Policies', 'url_name': 'yatras:char_dham_policies'}
    )
    context.update({
        'page_title': 'Char Dham Pilgrimage Travel Guide & Preparation | Swarnav',
        'meta_description': 'Essential travel preparation guide for Char Dham Yatra: health and fitness advice, required government registration documents, and packing checklist.',
        'travel_guide': TRAVEL_GUIDE,
    })
    return render(request, 'yatras/char_dham/travel_guide.html', context)

def char_dham_policies(request):
    """Booking terms, payment schedule, and structured cancellation policy."""
    context = _get_char_dham_base_context(
        active_slug='policies',
        current_page_label='Booking & Cancellation Policies',
        prev_nav={'name': 'Travel Guide', 'url_name': 'yatras:char_dham_travel_guide'},
        next_nav={'name': 'Overview', 'url_name': 'yatras:char_dham_overview'}
    )
    context.update({
        'page_title': 'Booking & Cancellation Policy | Char Dham Yatra | Swarnav',
        'meta_description': 'Official booking rules, advance payment terms, and time-based cancellation deduction percentages for Swarnav’s Char Dham Yatra.',
        'policies': POLICIES,
    })
    return render(request, 'yatras/char_dham/policies.html', context)


# --------------------------------------------------------------------------
# Jagannath Puri & Eastern Divine Pilgrimage Views
# --------------------------------------------------------------------------
def _get_puri_base_context(active_slug, current_page_label, prev_nav, next_nav):
    return {
        'package': PURI_PACKAGE,
        'nav_tabs': PURI_NAV_TABS,
        'active_tab': active_slug,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': 'Jagannath Puri Yatra', 'url_name': 'yatras:puri_overview'},
            {'label': current_page_label, 'url_name': None} if active_slug != 'overview' else None
        ],
        'prev_page': prev_nav,
        'next_page': next_nav,
    }

def puri_overview(request):
    """Main overview landing page for Jagannath Puri & Eastern Tour."""
    context = _get_puri_base_context(
        active_slug='overview',
        current_page_label='Overview',
        prev_nav=None,
        next_nav={'name': 'Itinerary', 'url_name': 'yatras:puri_itinerary'}
    )
    context.update({
        'page_title': 'Jagannath Puri 11 Days Tour Package from Surat | Swarnav',
        'meta_description': 'Experience the 11-day spiritual tour from Surat to Puri, Konark, Bhubaneswar, Kolkata, Gangasagar, Deoghar Baidyanath Jyotirlinga, and Varanasi Kashi.',
        'itinerary_summary': PURI_ITINERARY_DAYS[:4],
    })
    return render(request, 'yatras/puri/overview.html', context)

def puri_itinerary(request):
    """Detailed day-by-day 11-day itinerary."""
    context = _get_puri_base_context(
        active_slug='itinerary',
        current_page_label='11-Day Itinerary',
        prev_nav={'name': 'Overview', 'url_name': 'yatras:puri_overview'},
        next_nav={'name': 'Package Details', 'url_name': 'yatras:puri_package_details'}
    )
    context.update({
        'page_title': '11-Day Detailed Itinerary | Jagannath Puri & Eastern Yatra | Swarnav',
        'meta_description': 'Day-by-day itinerary for 11-day Puri, Kolkata, Gangasagar, Deoghar, and Varanasi pilgrimage from Surat.',
        'itinerary_days': PURI_ITINERARY_DAYS,
    })
    return render(request, 'yatras/puri/itinerary.html', context)

def puri_day_detail(request, day_number):
    """Route-detail page for an individual day of the Puri itinerary."""
    if day_number < 1 or day_number > len(PURI_ITINERARY_DAYS):
        raise Http404(f"Itinerary Day {day_number} does not exist in the 11-day Puri schedule.")
    
    day_data = PURI_ITINERARY_DAYS[day_number - 1]
    prev_day = PURI_ITINERARY_DAYS[day_number - 2] if day_number > 1 else None
    next_day = PURI_ITINERARY_DAYS[day_number] if day_number < len(PURI_ITINERARY_DAYS) else None

    context = {
        'package': PURI_PACKAGE,
        'nav_tabs': PURI_NAV_TABS,
        'active_tab': 'itinerary',
        'day': day_data,
        'prev_day': prev_day,
        'next_day': next_day,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': 'Jagannath Puri Yatra', 'url_name': 'yatras:puri_overview'},
            {'label': '11-Day Itinerary', 'url_name': 'yatras:puri_itinerary'},
            {'label': f"Day {day_number}: {day_data['title']}", 'url_name': None}
        ],
        'page_title': f"Day {day_number}: {day_data['title']} | Puri Itinerary | Swarnav",
        'meta_description': f"Route guide for Day {day_number} of Swarnav's Jagannath Puri tour: {day_data['route_summary']}.",
    }
    return render(request, 'yatras/puri/day_detail.html', context)

def puri_package_details(request):
    """Inclusions, exclusions, pricing tiers and notes."""
    context = _get_puri_base_context(
        active_slug='package-details',
        current_page_label='Package Details',
        prev_nav={'name': 'Itinerary', 'url_name': 'yatras:puri_itinerary'},
        next_nav={'name': 'Stay & Travel', 'url_name': 'yatras:puri_stay_and_travel'}
    )
    context.update({
        'page_title': 'Package Inclusions & Pricing | Jagannath Puri Tour | Swarnav',
        'meta_description': 'Complete inclusions, train connectivity, meal plans, and pricing for Swarnav’s 11-day Jagannath Puri and Eastern pilgrimage.',
        'package_details': PURI_PACKAGE_DETAILS,
    })
    return render(request, 'yatras/puri/package_details.html', context)

def puri_stay_and_travel(request):
    """Accommodation, train journeys, and local coach details."""
    context = _get_puri_base_context(
        active_slug='stay-and-travel',
        current_page_label='Stay & Travel',
        prev_nav={'name': 'Package Details', 'url_name': 'yatras:puri_package_details'},
        next_nav={'name': 'Travel Guide', 'url_name': 'yatras:puri_travel_guide'}
    )
    context.update({
        'page_title': 'Stay & Transport Guide | Jagannath Puri Tour | Swarnav',
        'meta_description': 'Hotel standards in Puri, Kolkata, Deoghar, Varanasi and train transport arrangements from Surat and Gujarat.',
        'stay_and_travel': PURI_STAY_AND_TRAVEL,
    })
    return render(request, 'yatras/puri/stay_and_travel.html', context)

def puri_travel_guide(request):
    """Temple rules, dress codes, Gangasagar prep, and packing tips."""
    context = _get_puri_base_context(
        active_slug='travel-guide',
        current_page_label='Travel Guide',
        prev_nav={'name': 'Stay & Travel', 'url_name': 'yatras:puri_stay_and_travel'},
        next_nav={'name': 'Policies', 'url_name': 'yatras:puri_policies'}
    )
    context.update({
        'page_title': 'Pilgrim Guide & Preparation | Jagannath Puri Tour | Swarnav',
        'meta_description': 'Essential travel preparation: Jagannath temple dress code, Gangasagar snan tips, Baidyanath rituals, and packing list.',
        'travel_guide': PURI_TRAVEL_GUIDE,
    })
    return render(request, 'yatras/puri/travel_guide.html', context)

def puri_policies(request):
    """Booking process, advance payment, and cancellation terms."""
    context = _get_puri_base_context(
        active_slug='policies',
        current_page_label='Booking & Policies',
        prev_nav={'name': 'Travel Guide', 'url_name': 'yatras:puri_travel_guide'},
        next_nav={'name': 'Overview', 'url_name': 'yatras:puri_overview'}
    )
    context.update({
        'page_title': 'Booking Terms & Cancellation | Jagannath Puri Tour | Swarnav',
        'meta_description': 'Booking steps, deposit terms, and cancellation policy for Swarnav’s 11-day Jagannath Puri pilgrimage.',
        'policies': PURI_POLICIES,
    })
    return render(request, 'yatras/puri/policies.html', context)

