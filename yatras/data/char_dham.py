"""
Verified source data for Char Dham Yatra.
Strictly extracted from source_content/Char Dham Yatra.docx.
"""

CHAR_DHAM_PACKAGE = {
    'slug': 'char-dham',
    'name': 'Char Dham Yatra',
    'subtitle': 'Yamunotri • Gangotri • Kedarnath • Badrinath',
    'tagline': 'Sacred 13-Day Pilgrimage to the Garhwal Himalayas',
    'duration_days': 13,
    'duration_nights': 12,
    'duration_display': '13 Days / 12 Nights',
    'starting_city': 'Surat, Gujarat',
    'ending_city': 'Surat, Gujarat',
    'starting_price': '₹30,000',
    'price_display': 'Starting from ₹30,000 per person',
    'departures_summary': 'Upcoming Confirmed Batch: 1st Nov – 13th Nov',
    'next_batch_dates': '1st November to 13th November',
    'next_batch_short': '1st Nov – 13th Nov',
    'departures_guidance': 'Next confirmed group departure: 1st November to 13th November. Registrations and seat bookings are now actively open. Limited seats per batch; please contact Swarnav directly to reserve.',
    'upcoming_batches': [
        {
            'batch_dates': '1st November to 13th November',
            'start_date': '1st Nov',
            'end_date': '13th Nov',
            'duration': '13 Days / 12 Nights',
            'origin': 'Surat, Gujarat (All-India connect arranged)',
            'status': 'Bookings Open',
            'badge': 'Confirmed Batch',
            'notes': 'Complete 4-Dham darshan (Yamunotri, Gangotri, Kedarnath Jyotirlinga, Badrinath) with Surat–Haridwar return train.'
        }
    ],
    'accommodation_summary': 'Economy hotels or guest houses (Triple-sharing basis: 1 double bed + 1 extra mattress)',
    'meals_summary': 'Lunch and dinner provided as per itinerary (Breakfast only if included in selected package)',
    'transport_summary': 'Surat–Haridwar–Surat train journey + bus/group vehicle across Uttarakhand mountain routes',
    'confirmation_note': 'Package price, departure schedule, and room availability require final written confirmation before booking.',
    'gujarat_support_note': 'Travellers from anywhere in Gujarat can request transportation arrangements to Surat, where the main journey will begin. Onward transportation from Surat to anywhere in Gujarat can also be arranged upon request (applicable charges communicated separately).',
    
    'introduction': [
        "The Char Dham Yatra is a sacred pilgrimage to four revered Hindu temples nestled in the Garhwal Himalayas of Uttarakhand. The journey traditionally begins at Yamunotri, the source of the River Yamuna, and continues to Gangotri, where the River Ganga is believed to have descended to Earth.",
        "The third destination is Kedarnath, home to one of the twelve Jyotirlingas of Lord Shiva, situated at an altitude of approximately 3,583 metres. The yatra concludes at Badrinath, the sacred abode of Lord Vishnu, surrounded by the magnificent Nar and Narayan mountain ranges.",
        "The Char Dham Yatra remains one of India’s most significant spiritual journeys. According to Hindu tradition, completing the pilgrimage in its prescribed sequence—from west to east—helps devotees seek divine blessings, spiritual purification and the path towards moksha.",
        "Our Char Dham Yatra package is carefully planned so that pilgrims can focus entirely on their spiritual journey. Transportation, accommodation, meals and other essential arrangements are organised in advance, providing a comfortable, safe and worry-free pilgrimage."
    ],

    'dhams': [
        {
            'order': '1',
            'name': 'Yamunotri',
            'significance': 'Source of the Sacred River Yamuna',
            'description': 'The traditional starting point of the pilgrimage in the western Garhwal mountains. Devotees visit the holy Yamunotri Temple and sacred thermal springs.',
            'highlight': 'First Dham',
            'image': 'yamunotri-temple.jpg'
        },
        {
            'order': '2',
            'name': 'Gangotri',
            'significance': 'Descent of the Sacred River Ganga',
            'description': 'Set amidst pine forests and Himalayan peaks along the Bhagirathi River, where Mother Ganga is believed to have descended to Earth.',
            'highlight': 'Second Dham',
            'image': 'gangotri-temple.jpg'
        },
        {
            'order': '3',
            'name': 'Kedarnath',
            'significance': 'Sacred Jyotirlinga of Lord Shiva',
            'description': 'One of the twelve sacred Jyotirlingas, situated at an altitude of approximately 3,583 metres surrounded by snow-capped peaks and glaciers.',
            'highlight': 'Third Dham (Approx. 3,583 m)',
            'image': 'kedarnath-temple.jpg'
        },
        {
            'order': '4',
            'name': 'Badrinath',
            'significance': 'Sacred Abode of Lord Vishnu',
            'description': 'The concluding destination of the Char Dham, nestled in the valley between the Nar and Narayan mountain ranges along the Alaknanda River.',
            'highlight': 'Fourth & Concluding Dham',
            'image': 'badrinath-temple.jpg'
        }
    ],

    'route_highlights': [
        'Surat', 'Haridwar', 'Barkot', 'Yamunotri', 'Uttarkashi', 'Gangotri', 
        'Sonprayag', 'Kedarnath', 'Pipalkoti', 'Badrinath & Mana', 'Rishikesh', 'Haridwar', 'Surat'
    ]
}

ITINERARY_DAYS = [
    {
        'day': 1,
        'title': 'Surat to Haridwar',
        'starting_point': 'Surat',
        'destination': 'Haridwar',
        'intro': 'Begin the sacred Char Dham Yatra with an interstate train journey to Haridwar.',
        'route_summary': 'Surat ➔ Haridwar',
        'route_nodes': [
            {'name': 'Surat', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Haridwar', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Haridwar Ganga Ghats',
                'image': 'haridwar-ganga.jpg',
                'image_alt': 'Holy Ganga River ghats in Haridwar',
                'caption': 'Sacred Ganga Ghats at Haridwar',
                'point': 'Sacred gateway city on the banks of River Ganga.'
            }
        ],
        'accommodation': {
            'night_stay': 'Haridwar',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Lakasha, Valmiki Chowk, Haridwar (or similar property)'
        },
        'meals': 'Dinner'
    },
    {
        'day': 2,
        'title': 'Haridwar to Barkot',
        'starting_point': 'Haridwar',
        'destination': 'Barkot',
        'intro': 'Scenic road journey ascending into the Garhwal foothills towards Barkot.',
        'route_summary': 'Haridwar ➔ Neelkanth Mahadev ➔ Mussoorie ➔ Lakhamandal ➔ Barkot',
        'route_nodes': [
            {'name': 'Haridwar', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Neelkanth Mahadev', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Mussoorie', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Lakhamandal', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Barkot', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Neelkanth Mahadev',
                'image': 'neelkanth-temple.jpg',
                'image_alt': 'Neelkanth Mahadev Temple in forested hills near Rishikesh',
                'caption': 'Neelkanth Mahadev Temple',
                'point': 'Revered Lord Shiva temple nestled in forested mountains.'
            },
            {
                'name': 'Mussoorie',
                'image': 'mussoorie-hills.jpg',
                'image_alt': 'Scenic mountain surroundings of Mussoorie in Uttarakhand',
                'caption': 'Mussoorie Hill Station',
                'point': 'Famous hill station halt offering sweeping Himalayan views.'
            },
            {
                'name': 'Lakhamandal',
                'image': 'lakhamandal-temple.jpg',
                'image_alt': 'Ancient Lakhamandal Temple compound in Uttarakhand',
                'caption': 'Ancient Lakhamandal Temple',
                'point': 'Historic temple complex revered for ancient Shiva lingams.'
            },
            {
                'name': 'Barkot',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Peaceful mountain base town for the Yamunotri trek.'
            }
        ],
        'accommodation': {
            'night_stay': 'Barkot',
            'type': 'Economy Hotel',
            'hotel_name': None
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 3,
        'title': 'Barkot–Yamunotri–Barkot',
        'starting_point': 'Barkot',
        'destination': 'Yamunotri and return to Barkot',
        'intro': 'Trek along the Yamuna valley to seek blessings at Yamunotri Dham.',
        'route_summary': 'Barkot ➔ Janki Chatti ➔ Yamunotri Temple ➔ Barkot',
        'route_nodes': [
            {'name': 'Barkot', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Janki Chatti', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Yamunotri Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Barkot', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Yamunotri Temple',
                'image': 'yamunotri-temple.jpg',
                'image_alt': 'Sacred Yamunotri Temple nestled in the Garhwal mountains',
                'caption': 'Yamunotri Dham Temple',
                'point': 'First sacred Dham and revered holy thermal springs.'
            },
            {
                'name': 'Janki Chatti',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Base point for the Yamunotri mountain trek.'
            }
        ],
        'accommodation': {
            'night_stay': 'Barkot',
            'type': 'Economy Hotel',
            'hotel_name': None
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 4,
        'title': 'Barkot to Uttarkashi',
        'starting_point': 'Barkot',
        'destination': 'Uttarkashi',
        'intro': 'Travel from the Yamuna valley to the sacred town of Uttarkashi.',
        'route_summary': 'Barkot ➔ Gupteshwar Mahadev ➔ Kashi Vishwanath Temple ➔ Uttarkashi',
        'route_nodes': [
            {'name': 'Barkot', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Gupteshwar Mahadev', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Kashi Vishwanath Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Uttarkashi', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Kashi Vishwanath Temple',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Ancient Shiva temple featuring revered Swayambhu Lingam.'
            },
            {
                'name': 'Gupteshwar Mahadev',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Historic cave temple dedicated to Lord Shiva.'
            },
            {
                'name': 'Uttarkashi',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Spiritual riverside town along the holy River Bhagirathi.'
            }
        ],
        'accommodation': {
            'night_stay': 'Uttarkashi',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Himalaya, Uttarkashi (or similar property)'
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 5,
        'title': 'Uttarkashi–Gangotri–Uttarkashi',
        'starting_point': 'Uttarkashi',
        'destination': 'Gangotri and return to Uttarkashi',
        'intro': 'Journey through Harsil Valley for holy darshan at Gangotri Dham.',
        'route_summary': 'Uttarkashi ➔ Gangnani ➔ Harsil Valley ➔ Gangotri Temple ➔ Uttarkashi',
        'route_nodes': [
            {'name': 'Uttarkashi', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Gangnani', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Harsil Valley', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Gangotri Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Uttarkashi', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Gangotri Temple',
                'image': 'gangotri-temple.jpg',
                'image_alt': 'Historic Gangotri Temple surrounded by Himalayan mountains',
                'caption': 'Gangotri Dham Temple',
                'point': 'Second sacred Dham dedicated to Goddess Ganga.'
            },
            {
                'name': 'Harsil Valley',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Scenic valley famous for deodar forests and orchards.'
            },
            {
                'name': 'Gangnani',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Natural thermal hot water spring along the route.'
            }
        ],
        'accommodation': {
            'night_stay': 'Uttarkashi',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Himalaya, Uttarkashi (or similar property)'
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 6,
        'title': 'Uttarkashi to Sonprayag',
        'starting_point': 'Uttarkashi',
        'destination': 'Sonprayag',
        'intro': 'Scenic mountain transit towards Sonprayag base camp.',
        'route_summary': 'Uttarkashi ➔ Dhari Devi Temple ➔ Sonprayag',
        'route_nodes': [
            {'name': 'Uttarkashi', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Dhari Devi Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Sonprayag', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Dhari Devi Temple',
                'image': 'dhari-devi.jpg',
                'image_alt': 'Dhari Devi Temple situated over the Alaknanda river',
                'caption': 'Dhari Devi Temple',
                'point': 'Revered protector deity temple situated over the river.'
            },
            {
                'name': 'Sonprayag Base',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Key base hub for the upcoming Kedarnath trek.'
            }
        ],
        'accommodation': {
            'night_stay': 'Sonprayag',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel GMD, Sonprayag (or similar property)'
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 7,
        'title': 'Sonprayag to Kedarnath',
        'starting_point': 'Sonprayag',
        'destination': 'Kedarnath',
        'intro': 'Trek from Gaurikund to the holy mountain abode of Kedarnath.',
        'route_summary': 'Sonprayag ➔ Gaurikund ➔ Kedarnath Trek ➔ Kedarnath Dham',
        'route_nodes': [
            {'name': 'Sonprayag', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Gaurikund', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Kedarnath Trek Route', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Kedarnath Dham', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Kedarnath Dham',
                'image': 'kedarnath-temple.jpg',
                'image_alt': 'Ancient Kedarnath Temple against snow-covered Himalayan peaks',
                'caption': 'Kedarnath Dham Temple',
                'point': 'Third sacred Dham and holy Shiva Jyotirlinga.'
            },
            {
                'name': 'Gaurikund',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Starting base point for the 16 km Kedarnath trek.'
            }
        ],
        'accommodation': {
            'night_stay': 'Kedarnath',
            'type': 'Economy Hotel',
            'hotel_name': 'Agarwal Bhavan, Kedarnath (or similar basic accommodation)'
        },
        'meals': 'Lunch or packed lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 8,
        'title': 'Kedarnath to Sonprayag',
        'starting_point': 'Kedarnath',
        'destination': 'Sonprayag',
        'intro': 'Morning darshan at Kedarnath followed by descent trek to Sonprayag.',
        'route_summary': 'Kedarnath ➔ Gaurikund ➔ Triyuginarayan Temple ➔ Sonprayag',
        'route_nodes': [
            {'name': 'Kedarnath', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Gaurikund', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Triyuginarayan Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Sonprayag', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Kedarnath Morning Darshan',
                'image': 'kedarnath-temple.jpg',
                'image_alt': 'Morning view of Kedarnath Temple and Himalayan valley',
                'caption': 'Morning Darshan at Kedarnath',
                'point': 'Early morning prayers before starting the return descent.'
            },
            {
                'name': 'Triyuginarayan Temple',
                'image': 'triyuginarayan-temple.jpg',
                'image_alt': 'Ancient Triyuginarayan Temple with eternal flame in Uttarakhand',
                'caption': 'Triyuginarayan Temple',
                'point': 'Historic Vedic wedding temple of Shiva and Parvati.'
            },
            {
                'name': 'Sonprayag Base',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Return to base hotel for evening dinner and rest.'
            }
        ],
        'accommodation': {
            'night_stay': 'Sonprayag',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel GMD, Sonprayag (or similar property)'
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 9,
        'title': 'Sonprayag to Pipalkoti',
        'starting_point': 'Sonprayag',
        'destination': 'Pipalkoti',
        'intro': 'Scenic transit across Garhwal mountain routes to Pipalkoti.',
        'route_summary': 'Sonprayag ➔ Tungnath Temple ➔ Pipalkoti',
        'route_nodes': [
            {'name': 'Sonprayag', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Tungnath Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Pipalkoti', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Tungnath Temple',
                'image': 'tungnath-temple.jpg',
                'image_alt': 'Ancient stone Tungnath Shiva temple in the Garhwal Himalayas',
                'caption': 'Tungnath Temple (3,680m)',
                'point': 'Highest Shiva temple in the world.'
            },
            {
                'name': 'Pipalkoti',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Scenic transit town in the Alaknanda valley.'
            }
        ],
        'accommodation': {
            'night_stay': 'Pipalkoti',
            'type': 'Economy Hotel',
            'hotel_name': 'Kushal Palace, Pipalkoti (or similar property)'
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 10,
        'title': 'Pipalkoti–Badrinath–Pipalkoti',
        'starting_point': 'Pipalkoti',
        'destination': 'Badrinath and return to Pipalkoti',
        'intro': 'Visit holy Badrinath Dham and explore the border village of Mana.',
        'route_summary': 'Pipalkoti ➔ Badrinath Temple ➔ Mana Village ➔ Charan Paduka ➔ Pipalkoti',
        'route_nodes': [
            {'name': 'Pipalkoti', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Badrinath Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Mana Village', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Charan Paduka', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Pipalkoti', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Badrinath Temple',
                'image': 'badrinath-temple.jpg',
                'image_alt': 'Historic Badrinath Temple with Nar-Narayan mountains in background',
                'caption': 'Badrinath Dham Temple',
                'point': 'Fourth and concluding sacred Char Dham.'
            },
            {
                'name': 'Mana Village',
                'image': 'mana-village.jpg',
                'image_alt': 'Mana Village scenic surroundings near Badrinath',
                'caption': 'Mana Border Village',
                'point': 'First Indian village with Vyas Gufa and Bhim Pul.'
            },
            {
                'name': 'Charan Paduka',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Sacred rock bearing Lord Vishnu footprints.'
            }
        ],
        'accommodation': {
            'night_stay': 'Pipalkoti',
            'type': 'Economy Hotel',
            'hotel_name': 'Kushal Palace, Pipalkoti (or similar property)'
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 11,
        'title': 'Pipalkoti to Haridwar',
        'starting_point': 'Pipalkoti',
        'destination': 'Haridwar',
        'intro': 'Descend through river confluences towards Rishikesh and Haridwar.',
        'route_summary': 'Pipalkoti ➔ Rishikesh ➔ Haridwar',
        'route_nodes': [
            {'name': 'Pipalkoti', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Rishikesh', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Haridwar', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Rishikesh',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Spiritual yoga hub on the banks of holy Ganga.'
            },
            {
                'name': 'Haridwar',
                'image': 'haridwar-ganga.jpg',
                'image_alt': 'Holy Ganga River ghats in Haridwar',
                'caption': 'Haridwar Ganga Ghats',
                'point': 'Return to Haridwar for evening rest and darshan.'
            }
        ],
        'accommodation': {
            'night_stay': 'Haridwar',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Lakasha, Haridwar (or similar property)'
        },
        'meals': 'Lunch and dinner; breakfast only if included in selected package'
    },
    {
        'day': 12,
        'title': 'Haridwar to Surat',
        'starting_point': 'Haridwar',
        'destination': 'Surat',
        'intro': 'Board the return train from Haridwar for the journey to Surat.',
        'route_summary': 'Haridwar ➔ Train Journey ➔ Surat',
        'route_nodes': [
            {'name': 'Haridwar', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Train Journey', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Surat', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Haridwar Railway Station',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Board reserved train coach for the journey to Surat.'
            },
            {
                'name': 'Interstate Train Travel',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Comfortable return journey with arranged meal service.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight train journey',
            'type': 'Economy Hotel',
            'hotel_name': 'Overnight train journey as per confirmed schedule'
        },
        'meals': 'Lunch and dinner according to package and train schedule'
    },
    {
        'day': 13,
        'title': 'Arrival in Surat',
        'starting_point': 'Train Arrival',
        'destination': 'Surat',
        'intro': 'Arrive safely in Surat carrying divine blessings of the Char Dham.',
        'route_summary': 'Surat Railway Station ➔ Surat City',
        'route_nodes': [
            {'name': 'Surat Railway Station', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Surat City', 'type': 'Final Destination', 'badge_class': 'destination'}
        ],
        'places_covered': [
            {
                'name': 'Surat Railway Station',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Yatra concludes upon safe arrival in Surat.'
            },
            {
                'name': 'Gujarat Onward Travel',
                'image': None,
                'image_alt': '',
                'caption': '',
                'point': 'Onward connections across Gujarat arranged upon request.'
            }
        ],
        'accommodation': {
            'night_stay': 'Not applicable',
            'type': 'Economy Hotel',
            'hotel_name': 'Not applicable (Yatra concludes upon arrival in Surat)'
        },
        'meals': 'According to arrival time and selected package'
    }
]

PACKAGE_DETAILS = {
    'inclusions': [
        'Surat-to-Haridwar and Haridwar-to-Surat train transportation, if specifically confirmed in the selected package',
        'Transportation between the main destinations in Uttarakhand',
        'Local sightseeing using the tour vehicle wherever road access is available',
        'Economy hotel or guest-house accommodation',
        'Triple-sharing rooms for three travellers (1 double bed + 1 extra mattress)',
        'Lunch and dinner according to the itinerary',
        'Breakfast only when included in the selected package',
        'Services of an experienced tour coordinator',
        'Driver charges, fuel charges, parking charges and applicable road tolls for the main tour vehicle',
        'Assistance with Char Dham Yatra registration',
        'Basic assistance throughout the scheduled journey'
    ],
    'exclusions': [
        'Transportation from the traveller’s home city to Surat, unless specifically arranged',
        'Local shuttle, jeep, taxi or auto-rickshaw charges not included in the main itinerary',
        'Mandatory local jeep charges between Sonprayag and Gaurikund',
        'Helicopter tickets for Kedarnath',
        'Pony, palki, porter or luggage-carrying charges',
        'Private or single-room accommodation',
        'Breakfast unless included in the selected package',
        'Extra meals, snacks, packaged water and beverages',
        'Personal expenses, shopping, laundry and telephone charges',
        'Temple donations, special puja or priority-darshan charges',
        'Entry tickets or activity charges not specifically mentioned',
        'Medical treatment, medicines, ambulance services or evacuation expenses',
        'Travel insurance',
        'Expenses caused by bad weather, landslides, road closures, train delays, government restrictions or other circumstances beyond our control',
        'Any service not specifically mentioned under “Package Inclusions”'
    ],
    'conditional_services': [
        {
            'service': 'Helicopter Tickets for Kedarnath',
            'condition': 'Available only when specifically selected and paid for in advance; strictly subject to ticket availability and mountain weather.'
        },
        {
            'service': 'Private Room Accommodation',
            'condition': 'Arranged upon request, subject to property availability and an additional single-room supplement.'
        },
        {
            'service': 'Breakfast Service',
            'condition': 'Provided only if specifically selected as part of the customized package.'
        },
        {
            'service': 'Pony / Palki / Porter Services',
            'condition': 'Controlled by independent local operators along trekking paths; paid directly by the passenger at local rates.'
        },
        {
            'service': 'Gujarat-Wide Transit to Surat',
            'condition': 'Available upon advance request for pilgrims joining from across Gujarat; applicable transit charges communicated separately.'
        }
    ],
    'important_notes': [
        'The itinerary is flexible and may change because of weather, road conditions, temple timings, government instructions or safety concerns.',
        'All sightseeing visits are subject to available time and accessibility.',
        'Char Dham Yatra registration and valid photo identification are compulsory for every traveller.',
        'Travellers must cooperate with the tour coordinator and follow the scheduled departure times.',
        'Helicopter, pony and palki services are controlled by independent operators and cannot be guaranteed.',
        'The management will make reasonable alternative arrangements if any destination becomes inaccessible.',
        'Travellers should confirm the final train details, hotel list, meal plan and departure schedule before making the full payment.'
    ]
}

STAY_AND_TRAVEL = {
    'accommodation': {
        'category': 'Economy hotels or guest houses',
        'room_sharing': 'Triple-sharing basis, with three travellers accommodated in one room. The room may include one double bed and one extra mattress.',
        'private_room': 'A separate private room can be arranged upon request, subject to availability and an additional charge.',
        'hot_water': 'Hot water will be provided only where it is available at the hotel. At remote destinations, it may be supplied in buckets or during fixed hours.',
        'remote_limitations': 'Hotels and guest houses at Kedarnath and other remote locations offer basic facilities. Luxury services, room heaters, elevators and continuous hot water may not be available.',
        'hotel_changes': 'The listed hotels are preferred options. A similar-category property may be provided if the listed hotel is unavailable.'
    },
    'meals': {
        'overview': 'Wholesome vegetarian meals prepared according to the travel and pilgrimage schedule.',
        'included_meals': 'Lunch and dinner according to the itinerary.',
        'breakfast_rule': 'Breakfast is provided only when explicitly included in the selected package.',
        'trek_days': 'On demanding trek days (such as the Kedarnath trek), lunch or packed lunch will be provided.',
        'extra_refreshments': 'Extra meals, snacks, packaged drinking water, tea, and personal beverages are not included and must be arranged individually.'
    },
    'transportation': {
        'main_mode': 'Train and road transport',
        'train_journey': 'Surat–Haridwar–Surat by train in the class confirmed at the time of booking.',
        'road_transport': 'Bus or another suitable group vehicle will be used for travel between the main destinations in Uttarakhand.',
        'local_transport': 'Shared jeeps or authorised local vehicles may be required on routes where the main tour vehicle is not permitted (such as the Sonprayag–Gaurikund shuttle).',
        'pickup_drop': 'Surat Railway Station or another confirmed location in Surat.',
        'gujarat_travellers': 'Transportation to and from Surat can be arranged upon request for devotees joining from anywhere in Gujarat. Applicable charges will be communicated separately.',
        'vehicle_allocation': 'The vehicle type may change according to the group size, route conditions and government regulations.',
        'travel_time_notice': 'Travel times may vary because of mountain roads, traffic, weather, landslides, road closures and local authority instructions.'
    }
}

TRAVEL_GUIDE = {
    'age_restrictions': {
        'guidance': 'The Yatra is open to travellers of all age groups.',
        'advisory': 'However, due to high altitude, long road journeys and physically demanding treks, children below 10 years, senior citizens above 60 years, pregnant women and travellers with existing medical conditions should consult a doctor before booking.',
        'safety_restriction': 'Participation may be restricted if a traveller’s health condition creates a serious safety risk.'
    },
    'health_requirements': [
        'Travellers should be physically fit enough to manage long road journeys, cold weather, high-altitude conditions and trekking routes.',
        'A medical check-up is strongly recommended before departure.',
        'Travellers with heart disease, asthma, high blood pressure, diabetes, breathing problems or other serious conditions must inform us during booking and carry their prescribed medicines.',
        'A medical fitness certificate may be requested for senior citizens or travellers with pre-existing health conditions.',
        'All travellers must follow government health screening requirements applicable during the Yatra.'
    ],
    'documents_required': [
        'Original Aadhaar card or another valid government-issued photo ID',
        'Char Dham Yatra registration letter with QR code',
        'Two recent passport-size photographs',
        'Tour booking confirmation and payment receipt',
        'Medical fitness certificate, if applicable',
        'Doctor’s prescription for regular medicines',
        'Passport and valid Indian visa for foreign nationals',
        'Emergency contact details',
        'Travel insurance documents, if purchased'
    ],
    'items_to_carry': [
        'Warm clothes, thermals, sweaters and a heavy jacket',
        'Woollen cap, gloves, warm socks and scarf',
        'Raincoat, poncho or umbrella',
        'Comfortable, waterproof trekking shoes',
        'Walking stick for the trekking routes',
        'Personal medicines with prescriptions',
        'Basic first-aid kit and ORS sachets',
        'Reusable water bottle and light energy snacks',
        'Sunscreen, sunglasses and lip balm',
        'Small backpack, torch and power bank',
        'Personal toiletries and hand sanitiser',
        'Valid ID, registration letter and sufficient cash'
    ],
    'packing_advice': 'Please pack lightly and avoid carrying unnecessary heavy luggage.',
    'weather_info': 'Weather in the Himalayan region is cold and unpredictable. Sudden rainfall, snowfall, strong winds and significant temperature changes may occur during the Yatra season. Travellers should carry warm and waterproof clothing regardless of their departure month. Road closures, landslides or bad weather may affect the planned itinerary. Please check the latest government weather advisory before and during the journey.'
}

POLICIES = {
    'booking_conditions': [
        'A 30% advance payment is required to confirm the booking.',
        'The remaining balance must be paid at least 15 days before departure.',
        'Bookings made within 15 days of departure require full payment.',
        'Confirmation is subject to the availability of hotels, vehicles and other services.',
        'Travellers must provide accurate personal, identification and medical information.',
        'Government Yatra registration is compulsory. We can assist with registration, but travellers must provide the required documents on time.',
        'Helicopter tickets, pony, palki and personal expenses are not included unless clearly mentioned in the package.',
        'Hotel rooms and transportation will be provided according to the selected package.',
        'The itinerary may be modified because of weather, road conditions, government instructions, temple timings or safety concerns.',
        'Additional expenses caused by unexpected delays, road closures, natural disasters or medical emergencies shall be paid by the traveller.',
        'The booking is considered confirmed only after the required payment and written confirmation have been received.'
    ],
    'cancellation_brackets': [
        {
            'timeline': '30 days or more before departure',
            'deduction': '10% of total package cost',
            'refund_estimate': '90% of package cost (less non-refundable fees)'
        },
        {
            'timeline': '16 to 29 days before departure',
            'deduction': '25% of total package cost',
            'refund_estimate': '75% of package cost (less non-refundable fees)'
        },
        {
            'timeline': '8 to 15 days before departure',
            'deduction': '50% of total package cost',
            'refund_estimate': '50% of package cost (less non-refundable fees)'
        },
        {
            'timeline': 'Within 7 days of departure',
            'deduction': '100% of total package cost',
            'refund_estimate': 'No refund'
        },
        {
            'timeline': 'No-show or leaving the Yatra early',
            'deduction': '100% of total package cost',
            'refund_estimate': 'No refund for unused services'
        }
    ],
    'cancellation_rules': [
        'Cancellation requests must be submitted in writing through WhatsApp or email.',
        'Non-refundable hotel, transport, permit, registration or ticket charges will be deducted separately, wherever applicable.',
        'Approved refunds will normally be processed within 7–15 working days.',
        'If the Yatra is affected by severe weather, natural disasters, road closures or government restrictions, an alternative date, itinerary adjustment or refund will be offered according to the cancellation terms of the respective service providers.',
        'If we cancel the tour for reasons within our control, travellers may choose an alternative departure or receive a refund of the amount paid.'
    ]
}

CHAR_DHAM_NAV_TABS = [
    {'name': 'Overview', 'url_name': 'yatras:char_dham_overview', 'slug': 'overview'},
    {'name': 'Itinerary', 'url_name': 'yatras:char_dham_itinerary', 'slug': 'itinerary'},
    {'name': 'Package Details', 'url_name': 'yatras:char_dham_package_details', 'slug': 'package-details'},
    {'name': 'Stay & Travel', 'url_name': 'yatras:char_dham_stay_and_travel', 'slug': 'stay-and-travel'},
    {'name': 'Travel Guide', 'url_name': 'yatras:char_dham_travel_guide', 'slug': 'travel-guide'},
    {'name': 'Policies', 'url_name': 'yatras:char_dham_policies', 'slug': 'policies'},
]
