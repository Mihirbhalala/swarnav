from django.core.management.base import BaseCommand
from core.models import TourCategory, WhyChooseUs, BookingInquiry, Testimonial
from yatras.models import (
    TourPackage,
    DhamDestination,
    ItineraryDay,
    PackageDetail,
    StayAndTravel,
    TravelGuide,
    PolicyAndFaq
)
from yatras.data.char_dham import (
    CHAR_DHAM_PACKAGE,
    ITINERARY_DAYS as CD_ITINERARY_DAYS,
    PACKAGE_DETAILS as CD_PACKAGE_DETAILS,
    STAY_AND_TRAVEL as CD_STAY_AND_TRAVEL,
    TRAVEL_GUIDE as CD_TRAVEL_GUIDE,
    POLICIES as CD_POLICIES
)
from yatras.data.puri_eastern import (
    PURI_PACKAGE,
    PURI_ITINERARY_DAYS,
    PURI_PACKAGE_DETAILS,
    PURI_STAY_AND_TRAVEL,
    PURI_TRAVEL_GUIDE,
    PURI_POLICIES
)


class Command(BaseCommand):
    help = "Seeds database with all tour circuits, full Char Dham and Jagannath Puri data, and why choose us features."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Beginning database seeding..."))

        # -------------------------------------------------------------
        # 1. Seed Why Choose Us Features
        # -------------------------------------------------------------
        why_swarnav_data = [
            {
                'icon': '🚆',
                'title': 'All Tours Start from Surat + Home City Connect',
                'description': 'All group tours originate from Surat (Gujarat), and we arrange train or flight bookings directly from your home city (Ahmedabad, Vadodara, Rajkot, Mumbai, etc.) to join the group effortlessly.',
                'order': 1
            },
            {
                'icon': '🛡️',
                'title': 'Honest & Transparent Planning',
                'description': 'No hidden charges or unrealistic promises. Clear itinerary, confirmed travel modes, and reliable accommodation details before departure.',
                'order': 2
            },
            {
                'icon': '🍲',
                'title': 'Pure Vegetarian Daily Meals',
                'description': 'Freshly prepared, hygienic, satvik vegetarian lunch and dinner provided throughout the pilgrimage journey according to schedule.',
                'order': 3
            },
            {
                'icon': '👨‍💼',
                'title': 'Dedicated On-Ground Coordinators',
                'description': 'Experienced tour managers accompany our groups from day one to handle logistics, local transport, hotel check-ins, and temple queues.',
                'order': 4
            },
            {
                'icon': '👴',
                'title': 'Special Senior Citizen Care',
                'description': 'Paced travel, assistance with registration, medical tips, and pony/doli coordination for high-altitude treks like Kedarnath & Yamunotri.',
                'order': 5
            },
            {
                'icon': '📝',
                'title': 'Official Yatra Registration Support',
                'description': 'Full guidance and verification for mandatory state pilgrim registration (Uttarakhand Char Dham, Nepal Yatra permits, etc.).',
                'order': 6
            }
        ]

        for item in why_swarnav_data:
            WhyChooseUs.objects.update_or_create(
                title=item['title'],
                defaults=item
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] Seeded {len(why_swarnav_data)} 'Why Choose Us' features."))

        # -------------------------------------------------------------
        # 2. Seed Tour Categories
        # -------------------------------------------------------------
        categories_data = [
            {
                'id_slug': 'north-india',
                'name': 'North India Tours',
                'tagline': 'Himalayan Holy Shrines & Mountain Valleys',
                'badge': 'Sacred Garhwal & Kashmir',
                'description': 'Sacred Himalayan pilgrimages including the world-revered Char Dham Yatra, Panch Kedar trek, and scenic Kashmir valley tours.',
                'order': 1
            },
            {
                'id_slug': 'south-india',
                'name': 'South India Tours',
                'tagline': 'Dravidian Architecture & Tropical Serenity',
                'badge': 'Southern Holy Temples & Coast',
                'description': 'Ancient architectural marvels, sacred ocean tirthas at Rameshwaram and the soothing backwaters and tea hills of Kerala.',
                'order': 2
            },
            {
                'id_slug': 'east-india',
                'name': 'East India Tours',
                'tagline': 'Sacred Jagannath Dham & Ancient Jyotirlingas',
                'badge': 'Eastern Spiritual Circuit',
                'description': 'Devotion to Lord Jagannath on the Bay of Bengal and holy Shiva Jyotirlinga darshan across Odisha and Jharkhand.',
                'order': 3
            },
            {
                'id_slug': 'nepal-tour',
                'name': 'Nepal Tour',
                'tagline': 'The Himalayan Kingdom of Gods',
                'badge': 'International Pilgrimage',
                'description': 'Sacred darshan of Lord Pashupatinath in Kathmandu valley and the liberation pilgrimage to Muktinath in the trans-Himalayan Mustang region.',
                'order': 4
            }
        ]

        cat_objs = {}
        for cat in categories_data:
            obj, _ = TourCategory.objects.update_or_create(
                slug=cat['id_slug'],
                defaults={
                    'name': cat['name'],
                    'tagline': cat['tagline'],
                    'badge': cat['badge'],
                    'description': cat['description'],
                    'order': cat['order']
                }
            )
            cat_objs[cat['id_slug']] = obj
        self.stdout.write(self.style.SUCCESS(f"[OK] Seeded {len(cat_objs)} tour categories."))

        # -------------------------------------------------------------
        # 3. Seed Homepage All 8 Tours
        # -------------------------------------------------------------
        all_tours_summary = [
            # North India
            {
                'category': cat_objs['north-india'],
                'slug': 'char-dham',
                'name': 'Char Dham Yatra',
                'subtitle': 'Yamunotri • Gangotri • Kedarnath • Badrinath',
                'tagline': 'Sacred 13-Day Pilgrimage to the Garhwal Himalayas',
                'region': 'North India (Uttarakhand)',
                'duration_days': 13,
                'duration_nights': 12,
                'duration_display': '13 Days / 12 Nights',
                'starting_price': '₹30,000',
                'price_display': 'Starting from ₹30,000 per person',
                'price_note': 'per person (Triple-sharing)',
                'origin': 'Starts & Ends in Surat, Gujarat',
                'starting_city': 'Surat, Gujarat',
                'ending_city': 'Surat, Gujarat',
                'home_city_connect': 'Train or flight from your home city can be arranged',
                'image': 'images/kedarnath-temple.jpg',
                'status': 'active',
                'status_label': 'Complete Guide Available',
                'is_completed': True,
                'order': 1,
                'highlights': [
                    'All 4 Sacred Dhams darshan in traditional sequence',
                    'Surat to Haridwar return train transport included',
                    'Mountain group coach travel across Uttarakhand',
                    'Economy hotel accommodation with daily meals'
                ],
                'brief_guide': 'The sacred 13-day pilgrimage covering Yamunotri, Gangotri, Kedarnath Jyotirlinga, and Badrinath with on-ground coordinator guidance.'
            },
            {
                'category': cat_objs['north-india'],
                'slug': 'panch-kedar',
                'name': 'Panch Kedar Yatra',
                'subtitle': 'Kedarnath • Tungnath • Rudranath • Madhyamaheshwar • Kalpeshwar',
                'tagline': 'Kedarnath • Tungnath • Rudranath • Madhyamaheshwar • Kalpeshwar',
                'region': 'North India (Uttarakhand)',
                'duration_days': 10,
                'duration_nights': 9,
                'duration_display': '10 Days / 9 Nights',
                'starting_price': '₹26,500',
                'price_display': 'Starting from ₹26,500 per person',
                'price_note': 'per person (Starting price)',
                'origin': 'Starts from Surat (Gujarat) / Haridwar Pickup',
                'starting_city': 'Surat, Gujarat',
                'ending_city': 'Surat, Gujarat',
                'home_city_connect': 'Train or flight from your home city can be arranged',
                'image': 'images/tungnath-temple.jpg',
                'status': 'upcoming',
                'status_label': 'Departures Open for Inquiry',
                'is_completed': False,
                'order': 2,
                'highlights': [
                    'Trek to highest Shiva temple Tungnath (3,680 m)',
                    'Darshan of all 5 sacred Shiva temples in Garhwal',
                    'Experienced mountain trek escorts and porters support',
                    'Clean mountain guest houses & warm satvik meals'
                ],
                'brief_guide': 'A divine trek dedicated to Lord Shiva covering the 5 sacred Himalayan manifestations amidst alpine meadows and glaciers.'
            },
            {
                'category': cat_objs['north-india'],
                'slug': 'kashmir-paradise',
                'name': 'Kashmir Tour (Paradise on Earth)',
                'subtitle': 'Srinagar • Gulmarg • Pahalgam • Sonamarg • Dal Lake',
                'tagline': 'Srinagar • Gulmarg • Pahalgam • Sonamarg • Dal Lake',
                'region': 'North India (Jammu & Kashmir)',
                'duration_days': 7,
                'duration_nights': 6,
                'duration_display': '7 Days / 6 Nights',
                'starting_price': '₹22,500',
                'price_display': 'Starting from ₹22,500 per person',
                'price_note': 'per person (Starting price)',
                'origin': 'Starts from Surat (Gujarat) / Srinagar Hub',
                'starting_city': 'Surat, Gujarat',
                'ending_city': 'Surat, Gujarat',
                'home_city_connect': 'Train or flight from your home city can be arranged',
                'image': 'images/kashmir-valley.jpg',
                'status': 'upcoming',
                'status_label': 'Seasonal Bookings Open',
                'is_completed': False,
                'order': 3,
                'highlights': [
                    'Traditional Dal Lake Houseboat stay with Shikara ride',
                    'Gondola ride at snow-capped Gulmarg',
                    'Scenic Betab & Aru Valleys in Pahalgam',
                    'Comfortable transport & pure vegetarian meal options'
                ],
                'brief_guide': 'Experience the breathtaking valleys, tranquil lakes, pine forests, and saffron fields of Kashmir with family-friendly comfort.'
            },
            # South India
            {
                'category': cat_objs['south-india'],
                'slug': 'rameshwaram-circuit',
                'name': 'Rameshwaram & South Divine Tour',
                'subtitle': 'Madurai • Rameshwaram • Dhanushkodi • Kanyakumari',
                'tagline': 'Madurai • Rameshwaram • Dhanushkodi • Kanyakumari',
                'region': 'South India (Tamil Nadu)',
                'duration_days': 8,
                'duration_nights': 7,
                'duration_display': '8 Days / 7 Nights',
                'starting_price': '₹24,000',
                'price_display': 'Starting from ₹24,000 per person',
                'price_note': 'per person (Starting price)',
                'origin': 'Starts from Surat (Gujarat) / Madurai Hub',
                'starting_city': 'Surat, Gujarat',
                'ending_city': 'Surat, Gujarat',
                'home_city_connect': 'Train or flight from your home city can be arranged',
                'image': 'images/rameshwaram-temple.jpg',
                'status': 'upcoming',
                'status_label': 'Year-Round Departures',
                'is_completed': False,
                'order': 1,
                'highlights': [
                    'Sacred 22 Theerthams holy bath at Ramanathaswamy Temple',
                    'Magnificent Meenakshi Amman Temple in Madurai',
                    'Dhanushkodi Ram Setu point & Kanyakumari Sunset',
                    'Air-conditioned coach & temple darshan guidance'
                ],
                'brief_guide': 'One of India’s original Char Dham shrines where Lord Rama worshipped Shiva, linked with Madurai and Kanyakumari.'
            },
            {
                'category': cat_objs['south-india'],
                'slug': 'kerala-tour',
                'name': 'Kerala Tour (God’s Own Country)',
                'subtitle': 'Munnar • Alleppey • Thekkady • Cochin',
                'tagline': 'Munnar • Alleppey • Thekkady • Cochin',
                'region': 'South India (Kerala)',
                'duration_days': 6,
                'duration_nights': 5,
                'duration_display': '6 Days / 5 Nights',
                'starting_price': '₹19,500',
                'price_display': 'Starting from ₹19,500 per person',
                'price_note': 'per person (Starting price)',
                'origin': 'Starts from Surat (Gujarat) / Cochin Hub',
                'starting_city': 'Surat, Gujarat',
                'ending_city': 'Surat, Gujarat',
                'home_city_connect': 'Train or flight from your home city can be arranged',
                'image': 'images/kerala-backwaters.jpg',
                'status': 'upcoming',
                'status_label': 'Custom Batches Available',
                'is_completed': False,
                'order': 2,
                'highlights': [
                    'Munnar lush tea gardens & misty waterfalls',
                    'Deluxe Alleppey Houseboat cruise in backwaters',
                    'Spice plantation tour in Periyar (Thekkady)',
                    'Family-friendly hotels with Gujarati & North Indian food options'
                ],
                'brief_guide': 'A relaxing nature escape through Kerala’s emerald tea hills, tranquil backwaters, spice gardens, and Arabian sea beaches.'
            },
            # East India
            {
                'category': cat_objs['east-india'],
                'slug': 'jagannath-puri',
                'name': 'Jagannath Puri & Eastern Divine Pilgrimage',
                'subtitle': 'Puri • Konark • Bhubaneswar • Kolkata • Gangasagar • Deoghar • Varanasi',
                'tagline': 'Sacred 11-Day Eastern Circuit Pilgrimage',
                'region': 'East India (Odisha, Bengal, Jharkhand, Kashi)',
                'duration_days': 11,
                'duration_nights': 10,
                'duration_display': '11 Days / 10 Nights',
                'starting_price': '₹24,500',
                'price_display': 'Starting from ₹24,500 per person',
                'price_note': 'per person (Triple-sharing)',
                'origin': 'Starts from Surat (Gujarat) / Home City Connect',
                'starting_city': 'Surat, Gujarat',
                'ending_city': 'Surat, Gujarat',
                'home_city_connect': 'Train or flight from your home city can be arranged',
                'image': 'images/puri-jagannath-temple-main.jpg',
                'status': 'active',
                'status_label': 'Complete Guide Available',
                'is_completed': True,
                'order': 1,
                'highlights': [
                    'Puri Shree Jagannath Temple & Konark Sun Temple',
                    'Kolkata Dakshineswar, Belur Math & Kalighat',
                    'Gangasagar Holy Snan at Ocean Confluence',
                    'Baba Baidyanath Jyotirlinga & Kashi Vishwanath Ganga Aarti'
                ],
                'brief_guide': 'The sacred 11-day eastern circuit covering Puri, Konark, Bhubaneswar, Kolkata, Gangasagar, Deoghar Baidyanath Jyotirlinga, and Varanasi.'
            },
            {
                'category': cat_objs['east-india'],
                'slug': 'jharkhand-tour',
                'name': 'Jharkhand Spiritual Yatra',
                'subtitle': 'Baba Baidyanath Jyotirlinga (Deoghar) • Basukinath • Shikharji',
                'tagline': 'Baba Baidyanath Jyotirlinga (Deoghar) • Basukinath • Shikharji',
                'region': 'East India (Jharkhand)',
                'duration_days': 5,
                'duration_nights': 4,
                'duration_display': '5 Days / 4 Nights',
                'starting_price': '₹14,500',
                'price_display': 'Starting from ₹14,500 per person',
                'price_note': 'per person (Starting price)',
                'origin': 'Starts from Surat (Gujarat) / Jasidih Hub',
                'starting_city': 'Surat, Gujarat',
                'ending_city': 'Surat, Gujarat',
                'home_city_connect': 'Train or flight from your home city can be arranged',
                'image': 'images/baidyanath-temple.jpg',
                'status': 'upcoming',
                'status_label': 'Inquiry Open',
                'is_completed': False,
                'order': 2,
                'highlights': [
                    'Vaidyanath Jyotirlinga darshan at Deoghar',
                    'Holy Basukinath temple worship rituals',
                    'Parasnath Shikharji sacred Jain pilgrim mountain',
                    'Dedicated road vehicles and vegetarian meals'
                ],
                'brief_guide': 'A deeply revered pilgrimage to Lord Shiva’s healing Vaidyanath Jyotirlinga in Deoghar combined with sacred regional shrines.'
            },
            # Nepal
            {
                'category': cat_objs['nepal-tour'],
                'slug': 'nepal-pashupatinath-muktinath',
                'name': 'Pashupatinath & Muktinath Holy Yatra',
                'subtitle': 'Kathmandu • Pokhara • Jomsom • Muktinath Dham',
                'tagline': 'Kathmandu • Pokhara • Jomsom • Muktinath Dham',
                'region': 'Nepal (Himalayas)',
                'duration_days': 8,
                'duration_nights': 7,
                'duration_display': '8 Days / 7 Nights',
                'starting_price': '₹34,500',
                'price_display': 'Starting from ₹34,500 per person',
                'price_note': 'per person (Starting price)',
                'origin': 'Starts from Surat (Gujarat) / Kathmandu Hub',
                'starting_city': 'Surat, Gujarat',
                'ending_city': 'Surat, Gujarat',
                'home_city_connect': 'Train or flight from your home city can be arranged',
                'image': 'images/pashupatinath-temple.jpg',
                'status': 'upcoming',
                'status_label': 'Departures in Apr–Oct',
                'is_completed': False,
                'order': 1,
                'highlights': [
                    'Darshan at UNESCO World Heritage Pashupatinath Temple',
                    'Scenic flight/drive to Jomsom & holy Muktinath 108 water spouts',
                    'Boating on Phewa Lake Pokhara facing Annapurna range',
                    'Special permit handling and senior citizen assistance'
                ],
                'brief_guide': 'The ultimate Himalayan pilgrimage to Pashupatinath and Muktinath Dham, fulfilling sacred vows in the lap of snow peaks.'
            }
        ]

        tour_package_map = {}
        for tour_data in all_tours_summary:
            slug = tour_data['slug']
            package, _ = TourPackage.objects.update_or_create(
                slug=slug,
                defaults=tour_data
            )
            tour_package_map[slug] = package

        self.stdout.write(self.style.SUCCESS(f"[OK] Seeded {len(tour_package_map)} tour packages."))

        # -------------------------------------------------------------
        # 4. Populate Full Char Dham Details
        # -------------------------------------------------------------
        cd_pkg = tour_package_map['char-dham']
        cd_pkg.departures_summary = CHAR_DHAM_PACKAGE.get('departures_summary', '')
        cd_pkg.departures_guidance = CHAR_DHAM_PACKAGE.get('departures_guidance', '')
        cd_pkg.accommodation_summary = CHAR_DHAM_PACKAGE.get('accommodation_summary', '')
        cd_pkg.meals_summary = CHAR_DHAM_PACKAGE.get('meals_summary', '')
        cd_pkg.transport_summary = CHAR_DHAM_PACKAGE.get('transport_summary', '')
        cd_pkg.confirmation_note = CHAR_DHAM_PACKAGE.get('confirmation_note', '')
        cd_pkg.gujarat_support_note = CHAR_DHAM_PACKAGE.get('gujarat_support_note', '')
        cd_pkg.introduction = CHAR_DHAM_PACKAGE.get('introduction', [])
        cd_pkg.route_highlights = CHAR_DHAM_PACKAGE.get('route_highlights', [])
        cd_pkg.save()

        # Seed Char Dham 4 Dhams
        DhamDestination.objects.filter(tour=cd_pkg).delete()
        for dham in CHAR_DHAM_PACKAGE.get('dhams', []):
            DhamDestination.objects.create(
                tour=cd_pkg,
                order=int(dham['order']),
                name=dham['name'],
                significance=dham.get('significance', ''),
                description=dham.get('description', ''),
                highlight=dham.get('highlight', ''),
                image=dham.get('image', '')
            )

        # Seed Char Dham 13 Itinerary Days
        ItineraryDay.objects.filter(tour=cd_pkg).delete()
        for day in CD_ITINERARY_DAYS:
            accom = day.get('accommodation') or {}
            ItineraryDay.objects.create(
                tour=cd_pkg,
                day_number=day['day'],
                title=day.get('title') or '',
                starting_point=day.get('starting_point') or '',
                destination=day.get('destination') or '',
                intro=day.get('intro') or '',
                route_summary=day.get('route_summary') or '',
                night_stay=accom.get('night_stay') or '',
                hotel_type=accom.get('type') or 'Economy Hotel',
                hotel_name=accom.get('hotel_name') or '',
                meals=day.get('meals') or '',
                altitude=day.get('altitude') or '',
                schedule=day.get('schedule') or {},
                darshan_tips=day.get('darshan_tips') or [],
                scenic_points=day.get('scenic_points') or [],
                places_covered=day.get('places_covered') or [],
                route_nodes=day.get('route_nodes') or []
            )

        # Seed Package Details
        PackageDetail.objects.update_or_create(
            tour=cd_pkg,
            defaults={
                'inclusions': CD_PACKAGE_DETAILS.get('inclusions', []),
                'exclusions': CD_PACKAGE_DETAILS.get('exclusions', []),
                'pricing_structure': CD_PACKAGE_DETAILS.get('pricing_structure', []),
                'booking_guidelines': CD_PACKAGE_DETAILS.get('booking_guidelines', []),
                'key_highlights': CD_PACKAGE_DETAILS.get('key_highlights', [])
            }
        )

        # Seed Stay and Travel
        StayAndTravel.objects.update_or_create(
            tour=cd_pkg,
            defaults={
                'hotel_options': CD_STAY_AND_TRAVEL.get('hotel_options', []),
                'vehicle_guidelines': CD_STAY_AND_TRAVEL.get('vehicle_guidelines', []),
                'baggage_rules': CD_STAY_AND_TRAVEL.get('baggage_rules', []),
                'meal_guidelines': CD_STAY_AND_TRAVEL.get('meal_guidelines', [])
            }
        )

        # Seed Travel Guide
        TravelGuide.objects.update_or_create(
            tour=cd_pkg,
            defaults={
                'weather': CD_TRAVEL_GUIDE.get('weather', []),
                'packing_list': CD_TRAVEL_GUIDE.get('packing_list', []),
                'registration_process': CD_TRAVEL_GUIDE.get('registration_process', []),
                'medical_advisory': CD_TRAVEL_GUIDE.get('medical_advisory', []),
                'local_customs': CD_TRAVEL_GUIDE.get('local_customs', []),
                'senior_citizen_tips': CD_TRAVEL_GUIDE.get('senior_citizen_tips', [])
            }
        )

        # Seed Policies & FAQs
        PolicyAndFaq.objects.update_or_create(
            tour=cd_pkg,
            defaults={
                'cancellation_policy': CD_POLICIES.get('cancellation_policy', []),
                'payment_terms': CD_POLICIES.get('payment_terms', []),
                'general_terms': CD_POLICIES.get('general_terms', []),
                'faqs': CD_POLICIES.get('faqs', [])
            }
        )
        self.stdout.write(self.style.SUCCESS("[OK] Seeded full 13-day Char Dham Yatra data."))

        # -------------------------------------------------------------
        # 5. Populate Full Jagannath Puri Details
        # -------------------------------------------------------------
        puri_pkg = tour_package_map['jagannath-puri']
        puri_pkg.departures_summary = PURI_PACKAGE.get('departures_summary', '')
        puri_pkg.departures_guidance = PURI_PACKAGE.get('departures_guidance', '')
        puri_pkg.accommodation_summary = PURI_PACKAGE.get('accommodation_summary', '')
        puri_pkg.meals_summary = PURI_PACKAGE.get('meals_summary', '')
        puri_pkg.transport_summary = PURI_PACKAGE.get('transport_summary', '')
        puri_pkg.confirmation_note = PURI_PACKAGE.get('confirmation_note', '')
        puri_pkg.gujarat_support_note = PURI_PACKAGE.get('gujarat_support_note', '')
        puri_pkg.introduction = PURI_PACKAGE.get('introduction', [])
        puri_pkg.route_highlights = PURI_PACKAGE.get('route_highlights', [])
        puri_pkg.save()

        # Seed Puri Key Shrines
        DhamDestination.objects.filter(tour=puri_pkg).delete()
        for dham in PURI_PACKAGE.get('dhams', []):
            DhamDestination.objects.create(
                tour=puri_pkg,
                order=int(dham['order']),
                name=dham['name'],
                significance=dham.get('significance', ''),
                description=dham.get('description', ''),
                highlight=dham.get('highlight', ''),
                image=dham.get('image', '')
            )

        # Seed Puri 11 Itinerary Days
        ItineraryDay.objects.filter(tour=puri_pkg).delete()
        for day in PURI_ITINERARY_DAYS:
            accom = day.get('accommodation') or {}
            ItineraryDay.objects.create(
                tour=puri_pkg,
                day_number=day['day'],
                title=day.get('title') or '',
                starting_point=day.get('starting_point') or '',
                destination=day.get('destination') or '',
                intro=day.get('intro') or '',
                route_summary=day.get('route_summary') or '',
                night_stay=accom.get('night_stay') or '',
                hotel_type=accom.get('type') or 'Economy Hotel',
                hotel_name=accom.get('hotel_name') or '',
                meals=day.get('meals') or '',
                altitude=day.get('altitude') or '',
                schedule=day.get('schedule') or {},
                darshan_tips=day.get('darshan_tips') or [],
                scenic_points=day.get('scenic_points') or [],
                places_covered=day.get('places_covered') or [],
                route_nodes=day.get('route_nodes') or []
            )

        # Seed Puri Package Details
        PackageDetail.objects.update_or_create(
            tour=puri_pkg,
            defaults={
                'inclusions': PURI_PACKAGE_DETAILS.get('inclusions', []),
                'exclusions': PURI_PACKAGE_DETAILS.get('exclusions', []),
                'pricing_structure': PURI_PACKAGE_DETAILS.get('pricing_structure', []),
                'booking_guidelines': PURI_PACKAGE_DETAILS.get('booking_guidelines', []),
                'key_highlights': PURI_PACKAGE_DETAILS.get('key_highlights', [])
            }
        )

        # Seed Puri Stay and Travel
        StayAndTravel.objects.update_or_create(
            tour=puri_pkg,
            defaults={
                'hotel_options': PURI_STAY_AND_TRAVEL.get('hotel_options', []),
                'vehicle_guidelines': PURI_STAY_AND_TRAVEL.get('vehicle_guidelines', []),
                'baggage_rules': PURI_STAY_AND_TRAVEL.get('baggage_rules', []),
                'meal_guidelines': PURI_STAY_AND_TRAVEL.get('meal_guidelines', [])
            }
        )

        # Seed Puri Travel Guide
        TravelGuide.objects.update_or_create(
            tour=puri_pkg,
            defaults={
                'weather': PURI_TRAVEL_GUIDE.get('weather', []),
                'packing_list': PURI_TRAVEL_GUIDE.get('packing_list', []),
                'registration_process': PURI_TRAVEL_GUIDE.get('registration_process', []),
                'medical_advisory': PURI_TRAVEL_GUIDE.get('medical_advisory', []),
                'local_customs': PURI_TRAVEL_GUIDE.get('local_customs', []),
                'senior_citizen_tips': PURI_TRAVEL_GUIDE.get('senior_citizen_tips', [])
            }
        )

        # Seed Puri Policies & FAQs
        PolicyAndFaq.objects.update_or_create(
            tour=puri_pkg,
            defaults={
                'cancellation_policy': PURI_POLICIES.get('cancellation_policy', []),
                'payment_terms': PURI_POLICIES.get('payment_terms', []),
                'general_terms': PURI_POLICIES.get('general_terms', []),
                'faqs': PURI_POLICIES.get('faqs', [])
            }
        )
        self.stdout.write(self.style.SUCCESS("[OK] Seeded full 11-day Jagannath Puri & Eastern Divine Circuit data."))

        # -------------------------------------------------------------
        # 6. Seed Sample Testimonials & Booking Inquiries
        # -------------------------------------------------------------
        sample_testimonials = [
            {
                'pilgrim_name': 'Rameshbhai & Jayaben Patel',
                'city': 'Surat, Gujarat',
                'yatra_name': 'Char Dham Yatra',
                'rating': 5,
                'review_text': 'Our 13-day Char Dham yatra was exceptionally smooth. Starting from Surat station, everything including train berths, mountain buses, Gujarati satvik food, and hotel stays were handled with utmost devotion and care.',
                'is_featured': True
            },
            {
                'pilgrim_name': 'Dr. Suresh Trivedi',
                'city': 'Ahmedabad, Gujarat',
                'yatra_name': 'Jagannath Puri & Eastern Yatra',
                'rating': 5,
                'review_text': 'The holy darshan of Mahaprabhu Jagannath and Gangasagar snan was truly divine. The coordinator escorted my elderly parents patiently throughout temple queues.',
                'is_featured': True
            }
        ]

        for t in sample_testimonials:
            Testimonial.objects.update_or_create(
                pilgrim_name=t['pilgrim_name'],
                yatra_name=t['yatra_name'],
                defaults=t
            )
        self.stdout.write(self.style.SUCCESS("[OK] Seeded sample testimonials."))

        # Sample Inquiries
        sample_inquiries = [
            {
                'full_name': 'Prakash Shah',
                'phone_number': '+91 98765 43210',
                'email': 'prakash.shah@example.com',
                'city': 'Vadodara',
                'tour_interest': 'Char Dham Yatra (13 Days)',
                'number_of_pilgrims': 4,
                'preferred_travel_date': 'May 2026 Batch',
                'message': 'We are 4 family members including 2 senior citizens. Please share batch dates and pricing details.',
                'status': 'new',
                'admin_notes': 'Called on May 10, shared brochure on WhatsApp.'
            }
        ]

        for inq in sample_inquiries:
            BookingInquiry.objects.update_or_create(
                phone_number=inq['phone_number'],
                tour_interest=inq['tour_interest'],
                defaults=inq
            )
        self.stdout.write(self.style.SUCCESS("\n[SUCCESS] Completed all database seeding successfully!"))
