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
from .data.kashmir import (
    KASHMIR_PACKAGE,
    KASHMIR_ITINERARY_DAYS,
    KASHMIR_PACKAGE_DETAILS,
    KASHMIR_STAY_AND_TRAVEL,
    KASHMIR_TRAVEL_GUIDE,
    KASHMIR_POLICIES,
    KASHMIR_NAV_TABS
)
from .data.rameshwaram import (
    RAMESHWARAM_PACKAGE,
    RAMESHWARAM_ITINERARY_DAYS,
    RAMESHWARAM_PACKAGE_DETAILS,
    RAMESHWARAM_STAY_AND_TRAVEL,
    RAMESHWARAM_TRAVEL_GUIDE,
    RAMESHWARAM_POLICIES,
    RAMESHWARAM_NAV_TABS
)
from .data.kerala import (
    KERALA_PACKAGE,
    KERALA_ITINERARY_DAYS,
    KERALA_PACKAGE_DETAILS,
    KERALA_STAY_AND_TRAVEL,
    KERALA_TRAVEL_GUIDE,
    KERALA_POLICIES,
    KERALA_NAV_TABS
)

def _get_synced_package(static_package, slug):
    """Sync static package definition with dynamic database fields from TourPackage."""
    try:
        from .models import TourPackage
        pkg = dict(static_package)
        db_tour = TourPackage.objects.filter(slug=slug).first()
        if db_tour:
            pkg['is_active'] = db_tour.is_active
            if db_tour.name:
                pkg['name'] = db_tour.name
            if db_tour.subtitle:
                pkg['subtitle'] = db_tour.subtitle
            if db_tour.tagline:
                pkg['tagline'] = db_tour.tagline
            if db_tour.region:
                pkg['region'] = db_tour.region
            if db_tour.duration_days:
                pkg['duration_days'] = db_tour.duration_days
            if db_tour.duration_nights is not None:
                pkg['duration_nights'] = db_tour.duration_nights
            if db_tour.duration_display:
                pkg['duration_display'] = db_tour.duration_display
            elif db_tour.duration_days:
                nights = db_tour.duration_nights if db_tour.duration_nights is not None else max(0, db_tour.duration_days - 1)
                pkg['duration_display'] = f"{db_tour.duration_days} Days / {nights} Nights"
            if db_tour.starting_price:
                pkg['starting_price'] = db_tour.starting_price
            if db_tour.price_display:
                pkg['price_display'] = db_tour.price_display
            if db_tour.price_note:
                pkg['price_note'] = db_tour.price_note
            if db_tour.starting_city:
                pkg['starting_city'] = db_tour.starting_city
            if db_tour.ending_city:
                pkg['ending_city'] = db_tour.ending_city
            if db_tour.origin:
                pkg['origin'] = db_tour.origin
            if db_tour.home_city_connect:
                pkg['home_city_connect'] = db_tour.home_city_connect
            if db_tour.brief_guide:
                pkg['brief_guide'] = db_tour.brief_guide
            if db_tour.departures_summary:
                pkg['departures_summary'] = db_tour.departures_summary
            if db_tour.departures_guidance:
                pkg['departures_guidance'] = db_tour.departures_guidance
            if db_tour.accommodation_summary:
                pkg['accommodation_summary'] = db_tour.accommodation_summary
            if db_tour.meals_summary:
                pkg['meals_summary'] = db_tour.meals_summary
            if db_tour.transport_summary:
                pkg['transport_summary'] = db_tour.transport_summary
            if db_tour.confirmation_note:
                pkg['confirmation_note'] = db_tour.confirmation_note
            if db_tour.gujarat_support_note:
                pkg['gujarat_support_note'] = db_tour.gujarat_support_note
            if db_tour.highlights and isinstance(db_tour.highlights, list) and len(db_tour.highlights) > 0:
                pkg['highlights'] = db_tour.highlights
            if db_tour.image:
                pkg['image'] = db_tour.image
                pkg['image_url'] = db_tour.image_url
            if db_tour.status:
                pkg['status'] = db_tour.status
            if db_tour.status_label:
                pkg['status_label'] = db_tour.status_label
            tour_date_val = db_tour.tour_date or static_package.get('tour_date') or static_package.get('next_batch_short') or static_package.get('next_batch_dates') or ''
            pkg['tour_date'] = tour_date_val
            pkg['next_batch'] = tour_date_val
            pkg['db_tour'] = db_tour
        else:
            pkg['is_active'] = static_package.get('status') == 'active' or static_package.get('is_active', False)
            tour_date_val = static_package.get('tour_date') or static_package.get('next_batch_short') or static_package.get('next_batch_dates') or ''
            pkg['tour_date'] = tour_date_val
            pkg['next_batch'] = tour_date_val
        return pkg
    except Exception:
        return static_package


def _get_dynamic_nav_tabs(base_tabs, duration_days):
    """Adjust the 'itinerary' tab label to reflect dynamic duration."""
    tabs = []
    for tab in base_tabs:
        t = dict(tab)
        if t.get('slug') == 'itinerary' and duration_days:
            t['name'] = f"{duration_days}-Day Itinerary"
        tabs.append(t)
    return tabs


# --------------------------------------------------------------------------
# Char Dham Yatra Views
# --------------------------------------------------------------------------
def _get_char_dham_base_context(active_slug, current_page_label, prev_nav, next_nav):
    pkg = _get_synced_package(CHAR_DHAM_PACKAGE, 'char-dham')
    nav_tabs = _get_dynamic_nav_tabs(CHAR_DHAM_NAV_TABS, pkg.get('duration_days', 13))
    return {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': active_slug,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Char Dham'), 'url_name': 'yatras:char_dham_overview'},
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
    pkg = context['package']
    days_num = pkg.get('duration_days', 13)
    context.update({
        'page_title': f"{pkg.get('name', 'Char Dham Yatra')} {days_num} Days Pilgrimage from Surat | Swarnav",
        'meta_description': f"Explore the sacred {days_num}-day Char Dham Yatra by Swarnav from Surat across Yamunotri, Gangotri, Kedarnath, and Badrinath with arranged travel and stay.",
        'itinerary_summary': ITINERARY_DAYS[:4],
    })
    return render(request, 'yatras/char_dham/overview.html', context)

def char_dham_itinerary(request):
    """Detailed day-by-day itinerary."""
    pkg = _get_synced_package(CHAR_DHAM_PACKAGE, 'char-dham')
    days_num = pkg.get('duration_days', 13)
    days_label = f"{days_num}-Day Itinerary"
    context = _get_char_dham_base_context(
        active_slug='itinerary',
        current_page_label=days_label,
        prev_nav={'name': 'Overview', 'url_name': 'yatras:char_dham_overview'},
        next_nav={'name': 'Package Details', 'url_name': 'yatras:char_dham_package_details'}
    )
    context.update({
        'page_title': f"{days_label} Detailed Itinerary | {pkg.get('name', 'Char Dham Yatra')} | Swarnav",
        'meta_description': f"Day-by-day spiritual itinerary for the {days_num}-day Char Dham Yatra from Surat covering Haridwar, Yamunotri, Gangotri, Kedarnath, and Badrinath.",
        'itinerary_days': ITINERARY_DAYS,
    })
    return render(request, 'yatras/char_dham/itinerary.html', context)

def char_dham_day_detail(request, day_number):
    """Route-detail page for an individual day of the Char Dham itinerary."""
    if day_number < 1 or day_number > len(ITINERARY_DAYS):
        raise Http404(f"Itinerary Day {day_number} does not exist in the Char Dham schedule.")
    
    day_data = ITINERARY_DAYS[day_number - 1]
    prev_day = ITINERARY_DAYS[day_number - 2] if day_number > 1 else None
    next_day = ITINERARY_DAYS[day_number] if day_number < len(ITINERARY_DAYS) else None

    pkg = _get_synced_package(CHAR_DHAM_PACKAGE, 'char-dham')
    nav_tabs = _get_dynamic_nav_tabs(CHAR_DHAM_NAV_TABS, pkg.get('duration_days', 13))
    days_num = pkg.get('duration_days', 13)
    days_label = f"{days_num}-Day Itinerary"

    context = {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': 'itinerary',
        'day': day_data,
        'prev_day': prev_day,
        'next_day': next_day,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Char Dham'), 'url_name': 'yatras:char_dham_overview'},
            {'label': days_label, 'url_name': 'yatras:char_dham_itinerary'},
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
    pkg = _get_synced_package(PURI_PACKAGE, 'jagannath-puri')
    nav_tabs = _get_dynamic_nav_tabs(PURI_NAV_TABS, pkg.get('duration_days', 11))
    return {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': active_slug,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Jagannath Puri Yatra'), 'url_name': 'yatras:puri_overview'},
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
    pkg = context['package']
    days_num = pkg.get('duration_days', 11)
    context.update({
        'page_title': f"{pkg.get('name', 'Jagannath Puri')} {days_num} Days Tour Package from Surat | Swarnav",
        'meta_description': f"Experience the {days_num}-day spiritual tour from Surat: {pkg.get('subtitle', '')}.",
        'itinerary_summary': PURI_ITINERARY_DAYS[:4],
    })
    return render(request, 'yatras/puri/overview.html', context)

def puri_itinerary(request):
    """Detailed day-by-day itinerary."""
    pkg = _get_synced_package(PURI_PACKAGE, 'jagannath-puri')
    days_num = pkg.get('duration_days', 11)
    days_label = f"{days_num}-Day Itinerary"
    context = _get_puri_base_context(
        active_slug='itinerary',
        current_page_label=days_label,
        prev_nav={'name': 'Overview', 'url_name': 'yatras:puri_overview'},
        next_nav={'name': 'Package Details', 'url_name': 'yatras:puri_package_details'}
    )
    context.update({
        'page_title': f"{days_label} | {pkg.get('name', 'Jagannath Puri & Eastern Yatra')} | Swarnav",
        'meta_description': f"Day-by-day itinerary for {days_num}-day {pkg.get('name', 'Puri pilgrimage')} from Surat.",
        'itinerary_days': PURI_ITINERARY_DAYS,
    })
    return render(request, 'yatras/puri/itinerary.html', context)

def puri_day_detail(request, day_number):
    """Route-detail page for an individual day of the Puri itinerary."""
    if day_number < 1 or day_number > len(PURI_ITINERARY_DAYS):
        raise Http404(f"Itinerary Day {day_number} does not exist in the Puri schedule.")
    
    day_data = PURI_ITINERARY_DAYS[day_number - 1]
    prev_day = PURI_ITINERARY_DAYS[day_number - 2] if day_number > 1 else None
    next_day = PURI_ITINERARY_DAYS[day_number] if day_number < len(PURI_ITINERARY_DAYS) else None

    pkg = _get_synced_package(PURI_PACKAGE, 'jagannath-puri')
    nav_tabs = _get_dynamic_nav_tabs(PURI_NAV_TABS, pkg.get('duration_days', 11))
    days_num = pkg.get('duration_days', 11)
    days_label = f"{days_num}-Day Itinerary"

    context = {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': 'itinerary',
        'day': day_data,
        'prev_day': prev_day,
        'next_day': next_day,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Jagannath Puri Yatra'), 'url_name': 'yatras:puri_overview'},
            {'label': days_label, 'url_name': 'yatras:puri_itinerary'},
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


# --------------------------------------------------------------------------
# Kashmir Paradise & Mata Vaishno Devi Tour Views
# --------------------------------------------------------------------------
def _get_kashmir_base_context(active_slug, current_page_label, prev_nav, next_nav):
    pkg = _get_synced_package(KASHMIR_PACKAGE, 'kashmir-paradise')
    nav_tabs = _get_dynamic_nav_tabs(KASHMIR_NAV_TABS, pkg.get('duration_days', 11))
    return {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': active_slug,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Kashmir Tour'), 'url_name': 'yatras:kashmir_overview'},
            {'label': current_page_label, 'url_name': None} if active_slug != 'overview' else None
        ],
        'prev_page': prev_nav,
        'next_page': next_nav,
    }

def kashmir_overview(request):
    """Main overview landing page for Kashmir Paradise & Vaishno Devi Tour."""
    context = _get_kashmir_base_context(
        active_slug='overview',
        current_page_label='Overview',
        prev_nav=None,
        next_nav={'name': 'Itinerary', 'url_name': 'yatras:kashmir_itinerary'}
    )
    pkg = context['package']
    days_num = pkg.get('duration_days', 11)
    context.update({
        'page_title': f"{pkg.get('name', 'Kashmir Paradise & Vaishno Devi')} {days_num} Days Tour Package from Surat | Swarnav",
        'meta_description': f"Experience the {days_num}-day Kashmir & Vaishno Devi tour from Surat: {pkg.get('subtitle', '')}.",
        'itinerary_summary': KASHMIR_ITINERARY_DAYS[:4],
    })
    return render(request, 'yatras/kashmir/overview.html', context)

def kashmir_itinerary(request):
    """Detailed day-by-day itinerary."""
    pkg = _get_synced_package(KASHMIR_PACKAGE, 'kashmir-paradise')
    days_num = pkg.get('duration_days', 11)
    days_label = f"{days_num}-Day Itinerary"
    context = _get_kashmir_base_context(
        active_slug='itinerary',
        current_page_label=days_label,
        prev_nav={'name': 'Overview', 'url_name': 'yatras:kashmir_overview'},
        next_nav={'name': 'Package Details', 'url_name': 'yatras:kashmir_package_details'}
    )
    context.update({
        'page_title': f"{days_label} | {pkg.get('name', 'Kashmir & Vaishno Devi Tour')} | Swarnav",
        'meta_description': f"Day-by-day itinerary for {days_num}-day {pkg.get('name', 'Kashmir tour')} from Surat.",
        'itinerary_days': KASHMIR_ITINERARY_DAYS,
    })
    return render(request, 'yatras/kashmir/itinerary.html', context)

def kashmir_day_detail(request, day_number):
    """Route-detail page for an individual day of the Kashmir itinerary."""
    if day_number < 1 or day_number > len(KASHMIR_ITINERARY_DAYS):
        raise Http404(f"Itinerary Day {day_number} does not exist in the Kashmir schedule.")
    
    day_data = KASHMIR_ITINERARY_DAYS[day_number - 1]
    prev_day = KASHMIR_ITINERARY_DAYS[day_number - 2] if day_number > 1 else None
    next_day = KASHMIR_ITINERARY_DAYS[day_number] if day_number < len(KASHMIR_ITINERARY_DAYS) else None

    pkg = _get_synced_package(KASHMIR_PACKAGE, 'kashmir-paradise')
    nav_tabs = _get_dynamic_nav_tabs(KASHMIR_NAV_TABS, pkg.get('duration_days', 11))
    days_num = pkg.get('duration_days', 11)
    days_label = f"{days_num}-Day Itinerary"

    context = {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': 'itinerary',
        'day': day_data,
        'prev_day': prev_day,
        'next_day': next_day,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Kashmir Tour'), 'url_name': 'yatras:kashmir_overview'},
            {'label': days_label, 'url_name': 'yatras:kashmir_itinerary'},
            {'label': f"Day {day_number}: {day_data['title']}", 'url_name': None}
        ],
        'page_title': f"Day {day_number}: {day_data['title']} | Kashmir Itinerary | Swarnav",
        'meta_description': f"Route guide for Day {day_number} of Swarnav's Kashmir & Vaishno Devi tour: {day_data['route_summary']}.",
    }
    return render(request, 'yatras/kashmir/day_detail.html', context)

def kashmir_package_details(request):
    """Inclusions, exclusions, and travel conditions."""
    context = _get_kashmir_base_context(
        active_slug='package-details',
        current_page_label='Package Details',
        prev_nav={'name': 'Itinerary', 'url_name': 'yatras:kashmir_itinerary'},
        next_nav={'name': 'Stay & Travel', 'url_name': 'yatras:kashmir_stay_and_travel'}
    )
    context.update({
        'page_title': 'Package Inclusions & Pricing | Kashmir Tour | Swarnav',
        'meta_description': 'Complete inclusions, AC train connectivity, meal plans, and pricing for Swarnav’s 11-day Kashmir & Vaishno Devi tour.',
        'package_details': KASHMIR_PACKAGE_DETAILS,
    })
    return render(request, 'yatras/kashmir/package_details.html', context)

def kashmir_stay_and_travel(request):
    """Accommodation, train journeys, and local coach details."""
    context = _get_kashmir_base_context(
        active_slug='stay-and-travel',
        current_page_label='Stay & Travel',
        prev_nav={'name': 'Package Details', 'url_name': 'yatras:kashmir_package_details'},
        next_nav={'name': 'Travel Guide', 'url_name': 'yatras:kashmir_travel_guide'}
    )
    context.update({
        'page_title': 'Stay & Transport Guide | Kashmir Tour | Swarnav',
        'meta_description': 'Hotel standards in Katra, Srinagar, Amritsar, AC train journeys, and mountain transport from Surat and Gujarat.',
        'stay_and_travel': KASHMIR_STAY_AND_TRAVEL,
    })
    return render(request, 'yatras/kashmir/stay_and_travel.html', context)

def kashmir_travel_guide(request):
    """Winter clothing, Vaishno Devi guidelines, Gondola advice, and packing tips."""
    context = _get_kashmir_base_context(
        active_slug='travel-guide',
        current_page_label='Travel Guide',
        prev_nav={'name': 'Stay & Travel', 'url_name': 'yatras:kashmir_stay_and_travel'},
        next_nav={'name': 'Policies', 'url_name': 'yatras:kashmir_policies'}
    )
    context.update({
        'page_title': 'Winter Travel Guide & Preparation | Kashmir Tour | Swarnav',
        'meta_description': 'Essential travel preparation: Kashmir December winter woolens, Vaishno Devi RFID yatra parchi, Gulmarg Gondola tips, and packing list.',
        'travel_guide': KASHMIR_TRAVEL_GUIDE,
    })
    return render(request, 'yatras/kashmir/travel_guide.html', context)

def kashmir_policies(request):
    """Booking process, advance payment, and cancellation terms."""
    context = _get_kashmir_base_context(
        active_slug='policies',
        current_page_label='Booking & Policies',
        prev_nav={'name': 'Travel Guide', 'url_name': 'yatras:kashmir_travel_guide'},
        next_nav={'name': 'Overview', 'url_name': 'yatras:kashmir_overview'}
    )
    context.update({
        'page_title': 'Booking Terms & Cancellation | Kashmir Tour | Swarnav',
        'meta_description': 'Booking steps, advance payment rules, and cancellation policy for Swarnav’s 11-day Kashmir & Vaishno Devi tour.',
        'policies': KASHMIR_POLICIES,
    })
    return render(request, 'yatras/kashmir/policies.html', context)


# --------------------------------------------------------------------------
# Rameshwaram & South Circuit Pilgrimage Tour Views
# --------------------------------------------------------------------------
def _get_rameshwaram_base_context(active_slug, current_page_label, prev_nav, next_nav):
    pkg = _get_synced_package(RAMESHWARAM_PACKAGE, 'rameshwaram-circuit')
    nav_tabs = _get_dynamic_nav_tabs(RAMESHWARAM_NAV_TABS, pkg.get('duration_days', 12))
    return {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': active_slug,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Rameshwaram Tour'), 'url_name': 'yatras:rameshwaram_overview'},
            {'label': current_page_label, 'url_name': None} if active_slug != 'overview' else None
        ],
        'prev_page': prev_nav,
        'next_page': next_nav,
    }

def rameshwaram_overview(request):
    """Main overview landing page for Rameshwaram & South India Circuit."""
    context = _get_rameshwaram_base_context(
        active_slug='overview',
        current_page_label='Overview',
        prev_nav=None,
        next_nav={'name': 'Itinerary', 'url_name': 'yatras:rameshwaram_itinerary'}
    )
    pkg = context['package']
    days_num = pkg.get('duration_days', 12)
    context.update({
        'page_title': f"{pkg.get('name', 'Rameshwaram & South India Pilgrimage Tour')} ({days_num} Days) from Surat | Swarnav",
        'meta_description': f"Sacred {days_num}-day Rameshwaram tour from Surat: {pkg.get('subtitle', '')}.",
        'itinerary_summary': RAMESHWARAM_ITINERARY_DAYS[:4],
    })
    return render(request, 'yatras/rameshwaram/overview.html', context)

def rameshwaram_itinerary(request):
    """Detailed day-by-day itinerary."""
    pkg = _get_synced_package(RAMESHWARAM_PACKAGE, 'rameshwaram-circuit')
    days_num = pkg.get('duration_days', 12)
    days_label = f"{days_num}-Day Itinerary"
    context = _get_rameshwaram_base_context(
        active_slug='itinerary',
        current_page_label=days_label,
        prev_nav={'name': 'Overview', 'url_name': 'yatras:rameshwaram_overview'},
        next_nav={'name': 'Package Details', 'url_name': 'yatras:rameshwaram_package_details'}
    )
    context.update({
        'page_title': f"{days_label} Detailed Itinerary | {pkg.get('name', 'Rameshwaram & South Circuit')} | Swarnav",
        'meta_description': f"Complete {days_num}-day itinerary for {pkg.get('name', 'Rameshwaram pilgrimage')} starting from Surat.",
        'itinerary_days': RAMESHWARAM_ITINERARY_DAYS,
    })
    return render(request, 'yatras/rameshwaram/itinerary.html', context)

def rameshwaram_day_detail(request, day_number):
    """Route-detail page for an individual day of the Rameshwaram itinerary."""
    if day_number < 1 or day_number > len(RAMESHWARAM_ITINERARY_DAYS):
        raise Http404(f"Itinerary Day {day_number} does not exist in the Rameshwaram schedule.")
    
    day_data = RAMESHWARAM_ITINERARY_DAYS[day_number - 1]
    prev_day = RAMESHWARAM_ITINERARY_DAYS[day_number - 2] if day_number > 1 else None
    next_day = RAMESHWARAM_ITINERARY_DAYS[day_number] if day_number < len(RAMESHWARAM_ITINERARY_DAYS) else None

    pkg = _get_synced_package(RAMESHWARAM_PACKAGE, 'rameshwaram-circuit')
    nav_tabs = _get_dynamic_nav_tabs(RAMESHWARAM_NAV_TABS, pkg.get('duration_days', 12))
    days_num = pkg.get('duration_days', 12)
    days_label = f"{days_num}-Day Itinerary"

    context = {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': 'itinerary',
        'day': day_data,
        'prev_day': prev_day,
        'next_day': next_day,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Rameshwaram Tour'), 'url_name': 'yatras:rameshwaram_overview'},
            {'label': days_label, 'url_name': 'yatras:rameshwaram_itinerary'},
            {'label': f"Day {day_number}: {day_data['title']}", 'url_name': None}
        ],
        'page_title': f"Day {day_number}: {day_data['title']} | Rameshwaram Itinerary | Swarnav",
        'meta_description': f"Route guide for Day {day_number} of Swarnav's Rameshwaram & South circuit: {day_data['route_summary']}.",
    }
    return render(request, 'yatras/rameshwaram/day_detail.html', context)

def rameshwaram_package_details(request):
    """Inclusions, exclusions, and travel conditions."""
    context = _get_rameshwaram_base_context(
        active_slug='package-details',
        current_page_label='Package Details',
        prev_nav={'name': 'Itinerary', 'url_name': 'yatras:rameshwaram_itinerary'},
        next_nav={'name': 'Stay & Travel', 'url_name': 'yatras:rameshwaram_stay_and_travel'}
    )
    context.update({
        'page_title': 'Package Inclusions & Pricing (₹30,000) | Rameshwaram Tour | Swarnav',
        'meta_description': 'Transparent package inclusions, AC train transit, pure veg meal plans, and pricing for Swarnav’s 12-day Rameshwaram pilgrimage.',
        'package_details': RAMESHWARAM_PACKAGE_DETAILS,
    })
    return render(request, 'yatras/rameshwaram/package_details.html', context)

def rameshwaram_stay_and_travel(request):
    """Accommodation, train journeys, and local coach details."""
    context = _get_rameshwaram_base_context(
        active_slug='stay-and-travel',
        current_page_label='Stay & Travel',
        prev_nav={'name': 'Package Details', 'url_name': 'yatras:rameshwaram_package_details'},
        next_nav={'name': 'Travel Guide', 'url_name': 'yatras:rameshwaram_travel_guide'}
    )
    context.update({
        'page_title': 'Stay & Transport Guide | Rameshwaram Tour | Swarnav',
        'meta_description': 'Hotel standards in Madurai, Rameshwaram, Kanyakumari, Trivandrum, AC train travel, and AC bus transit from Surat.',
        'stay_and_travel': RAMESHWARAM_STAY_AND_TRAVEL,
    })
    return render(request, 'yatras/rameshwaram/stay_and_travel.html', context)

def rameshwaram_travel_guide(request):
    """Temple dress codes, 22 kund theertham rules, and packing tips."""
    context = _get_rameshwaram_base_context(
        active_slug='travel-guide',
        current_page_label='Travel Guide',
        prev_nav={'name': 'Stay & Travel', 'url_name': 'yatras:rameshwaram_stay_and_travel'},
        next_nav={'name': 'Policies', 'url_name': 'yatras:rameshwaram_policies'}
    )
    context.update({
        'page_title': 'Temple Guidelines & Travel Guide | Rameshwaram Tour | Swarnav',
        'meta_description': 'South Indian temple dress codes (dhoti/veshti & sarees), 22 theerthams snan ritual instructions, and packing essentials for Rameshwaram.',
        'travel_guide': RAMESHWARAM_TRAVEL_GUIDE,
    })
    return render(request, 'yatras/rameshwaram/travel_guide.html', context)

def rameshwaram_policies(request):
    """Booking process, advance payment, and cancellation terms."""
    context = _get_rameshwaram_base_context(
        active_slug='policies',
        current_page_label='Booking & Policies',
        prev_nav={'name': 'Travel Guide', 'url_name': 'yatras:rameshwaram_travel_guide'},
        next_nav={'name': 'Overview', 'url_name': 'yatras:rameshwaram_overview'}
    )
    context.update({
        'page_title': 'Booking Terms & Cancellation | Rameshwaram Tour | Swarnav',
        'meta_description': 'Booking steps, advance payment rules, and cancellation policy for Swarnav’s 12-day Rameshwaram & South Circuit tour.',
        'policies': RAMESHWARAM_POLICIES,
    })
    return render(request, 'yatras/rameshwaram/policies.html', context)


# --------------------------------------------------------------------------
# Kerala Tour (God’s Own Country - 13 Days / 12 Nights) Views
# --------------------------------------------------------------------------
def _get_kerala_base_context(active_slug, current_page_label, prev_nav, next_nav):
    pkg = _get_synced_package(KERALA_PACKAGE, 'kerala-tour')
    nav_tabs = _get_dynamic_nav_tabs(KERALA_NAV_TABS, pkg.get('duration_days', 13))
    return {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': active_slug,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Kerala Tour'), 'url_name': 'yatras:kerala_overview'},
            {'label': current_page_label, 'url_name': None} if active_slug != 'overview' else None
        ],
        'prev_page': prev_nav,
        'next_page': next_nav,
    }

def kerala_overview(request):
    """Main overview landing page for Kerala Grand Tour."""
    context = _get_kerala_base_context(
        active_slug='overview',
        current_page_label='Overview',
        prev_nav=None,
        next_nav={'name': 'Itinerary', 'url_name': 'yatras:kerala_itinerary'}
    )
    pkg = context['package']
    days_num = pkg.get('duration_days', 13)
    context.update({
        'page_title': f"{pkg.get('name', 'Kerala Tour Package')} ({days_num} Days) from Surat | Swarnav",
        'meta_description': f"Unforgettable {days_num}-day Kerala tour from Surat: {pkg.get('subtitle', '')}.",
        'itinerary_summary': KERALA_ITINERARY_DAYS[:4],
    })
    return render(request, 'yatras/kerala/overview.html', context)

def kerala_itinerary(request):
    """Detailed day-by-day itinerary."""
    pkg = _get_synced_package(KERALA_PACKAGE, 'kerala-tour')
    days_num = pkg.get('duration_days', 13)
    days_label = f"{days_num}-Day Itinerary"
    context = _get_kerala_base_context(
        active_slug='itinerary',
        current_page_label=days_label,
        prev_nav={'name': 'Overview', 'url_name': 'yatras:kerala_overview'},
        next_nav={'name': 'Package Details', 'url_name': 'yatras:kerala_package_details'}
    )
    context.update({
        'page_title': f"{days_label} Detailed Itinerary | {pkg.get('name', 'Kerala Grand Tour')} | Swarnav",
        'meta_description': f"Complete day-by-day schedule for {days_num}-day {pkg.get('name', 'Kerala tour')} from Surat.",
        'itinerary_days': KERALA_ITINERARY_DAYS,
    })
    return render(request, 'yatras/kerala/itinerary.html', context)

def kerala_day_detail(request, day_number):
    """Route-detail page for an individual day of the Kerala itinerary."""
    if day_number < 1 or day_number > len(KERALA_ITINERARY_DAYS):
        raise Http404(f"Itinerary Day {day_number} does not exist in the Kerala schedule.")
    
    day_data = KERALA_ITINERARY_DAYS[day_number - 1]
    prev_day = KERALA_ITINERARY_DAYS[day_number - 2] if day_number > 1 else None
    next_day = KERALA_ITINERARY_DAYS[day_number] if day_number < len(KERALA_ITINERARY_DAYS) else None

    pkg = _get_synced_package(KERALA_PACKAGE, 'kerala-tour')
    nav_tabs = _get_dynamic_nav_tabs(KERALA_NAV_TABS, pkg.get('duration_days', 13))
    days_num = pkg.get('duration_days', 13)
    days_label = f"{days_num}-Day Itinerary"

    context = {
        'package': pkg,
        'nav_tabs': nav_tabs,
        'active_tab': 'itinerary',
        'day': day_data,
        'prev_day': prev_day,
        'next_day': next_day,
        'breadcrumbs': [
            {'label': 'Home', 'url_name': 'core:home'},
            {'label': pkg.get('name', 'Kerala Tour'), 'url_name': 'yatras:kerala_overview'},
            {'label': days_label, 'url_name': 'yatras:kerala_itinerary'},
            {'label': f"Day {day_number}: {day_data['title']}", 'url_name': None}
        ],
        'page_title': f"Day {day_number}: {day_data['title']} | Kerala Itinerary | Swarnav",
        'meta_description': f"Route guide for Day {day_number} of Swarnav's Kerala tour: {day_data['route_summary']}.",
    }
    return render(request, 'yatras/kerala/day_detail.html', context)

def kerala_package_details(request):
    """Inclusions, exclusions, and travel conditions."""
    context = _get_kerala_base_context(
        active_slug='package-details',
        current_page_label='Package Details',
        prev_nav={'name': 'Itinerary', 'url_name': 'yatras:kerala_itinerary'},
        next_nav={'name': 'Stay & Travel', 'url_name': 'yatras:kerala_stay_and_travel'}
    )
    context.update({
        'page_title': 'Package Inclusions & Pricing (₹32,000) | Kerala Tour | Swarnav',
        'meta_description': 'Transparent inclusions, AC train connectivity, houseboat stay, pure veg meals, and pricing for Swarnav’s 13-day Kerala tour.',
        'package_details': KERALA_PACKAGE_DETAILS,
    })
    return render(request, 'yatras/kerala/package_details.html', context)

def kerala_stay_and_travel(request):
    """Accommodation, train journeys, and local coach details."""
    context = _get_kerala_base_context(
        active_slug='stay-and-travel',
        current_page_label='Stay & Travel',
        prev_nav={'name': 'Package Details', 'url_name': 'yatras:kerala_package_details'},
        next_nav={'name': 'Travel Guide', 'url_name': 'yatras:kerala_travel_guide'}
    )
    context.update({
        'page_title': 'Stay & Transport Standards | Kerala Tour | Swarnav',
        'meta_description': 'Hotel standards in Munnar, Thekkady, Kovalam, Kochi, deluxe Alleppey houseboat, and AC train transit from Surat.',
        'stay_and_travel': KERALA_STAY_AND_TRAVEL,
    })
    return render(request, 'yatras/kerala/stay_and_travel.html', context)

def kerala_travel_guide(request):
    """Packing advice, temple guidelines, and weather tips."""
    context = _get_kerala_base_context(
        active_slug='travel-guide',
        current_page_label='Travel Guide',
        prev_nav={'name': 'Stay & Travel', 'url_name': 'yatras:kerala_stay_and_travel'},
        next_nav={'name': 'Policies', 'url_name': 'yatras:kerala_policies'}
    )
    context.update({
        'page_title': 'Kerala Travel Guide & Packing Tips | Swarnav',
        'meta_description': 'Packing advice for Munnar hills, Kovalam beaches, Padmanabhaswamy temple dress rules, and weather guidelines for Kerala.',
        'travel_guide': KERALA_TRAVEL_GUIDE,
    })
    return render(request, 'yatras/kerala/travel_guide.html', context)

def kerala_policies(request):
    """Booking process, advance payment, and cancellation terms."""
    context = _get_kerala_base_context(
        active_slug='policies',
        current_page_label='Booking & Policies',
        prev_nav={'name': 'Travel Guide', 'url_name': 'yatras:kerala_travel_guide'},
        next_nav={'name': 'Overview', 'url_name': 'yatras:kerala_overview'}
    )
    context.update({
        'page_title': 'Booking Terms & Cancellation | Kerala Tour | Swarnav',
        'meta_description': 'Booking steps, advance token guidelines, and cancellation deduction schedule for Swarnav’s 13-day Kerala tour.',
        'policies': KERALA_POLICIES,
    })
    return render(request, 'yatras/kerala/policies.html', context)


