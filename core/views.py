from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

@ensure_csrf_cookie
def home(request):

    """
    Render the homepage for Swarnav Tour & Travels.
    Presents all 4 regional pilgrimage & tour circuits:
    - North India: Char Dham (completed), Panch Kedar, Kashmir Tour
    - South India: Rameshwaram, Kerala Tour
    - East India: Jagannath Puri Odisha, Jharkhand Tour
    - Nepal Tour: Pashupatinath Muktinath Tour

    * All tours have main departures coordinated from Surat (Gujarat), with train or flight
      connectivity arranged from pilgrims' home cities (Ahmedabad, Vadodara, Rajkot, Mumbai, Delhi, etc.).
    """

    tour_categories = [
        {
            'id': 'north-india',
            'name': 'North India Tours',
            'tagline': 'Himalayan Holy Shrines & Mountain Valleys',
            'badge': 'Sacred Garhwal & Kashmir',
            'description': 'Sacred Himalayan pilgrimages including the world-revered Char Dham Yatra, Panch Kedar trek, and scenic Kashmir valley tours.',
            'tours': [
                {
                    'id': 'char-dham',
                    'name': 'Char Dham Yatra',
                    'tagline': 'Yamunotri • Gangotri • Kedarnath • Badrinath',
                    'region': 'North India (Uttarakhand)',
                    'duration_days': 13,
                    'duration_nights': 12,
                    'duration_display': '13 Days / 12 Nights',
                    'starting_price': '₹30,000',
                    'price_note': 'per person (Triple-sharing)',
                    'origin': 'Starts & Ends in Surat, Gujarat',
                    'home_city_connect': 'Train or flight from your home city can be arranged',
                    'image': 'images/kedarnath-temple.jpg',
                    'status': 'active',
                    'status_label': 'Next Batch: 1st Nov – 13th Nov (Open)',
                    'next_batch': '1st Nov – 13th Nov',
                    'is_completed': True,
                    'link': 'yatras:char_dham_overview',
                    'highlights': [
                        'Confirmed Autumn Batch: 1st Nov – 13th Nov',
                        'All 4 Sacred Dhams darshan in traditional sequence',
                        'Surat to Haridwar return train transport included',
                        'Mountain group coach travel across Uttarakhand',
                        'Economy hotel accommodation with daily meals'
                    ],
                    'brief_guide': 'The sacred 13-day pilgrimage covering Yamunotri, Gangotri, Kedarnath Jyotirlinga, and Badrinath with on-ground coordinator guidance. Next confirmed batch: 1st Nov – 13th Nov.'
                },
                {
                    'id': 'panch-kedar',
                    'name': 'Panch Kedar Yatra',
                    'tagline': 'Kedarnath • Tungnath • Rudranath • Madhyamaheshwar • Kalpeshwar',
                    'region': 'North India (Uttarakhand)',
                    'duration_days': 10,
                    'duration_nights': 9,
                    'duration_display': '10 Days / 9 Nights',
                    'starting_price': '₹26,500',
                    'price_note': 'per person (Starting price)',
                    'origin': 'Starts from Surat (Gujarat) / Haridwar Pickup',
                    'home_city_connect': 'Train or flight from your home city can be arranged',
                    'image': 'images/tungnath-temple.jpg',
                    'status': 'upcoming',
                    'status_label': 'Departures Open for Inquiry',
                    'is_completed': False,
                    'highlights': [
                        'Trek to highest Shiva temple Tungnath (3,680 m)',
                        'Darshan of all 5 sacred Shiva temples in Garhwal',
                        'Experienced mountain trek escorts and porters support',
                        'Clean mountain guest houses & warm satvik meals'
                    ],
                    'brief_guide': 'A divine trek dedicated to Lord Shiva covering the 5 sacred Himalayan manifestations amidst alpine meadows and glaciers.'
                },
                {
                    'id': 'kashmir-paradise',
                    'name': 'Kashmir Tour (Paradise on Earth)',
                    'tagline': 'Srinagar • Gulmarg • Pahalgam • Sonamarg • Dal Lake',
                    'region': 'North India (Jammu & Kashmir)',
                    'duration_days': 7,
                    'duration_nights': 6,
                    'duration_display': '7 Days / 6 Nights',
                    'starting_price': '₹22,500',
                    'price_note': 'per person (Starting price)',
                    'origin': 'Starts from Surat (Gujarat) / Srinagar Hub',
                    'home_city_connect': 'Train or flight from your home city can be arranged',
                    'image': 'images/kashmir-valley.jpg',
                    'status': 'upcoming',
                    'status_label': 'Seasonal Bookings Open',
                    'is_completed': False,
                    'highlights': [
                        'Traditional Dal Lake Houseboat stay with Shikara ride',
                        'Gondola ride at snow-capped Gulmarg',
                        'Scenic Betab & Aru Valleys in Pahalgam',
                        'Comfortable transport & pure vegetarian meal options'
                    ],
                    'brief_guide': 'Experience the breathtaking valleys, tranquil lakes, pine forests, and saffron fields of Kashmir with family-friendly comfort.'
                }
            ]
        },
        {
            'id': 'south-india',
            'name': 'South India Tours',
            'tagline': 'Dravidian Architecture & Tropical Serenity',
            'badge': 'Southern Holy Temples & Coast',
            'description': 'Ancient architectural marvels, sacred ocean tirthas at Rameshwaram and the soothing backwaters and tea hills of Kerala.',
            'tours': [
                {
                    'id': 'rameshwaram-circuit',
                    'name': 'Rameshwaram & South Divine Tour',
                    'tagline': 'Madurai • Rameshwaram • Dhanushkodi • Kanyakumari',
                    'region': 'South India (Tamil Nadu)',
                    'duration_days': 8,
                    'duration_nights': 7,
                    'duration_display': '8 Days / 7 Nights',
                    'starting_price': '₹24,000',
                    'price_note': 'per person (Starting price)',
                    'origin': 'Starts from Surat (Gujarat) / Madurai Hub',
                    'home_city_connect': 'Train or flight from your home city can be arranged',
                    'image': 'images/rameshwaram-temple.jpg',
                    'status': 'upcoming',
                    'status_label': 'Year-Round Departures',
                    'is_completed': False,
                    'highlights': [
                        'Sacred 22 Theerthams holy bath at Ramanathaswamy Temple',
                        'Magnificent Meenakshi Amman Temple in Madurai',
                        'Dhanushkodi Ram Setu point & Kanyakumari Sunset',
                        'Air-conditioned coach & temple darshan guidance'
                    ],
                    'brief_guide': 'One of India’s original Char Dham shrines where Lord Rama worshipped Shiva, linked with Madurai and Kanyakumari.'
                },
                {
                    'id': 'kerala-tour',
                    'name': 'Kerala Tour (God’s Own Country)',
                    'tagline': 'Munnar • Alleppey • Thekkady • Cochin',
                    'region': 'South India (Kerala)',
                    'duration_days': 6,
                    'duration_nights': 5,
                    'duration_display': '6 Days / 5 Nights',
                    'starting_price': '₹19,500',
                    'price_note': 'per person (Starting price)',
                    'origin': 'Starts from Surat (Gujarat) / Cochin Hub',
                    'home_city_connect': 'Train or flight from your home city can be arranged',
                    'image': 'images/kerala-backwaters.jpg',
                    'status': 'upcoming',
                    'status_label': 'Custom Batches Available',
                    'is_completed': False,
                    'highlights': [
                        'Munnar lush tea gardens & misty waterfalls',
                        'Deluxe Alleppey Houseboat cruise in backwaters',
                        'Spice plantation tour in Periyar (Thekkady)',
                        'Family-friendly hotels with Gujarati & North Indian food options'
                    ],
                    'brief_guide': 'A relaxing nature escape through Kerala’s emerald tea hills, tranquil backwaters, spice gardens, and Arabian sea beaches.'
                }
            ]
        },
        {
            'id': 'east-india',
            'name': 'East India Tours',
            'tagline': 'Sacred Jagannath Dham & Ancient Jyotirlingas',
            'badge': 'Eastern Spiritual Circuit',
            'description': 'Devotion to Lord Jagannath on the Bay of Bengal and holy Shiva Jyotirlinga darshan across Odisha and Jharkhand.',
            'tours': [
                {
                    'id': 'jagannath-puri',
                    'name': 'Jagannath Puri & Eastern Divine Pilgrimage',
                    'tagline': 'Puri • Konark • Bhubaneswar • Kolkata • Gangasagar • Deoghar • Varanasi',
                    'region': 'East India (Odisha, Bengal, Jharkhand, Kashi)',
                    'duration_days': 11,
                    'duration_nights': 10,
                    'duration_display': '11 Days / 10 Nights',
                    'starting_price': '₹24,500',
                    'price_note': 'per person (Triple-sharing)',
                    'origin': 'Starts from Surat (Gujarat) / Home City Connect',
                    'home_city_connect': 'Train or flight from your home city can be arranged',
                    'image': 'images/puri-jagannath-temple-main.jpg',
                    'status': 'active',
                    'status_label': 'Complete Guide Available',
                    'is_completed': True,
                    'link': 'yatras:puri_overview',
                    'highlights': [
                        'Puri Shree Jagannath Temple & Konark Sun Temple',
                        'Kolkata Dakshineswar, Belur Math & Kalighat',
                        'Gangasagar Holy Snan at Ocean Confluence',
                        'Baba Baidyanath Jyotirlinga & Kashi Vishwanath Ganga Aarti'
                    ],
                    'brief_guide': 'The sacred 11-day eastern circuit covering Puri, Konark, Bhubaneswar, Kolkata, Gangasagar, Deoghar Baidyanath Jyotirlinga, and Varanasi.'
                },
                {
                    'id': 'jharkhand-tour',
                    'name': 'Jharkhand Spiritual Yatra',
                    'tagline': 'Baba Baidyanath Jyotirlinga (Deoghar) • Basukinath • Shikharji',
                    'region': 'East India (Jharkhand)',
                    'duration_days': 5,
                    'duration_nights': 4,
                    'duration_display': '5 Days / 4 Nights',
                    'starting_price': '₹14,500',
                    'price_note': 'per person (Starting price)',
                    'origin': 'Starts from Surat (Gujarat) / Jasidih Hub',
                    'home_city_connect': 'Train or flight from your home city can be arranged',
                    'image': 'images/baidyanath-temple.jpg',
                    'status': 'upcoming',
                    'status_label': 'Inquiry Open',
                    'is_completed': False,
                    'highlights': [
                        'Vaidyanath Jyotirlinga darshan at Deoghar',
                        'Holy Basukinath temple worship rituals',
                        'Parasnath Shikharji sacred Jain pilgrim mountain',
                        'Dedicated road vehicles and vegetarian meals'
                    ],
                    'brief_guide': 'A deeply revered pilgrimage to Lord Shiva’s healing Vaidyanath Jyotirlinga in Deoghar combined with sacred regional shrines.'
                }
            ]
        },
        {
            'id': 'nepal-tour',
            'name': 'Nepal Tour',
            'tagline': 'The Himalayan Kingdom of Gods',
            'badge': 'International Pilgrimage',
            'description': 'Sacred darshan of Lord Pashupatinath in Kathmandu valley and the liberation pilgrimage to Muktinath in the trans-Himalayan Mustang region.',
            'tours': [
                {
                    'id': 'nepal-pashupatinath-muktinath',
                    'name': 'Pashupatinath & Muktinath Holy Yatra',
                    'tagline': 'Kathmandu • Pokhara • Jomsom • Muktinath Dham',
                    'region': 'Nepal (Himalayas)',
                    'duration_days': 8,
                    'duration_nights': 7,
                    'duration_display': '8 Days / 7 Nights',
                    'starting_price': '₹34,500',
                    'price_note': 'per person (Starting price)',
                    'origin': 'Starts from Surat (Gujarat) / Kathmandu Hub',
                    'home_city_connect': 'Train or flight from your home city can be arranged',
                    'image': 'images/pashupatinath-temple.jpg',
                    'status': 'upcoming',
                    'status_label': 'Departures in Apr–Oct',
                    'is_completed': False,
                    'highlights': [
                        'Darshan at UNESCO World Heritage Pashupatinath Temple',
                        'Scenic flight/drive to Jomsom & holy Muktinath 108 water spouts',
                        'Boating on Phewa Lake Pokhara facing Annapurna range',
                        'Special permit handling and senior citizen assistance'
                    ],
                    'brief_guide': 'The ultimate Himalayan pilgrimage to Pashupatinath and Muktinath Dham, fulfilling sacred vows in the lap of snow peaks.'
                }
            ]
        }
    ]

    total_tours = sum(len(cat['tours']) for cat in tour_categories)

    why_swarnav = [
        {
            'icon': '🚆',
            'title': 'All Tours Start from Surat + Home City Connect',
            'description': 'All group tours originate from Surat (Gujarat), and we arrange train or flight bookings directly from your home city (Ahmedabad, Vadodara, Rajkot, Mumbai, etc.) to join the group effortlessly.'
        },
        {
            'icon': '🛡️',
            'title': 'Honest & Transparent Planning',
            'description': 'No hidden charges or unrealistic promises. Clear itinerary, confirmed travel modes, and reliable accommodation details before departure.'
        },
        {
            'icon': '🍲',
            'title': 'Pure Vegetarian Daily Meals',
            'description': 'Freshly prepared, hygienic, satvik vegetarian lunch and dinner provided throughout the pilgrimage journey according to schedule.'
        },
        {
            'icon': '👨‍💼',
            'title': 'Dedicated On-Ground Coordinators',
            'description': 'Experienced tour managers accompany our groups from day one to handle logistics, local transport, hotel check-ins, and temple queues.'
        },
        {
            'icon': '👴',
            'title': 'Special Senior Citizen Care',
            'description': 'Paced travel, assistance with registration, medical tips, and pony/doli coordination for high-altitude treks like Kedarnath & Yamunotri.'
        },
        {
            'icon': '📝',
            'title': 'Official Yatra Registration Support',
            'description': 'Full guidance and verification for mandatory state pilgrim registration (Uttarakhand Char Dham, Nepal Yatra permits, etc.).'
        }
    ]

    context = {
        'page_title': 'Swarnav Tour & Travels | Spiritual Pilgrimages & Nature Tours Across India & Nepal',
        'meta_description': 'Swarnav Tour & Travels organizes trusted spiritual pilgrimages and tours across North India (Char Dham, Panch Kedar, Kashmir), South India (Rameshwaram, Kerala), East India (Puri, Jharkhand), and Nepal (Pashupatinath, Muktinath). Departures from Surat & train/flight arranged from your home city.',
        'tour_categories': tour_categories,
        'total_tours': total_tours,
        'why_swarnav': why_swarnav,
        'inquiry_form': InquiryForm(),
    }
    return render(request, 'core/home.html', context)


import json
import logging
import urllib.parse
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Inquiry
from .forms import InquiryForm
from .email_utils import send_admin_inquiry_notification

logger = logging.getLogger(__name__)



def build_whatsapp_url(inquiry):
    """
    Construct a URL-encoded WhatsApp link to Swarnav's verified business number.
    Contains inquiry reference ID, customer details, selected tour, and notes.
    """
    business_number = "919586825353"
    tour_name = inquiry.get_tour_display()
    ref_id = f"SW-INQ-{inquiry.id:04d}"

    lines = [
        "Namaste Swarnav Tour & Travels,",
        "",
        f"*New Yatra Inquiry (Ref: #{ref_id})*",
        f"• *Tour:* {tour_name}",
        f"• *Name:* {inquiry.name}",
        f"• *Phone:* {inquiry.phone}",
    ]
    if inquiry.departure_city:
        lines.append(f"• *Departure City:* {inquiry.departure_city}")
    if inquiry.total_pilgrims:
        lines.append(f"• *Total Pilgrims:* {inquiry.total_pilgrims}")
    if inquiry.message:
        lines.append(f"• *Requirements / Notes:* {inquiry.message}")

    lines.append("")
    lines.append("Please share departure batch dates and booking details. Har Har Mahadev!")

    full_message = "\n".join(lines)
    encoded_message = urllib.parse.quote(full_message)
    return f"https://wa.me/{business_number}?text={encoded_message}"


@require_POST
def submit_inquiry(request):
    """
    Securely validate and save customer inquiry to database.
    Requires CSRF token and valid POST request.
    Only after successful database save, generates WhatsApp link.
    Supports both AJAX JSON payloads and standard multipart/urlencoded form submissions.
    """
    is_json = request.content_type == 'application/json' or request.headers.get('x-requested-with') == 'XMLHttpRequest'

    if request.content_type == 'application/json':
        try:
            raw_data = json.loads(request.body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON format received.'
            }, status=400)
    else:
        raw_data = request.POST.dict()

    # Map form fields if submitted with legacy or alternative field names
    form_payload = {
        'tour': raw_data.get('tour') or raw_data.get('tour_interest') or 'char-dham',
        'name': raw_data.get('name') or raw_data.get('full_name') or '',
        'phone': raw_data.get('phone') or raw_data.get('phone_number') or '',
        'departure_city': raw_data.get('departure_city') or raw_data.get('city') or '',
        'total_pilgrims': raw_data.get('total_pilgrims') or raw_data.get('pilgrim_count') or raw_data.get('number_of_pilgrims') or '',
        'message': raw_data.get('message') or raw_data.get('notes') or '',
        'consent_given': raw_data.get('consent_given') in [True, 'true', 'True', '1', 'on', True],
    }

    # If empty string passed for total_pilgrims, make it None so integer clean works
    if form_payload['total_pilgrims'] == '' or form_payload['total_pilgrims'] is None:
        form_payload['total_pilgrims'] = None

    form = InquiryForm(data=form_payload)

    if form.is_valid():
        try:
            inquiry = form.save(commit=True)

            # Trigger instant admin email notification
            try:
                base_site_url = request.build_absolute_uri('/')[:-1]
                send_admin_inquiry_notification(inquiry, site_url=base_site_url)
            except Exception as mail_err:
                logger.warning("Could not dispatch admin notification email: %s", mail_err)

            whatsapp_url = build_whatsapp_url(inquiry)
            success_url = reverse('core:inquiry_success', args=[inquiry.id])

            if is_json:
                return JsonResponse({
                    'success': True,
                    'inquiry_id': inquiry.id,
                    'inquiry_ref': f"SW-INQ-{inquiry.id:04d}",
                    'whatsapp_url': whatsapp_url,
                    'success_url': success_url,
                    'message': 'Har Har Mahadev! Your inquiry has been saved successfully.'
                })
            else:
                return redirect('core:inquiry_success', inquiry_id=inquiry.id)


        except Exception as exc:
            logger.exception("Database error while saving Inquiry: %s", exc)
            error_msg = "We encountered a temporary server issue while recording your inquiry. Please try again or contact us directly on WhatsApp."
            if is_json:
                return JsonResponse({
                    'success': False,
                    'error': error_msg
                }, status=500)
            else:
                return render(request, 'core/home.html', {
                    'inquiry_error': error_msg,
                    'inquiry_form': form,
                }, status=500)

    else:
        # Validation failed - format errors
        errors_dict = {}
        for field, error_list in form.errors.items():
            errors_dict[field] = [str(err) for err in error_list]

        if is_json:
            first_err = next(iter(form.errors.values()))[0] if form.errors else "Please check your entries."
            return JsonResponse({
                'success': False,
                'error': str(first_err),
                'errors': errors_dict
            }, status=400)
        else:
            return render(request, 'core/home.html', {
                'inquiry_form': form,
            }, status=400)


def inquiry_success(request, inquiry_id):
    """
    Display safe confirmation page after inquiry is saved in database.
    Provides explicit 'Continue to WhatsApp' CTA without triggering popup blockers.
    """
    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)
    whatsapp_url = build_whatsapp_url(inquiry)
    return render(request, 'core/inquiry_success.html', {
        'inquiry': inquiry,
        'inquiry_ref': f"SW-INQ-{inquiry.id:04d}",
        'whatsapp_url': whatsapp_url,
        'page_title': f'Inquiry Received #{inquiry.id:04d} | Swarnav Tour & Travels',
    })


def inquiry_download_pdf(request, inquiry_id):
    """
    Render a clean printable / downloadable PDF inquiry summary slip.
    Accessible by the customer after submission and by administrators.
    """
    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)
    whatsapp_url = build_whatsapp_url(inquiry)
    return render(request, 'core/inquiry_pdf.html', {
        'inquiry': inquiry,
        'inquiry_ref': f"SW-INQ-{inquiry.id:04d}",
        'whatsapp_url': whatsapp_url,
    })


from django.contrib.admin.views.decorators import staff_member_required
from .export_utils import export_inquiries_to_excel_response


@staff_member_required
def inquiry_export_excel(request):
    """
    Staff-only endpoint to export all or filtered inquiries to an Excel/CSV spreadsheet.
    """
    status_filter = request.GET.get('status')
    tour_filter = request.GET.get('tour')

    queryset = Inquiry.objects.all().order_by('-created_at')
    if status_filter:
        queryset = queryset.filter(status=status_filter)
    if tour_filter:
        queryset = queryset.filter(tour=tour_filter)

    return export_inquiries_to_excel_response(queryset, filename_prefix="swarnav_all_inquiries")


from django.utils import timezone


@staff_member_required
def inquiry_master_pdf(request):
    """
    Staff-only endpoint to view/print master inquiries register report as a PDF document.
    """
    inquiries = Inquiry.objects.all().order_by('-created_at')
    total_count = inquiries.count()
    new_count = inquiries.filter(status='new').count()
    contacted_count = inquiries.filter(status__in=['contacted', 'follow_up']).count()
    converted_count = inquiries.filter(status='converted').count()

    return render(request, 'admin/inquiries_master_pdf.html', {
        'inquiries': inquiries,
        'total_count': total_count,
        'new_count': new_count,
        'contacted_count': contacted_count,
        'converted_count': converted_count,
        'now': timezone.now(),
    })


@csrf_exempt
@require_POST
def ai_chat_api(request):
    """
    Asynchronous endpoint for Swarnav AI Pilgrimage Assistant.
    Processes user query with Hybrid RAG + Gemini Agent Tools,
    persists conversational session memory, and returns rich reply payload.
    """
    try:
        if request.content_type == 'application/json':
            try:
                body = json.loads(request.body.decode('utf-8'))
            except (ValueError, UnicodeDecodeError):
                return JsonResponse({'success': False, 'error': 'Invalid JSON format.'}, status=400)
        else:
            body = request.POST.dict()

        user_message = (body.get('message') or body.get('prompt') or '').strip()
        if not user_message:
            return JsonResponse({'success': False, 'error': 'Message cannot be empty.'}, status=400)

        # Retrieve or initialize session history
        history = request.session.get('ai_chat_history', [])
        if not isinstance(history, list):
            history = []

        from core.ai.agent_service import execute_agent_chat
        result = execute_agent_chat(user_message, session_history=history)

        # Update session history (keep last 12 turns to preserve context without bloat)
        history.append({"sender": "user", "text": user_message})
        history.append({"sender": "bot", "text": result.get("reply", "")})
        request.session['ai_chat_history'] = history[-12:]
        request.session.modified = True

        return JsonResponse({
            'success': True,
            'reply': result.get('reply', ''),
            'action_card': result.get('action_card'),
            'suggested_questions': result.get('suggested_questions', []),
            'tools_used': result.get('tools_used', [])
        })
    except Exception as exc:
        logger.exception("AI Chat API encountered an error: %s", exc)
        return JsonResponse({
            'success': False,
            'error': 'Our AI Assistant encountered a temporary server error. Please try again or contact our team via WhatsApp.'
        }, status=500)


@csrf_exempt
@require_POST
def ai_reset_api(request):
    """Reset the current user's conversational session memory."""
    request.session['ai_chat_history'] = []
    request.session.modified = True
    return JsonResponse({'success': True, 'message': 'Chat session reset successfully.'})



