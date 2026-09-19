"""
Verified source data for Jagannath Puri & Eastern Divine Pilgrimage Tour.
Short, concise, point-wise pilgrimage structure matching Char Dham Yatra format.
"""

PURI_PACKAGE = {
    'slug': 'puri-eastern-pilgrimage',
    'name': 'Jagannath Puri & Eastern Divine Pilgrimage',
    'subtitle': 'Puri • Konark • Bhubaneswar • Kolkata • Gangasagar • Deoghar (Baidyanath) • Varanasi (Kashi)',
    'tagline': 'Sacred 11-Day Grand Pilgrimage across Odisha, Bengal, Jharkhand & Kashi',
    'duration_days': 11,
    'duration_nights': 10,
    'duration_display': '11 Days / 10 Nights',
    'starting_city': 'Surat, Gujarat',
    'ending_city': 'Surat, Gujarat',
    'starting_price': '₹24,500',
    'price_display': 'Starting from ₹24,500 per person',
    'departures_summary': 'Monthly scheduled departures & festival batches',
    'departures_guidance': 'Regular group departures are available each month. Please contact Swarnav directly for exact calendar dates and seat availability.',
    'accommodation_summary': 'Economy hotels or guest houses (Triple-sharing basis: 1 double bed + 1 extra mattress) + 3 Night Train journeys',
    'meals_summary': 'Lunch and dinner provided as per itinerary (Breakfast only if included in selected package)',
    'transport_summary': 'Surat–Puri & Varanasi–Surat train journey + AC/2x2 coach for local temple tours + Gangasagar ferry crossing + Jasidih–Varanasi overnight train',
    'confirmation_note': 'Package price, departure schedule, and room availability require final written confirmation before booking.',
    'gujarat_support_note': 'Main departure starts at Surat Railway Station. Transportation arrangements to and from Surat can be arranged for devotees travelling from anywhere in Gujarat or India (charges applicable).',
    
    'introduction': [
        "The Jagannath Puri & Eastern Divine Pilgrimage connects four revered spiritual regions across Odisha, West Bengal, Jharkhand, and Uttar Pradesh.",
        "Pilgrims receive Chaturdha Murti darshan of Lord Jagannath in Puri, visit the Konark Sun Temple, and witness ancient Kalinga temples in Bhubaneswar.",
        "The journey continues to Kolkata's revered Dakshineswar and Kalighat Shaktipeeth, followed by the sacred Ganga–Sagar Sangam ocean snan.",
        "The yatra culminates with holy Jalabhishekam at Baba Baidyanath Jyotirlinga in Deoghar, and grand darshan of Shri Kashi Vishwanath with Dashashwamedh Ganga Aarti in Varanasi."
    ],

    'dhams': [
        {
            'order': '1',
            'name': 'Shree Jagannath Puri',
            'significance': 'Original Char Dham Abode of Lord Jagannath',
            'description': 'Revered 12th-century ocean temple on the Bay of Bengal coast with Chaturdha Murti darshan and holy Mahaprasad.',
            'highlight': 'First Spiritual Dham',
            'image': 'puri-jagannath-temple-main.jpg'
        },
        {
            'order': '2',
            'name': 'Gangasagar Sangam',
            'significance': 'Holy Confluence of Sacred Ganga & Bay of Bengal Ocean',
            'description': 'Ancient ocean island tirtha where taking a holy dip and visiting Kapil Muni Temple liberates souls.',
            'highlight': 'Sacred Ocean Confluence',
            'image': 'gangasagar-mela-sangam.jpg'
        },
        {
            'order': '3',
            'name': 'Baba Baidyanath Jyotirlinga',
            'significance': 'Sacred Shiva Jyotirlinga of Healing (Kamna Linga)',
            'description': 'One of the 12 sacred Jyotirlingas in Deoghar, Jharkhand, celebrated for divine healing and fulfilling wishes.',
            'highlight': 'Sacred Shiva Jyotirlinga',
            'image': 'deoghar-baidyanath-dham.jpg'
        },
        {
            'order': '4',
            'name': 'Kashi Vishwanath (Varanasi)',
            'significance': 'The Eternal Moksha Dham on Sacred River Ganga',
            'description': 'Supreme Jyotirlinga in Varanasi featuring the grand Corridor, Ganga Ghats, and evening Dashashwamedh Aarti.',
            'highlight': 'Concluding Moksha Dham',
            'image': 'kashi-vishwanath-corridor.jpg'
        }
    ],

    'route_highlights': [
        'Surat', 'Puri', 'Konark', 'Bhubaneswar', 'Kolkata', 
        'Gangasagar', 'Deoghar (Jasidih)', 'Varanasi', 'Sarnath', 'Surat'
    ]
}

PURI_ITINERARY_DAYS = [
    {
        'day': 1,
        'title': 'Surat to Puri',
        'starting_point': 'Surat',
        'destination': 'Puri (En Route)',
        'intro': 'Morning departure from Surat Railway Station by train. Full-day and overnight interstate journey towards Puri.',
        'route_summary': 'Surat ➔ Central India ➔ Puri (Overnight Train)',
        'route_nodes': [
            {'name': 'Surat Station', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Central India Route', 'type': 'Transit', 'badge_class': 'visit'},
            {'name': 'Overnight Train', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Surat Railway Station Departure',
                'image': 'puri-beach-swargadwar.jpg',
                'image_alt': 'Pilgrimage train journey from Surat towards Odisha',
                'caption': 'Train journey towards holy Puri',
                'point': 'Morning departure from Surat in reserved berths with tour manager assistance and meals.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight Train',
            'type': 'Reserved Train Berth',
            'hotel_name': 'Indian Railways Express Train'
        },
        'meals': 'Lunch & Dinner on Train'
    },
    {
        'day': 2,
        'title': 'Arrival in Puri & Shree Jagannath Temple Darshan',
        'starting_point': 'Puri Station',
        'destination': 'Puri',
        'intro': 'Arrival in Puri, hotel check-in, Shree Jagannath Temple darshan, Gundicha Temple, Swargadwar and Puri Beach.',
        'route_summary': 'Puri Station ➔ Hotel Check-in ➔ Shree Jagannath Temple ➔ Gundicha Temple ➔ Puri Beach',
        'route_nodes': [
            {'name': 'Puri Station', 'type': 'Arrival', 'badge_class': 'start'},
            {'name': 'Shree Jagannath Temple', 'type': 'Main Darshan', 'badge_class': 'visit'},
            {'name': 'Gundicha Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Puri Beach & Swargadwar', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Puri', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Shree Jagannath Temple',
                'image': 'puri-jagannath-temple-main.jpg',
                'image_alt': 'Shree Jagannath Temple in Puri Odisha',
                'caption': 'Shree Jagannath Temple Sanctum',
                'point': '12th-century Char Dham temple dedicated to Lord Jagannath, Balabhadra, and Subhadra.'
            },
            {
                'name': 'Puri Beach & Swargadwar',
                'image': 'puri-beach-swargadwar.jpg',
                'image_alt': 'Golden sandy beach in Puri',
                'caption': 'Puri Golden Beach Coastline',
                'point': 'Sacred sea beach and historic Swargadwar along the Bay of Bengal coastline.'
            }
        ],
        'accommodation': {
            'night_stay': 'Puri',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Nilachal / Golden Wave (or similar)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 3,
        'title': 'Puri to Konark, Bhubaneswar & Night Train to Kolkata',
        'starting_point': 'Puri',
        'destination': 'Bhubaneswar / Kolkata (Overnight Train)',
        'intro': 'Early departure. Visit Chandrabhaga Beach, Konark Sun Temple, Dhauli Shanti Stupa and Lingaraj Temple. Board night train for Kolkata.',
        'route_summary': 'Puri ➔ Chandrabhaga Beach ➔ Konark Sun Temple ➔ Dhauli Stupa ➔ Lingaraj Temple ➔ Kolkata',
        'route_nodes': [
            {'name': 'Puri', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Chandrabhaga Beach', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Konark Sun Temple', 'type': 'UNESCO Site', 'badge_class': 'visit'},
            {'name': 'Dhauli Peace Pagoda', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Lingaraj Temple', 'type': 'Darshan', 'badge_class': 'visit'},
            {'name': 'Overnight Train to Kolkata', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Konark Sun Temple',
                'image': 'konark-sun-temple-wheel.jpg',
                'image_alt': 'Carved stone chariot wheel at Konark Sun Temple',
                'caption': 'UNESCO World Heritage Sun Temple',
                'point': '13th-century stone chariot masterpiece with 24 intricately sculpted wheels.'
            },
            {
                'name': 'Lingaraj Temple, Bhubaneswar',
                'image': 'lingaraj-temple-bhubaneswar.jpg',
                'image_alt': 'Lingaraj Temple spire in Bhubaneswar',
                'caption': 'Historic Lingaraj Temple in Bhubaneswar',
                'point': 'Ancient Kalinga temple dedicated to Harihara (Lord Shiva and Lord Vishnu).'
            },
            {
                'name': 'Dhauli Shanti Stupa',
                'image': 'dhauli-shanti-stupa.jpg',
                'image_alt': 'Peace Pagoda at Dhauli Giri near Daya River',
                'caption': 'Dhauli Peace Pagoda',
                'point': 'Historic Peace Pagoda where Emperor Ashoka renounced war for Buddhism.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight Train to Kolkata',
            'type': 'Reserved Train Berth',
            'hotel_name': 'Indian Railways Express Train'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 4,
        'title': 'Kolkata Temple Tour',
        'starting_point': 'Kolkata Station',
        'destination': 'Kolkata',
        'intro': 'Morning arrival and hotel check-in. Visit Dakshineswar Kali Temple, Belur Math, Kalighat Kali Temple, and Birla Mandir or ISKCON.',
        'route_summary': 'Kolkata ➔ Dakshineswar Kali ➔ Belur Math ➔ Kalighat Kali ➔ Birla Mandir',
        'route_nodes': [
            {'name': 'Kolkata Station', 'type': 'Arrival', 'badge_class': 'start'},
            {'name': 'Dakshineswar Kali Temple', 'type': 'Darshan', 'badge_class': 'visit'},
            {'name': 'Belur Math', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Kalighat Kali Temple', 'type': 'Shaktipeeth', 'badge_class': 'visit'},
            {'name': 'Kolkata', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Dakshineswar Kali Temple',
                'image': 'dakshineswar-kali-temple.jpg',
                'image_alt': 'Dakshineswar Kali Temple along Hooghly River',
                'caption': 'Maa Bhavatarini at Dakshineswar',
                'point': 'Revered temple on Hooghly riverbank associated with Sri Ramakrishna Paramahamsa.'
            },
            {
                'name': 'Belur Math',
                'image': 'belur-math-kolkata.jpg',
                'image_alt': 'Main temple of Belur Math Headquarters',
                'caption': 'Belur Math Ramakrishna Mission',
                'point': 'Global headquarters of Ramakrishna Mission founded by Swami Vivekananda.'
            },
            {
                'name': 'Kalighat Kali Temple',
                'image': 'kalighat-temple-kolkata.jpg',
                'image_alt': 'Kalighat Kali Temple in Kolkata',
                'caption': 'Kalighat 51 Maha Shaktipeeth',
                'point': '51 Maha Shaktipeeth shrine where the sacred right toes of Goddess Sati fell.'
            }
        ],
        'accommodation': {
            'night_stay': 'Kolkata',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Lindsay / Hotel Aster (or similar)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 5,
        'title': 'Kolkata Sightseeing & Bazaars',
        'starting_point': 'Kolkata',
        'destination': 'Kolkata',
        'intro': 'Visit Victoria Memorial, St. Paul’s Cathedral, Howrah Bridge, Prinsep Ghat, and Indian Museum. Shopping at New Market and Bara Bazar.',
        'route_summary': 'Victoria Memorial ➔ St. Paul’s ➔ Prinsep Ghat ➔ Howrah Bridge ➔ Bara Bazar',
        'route_nodes': [
            {'name': 'Kolkata Hotel', 'type': 'Start', 'badge_class': 'start'},
            {'name': 'Victoria Memorial', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Prinsep Ghat', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Howrah Bridge', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Bara Bazar Shopping', 'type': 'Shopping', 'badge_class': 'visit'},
            {'name': 'Kolkata', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Victoria Memorial',
                'image': 'victoria-memorial-kolkata.jpg',
                'image_alt': 'Victoria Memorial white marble monument',
                'caption': 'Grand Victoria Memorial & Maidan',
                'point': 'Grand white Makrana marble monument with royal gardens and museum galleries.'
            },
            {
                'name': 'Howrah Bridge',
                'image': 'howrah-bridge-kolkata.jpg',
                'image_alt': 'Cantilever Howrah Bridge over Hooghly River',
                'caption': 'Historic Howrah Bridge (Rabindra Setu)',
                'point': 'Iconic balanced cantilever bridge connecting Kolkata and Howrah over Hooghly River.'
            }
        ],
        'accommodation': {
            'night_stay': 'Kolkata',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Lindsay / Hotel Aster (or similar)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 6,
        'title': 'Kolkata to Gangasagar & Return',
        'starting_point': 'Kolkata',
        'destination': 'Gangasagar ➔ Kolkata',
        'intro': 'Early departure for Gangasagar. Ferry journey to Sagar Island. Visit Kapil Muni Temple, Ganga–Sagar Sangam, Gangasagar Beach, and return to Kolkata.',
        'route_summary': 'Kolkata ➔ Lot 8 ➔ Ferry to Sagar Island ➔ Kapil Muni Temple & Sangam ➔ Kolkata',
        'route_nodes': [
            {'name': 'Kolkata', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Lot 8 Ferry', 'type': 'Ferry Crossing', 'badge_class': 'visit'},
            {'name': 'Ganga-Sagar Sangam', 'type': 'Holy Snan', 'badge_class': 'visit'},
            {'name': 'Kapil Muni Temple', 'type': 'Darshan', 'badge_class': 'visit'},
            {'name': 'Kolkata', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Ganga-Sagar Sangam',
                'image': 'gangasagar-mela-sangam.jpg',
                'image_alt': 'Confluence of River Ganga with Bay of Bengal ocean at Gangasagar',
                'caption': 'Sacred Ganga–Sagar Sangam',
                'point': 'Holy confluence of Mother Ganga and Bay of Bengal for sacred snan and rituals.'
            },
            {
                'name': 'Kapil Muni Temple',
                'image': 'gangasagar-kapil-muni.jpg',
                'image_alt': 'Kapil Muni Temple on Sagar Island',
                'caption': 'Sage Kapil Muni Temple & Ashram',
                'point': 'Ancient hermitage temple of Sage Kapil Muni on Sagar Island.'
            }
        ],
        'accommodation': {
            'night_stay': 'Kolkata',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Lindsay / Hotel Aster (or similar)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 7,
        'title': 'Kolkata to Deoghar, Jharkhand',
        'starting_point': 'Kolkata',
        'destination': 'Deoghar, Jharkhand',
        'intro': 'Travel to Jasidih/Deoghar. After check-in, visit Naulakha Mandir, Satsang Ashram, and Nandan Pahar. Trikut Pahar if arrival is early.',
        'route_summary': 'Kolkata ➔ Jasidih / Deoghar ➔ Naulakha Mandir ➔ Satsang Ashram ➔ Nandan Pahar',
        'route_nodes': [
            {'name': 'Kolkata', 'type': 'Morning Departure', 'badge_class': 'start'},
            {'name': 'Jasidih / Deoghar', 'type': 'Arrival', 'badge_class': 'visit'},
            {'name': 'Naulakha Mandir', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Satsang Ashram', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Deoghar', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Deoghar Spiritual Town & Naulakha Mandir',
                'image': 'deoghar-baidyanath-dham.jpg',
                'image_alt': 'Baidyanath Dham holy town in Deoghar Jharkhand',
                'caption': 'Baidyanath Dham Holy Town',
                'point': 'Pilgrimage town in Santhal Parganas with Radha-Krishna Naulakha Mandir and ashrams.'
            }
        ],
        'accommodation': {
            'night_stay': 'Deoghar',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Baidyanath / Hotel Yashoda (or similar)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 8,
        'title': 'Deoghar to Varanasi (Baba Baidyanath Jyotirlinga)',
        'starting_point': 'Deoghar',
        'destination': 'Varanasi (Overnight Train)',
        'intro': 'Early morning Baba Baidyanath Jyotirlinga darshan. Visit Shiv Ganga and temple complex. Basukinath Temple if timing permits. Night train to Varanasi.',
        'route_summary': 'Baba Baidyanath Jyotirlinga ➔ Shiv Ganga ➔ Basukinath Temple ➔ Jasidih ➔ Varanasi',
        'route_nodes': [
            {'name': 'Deoghar', 'type': 'Start', 'badge_class': 'start'},
            {'name': 'Baba Baidyanath Jyotirlinga', 'type': 'Main Darshan', 'badge_class': 'visit'},
            {'name': 'Shiv Ganga Kund', 'type': 'Holy Water', 'badge_class': 'visit'},
            {'name': 'Basukinath Temple', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Overnight Train to Varanasi', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Baba Baidyanath Jyotirlinga',
                'image': 'deoghar-baidyanath-dham.jpg',
                'image_alt': 'Baba Baidyanath Jyotirlinga Temple in Deoghar Jharkhand',
                'caption': 'Sacred Baba Baidyanath Jyotirlinga',
                'point': 'Kamna Linga Jyotirlinga of Lord Shiva known for fulfilling deepest devotee prayers.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight Train to Varanasi',
            'type': 'Reserved Train Berth',
            'hotel_name': 'Indian Railways Express Train'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 9,
        'title': 'Arrival in Varanasi & Kashi Vishwanath Darshan',
        'starting_point': 'Varanasi Junction',
        'destination': 'Varanasi',
        'intro': 'Morning arrival and hotel check-in. Visit Shri Kashi Vishwanath Temple, Maa Annapurna Temple, Vishalakshi Temple, Kaal Bhairav, and Varanasi ghats.',
        'route_summary': 'Varanasi Station ➔ Hotel Check-in ➔ Kashi Vishwanath Corridor ➔ Annapurna ➔ Kaal Bhairav ➔ Ghats',
        'route_nodes': [
            {'name': 'Varanasi Station', 'type': 'Arrival', 'badge_class': 'start'},
            {'name': 'Shri Kashi Vishwanath', 'type': 'Jyotirlinga Darshan', 'badge_class': 'visit'},
            {'name': 'Maa Annapurna Mandir', 'type': 'Darshan', 'badge_class': 'visit'},
            {'name': 'Kaal Bhairav Temple', 'type': 'Darshan', 'badge_class': 'visit'},
            {'name': 'Varanasi', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Shri Kashi Vishwanath Corridor',
                'image': 'kashi-vishwanath-corridor.jpg',
                'image_alt': 'Grand Kashi Vishwanath Corridor leading to Ganga Ghats in Varanasi',
                'caption': 'Grand Shri Kashi Vishwanath Corridor',
                'point': 'Supreme Moksha Jyotirlinga situated on the sacred western banks of River Ganga.'
            }
        ],
        'accommodation': {
            'night_stay': 'Varanasi',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Kashi Inn / Hotel Ganges Grand (or similar)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 10,
        'title': 'Varanasi Sightseeing & Dashashwamedh Ganga Aarti',
        'starting_point': 'Varanasi',
        'destination': 'Varanasi',
        'intro': 'Visit Sankat Mochan Temple, Durga Kund, Tulsi Manas Mandir, BHU New Vishwanath Temple, and Sarnath. Evening Ganga Aarti at Dashashwamedh Ghat.',
        'route_summary': 'Sankat Mochan ➔ Durga Kund ➔ BHU Vishwanath ➔ Sarnath ➔ Dashashwamedh Ganga Aarti',
        'route_nodes': [
            {'name': 'Varanasi Hotel', 'type': 'Start', 'badge_class': 'start'},
            {'name': 'Sankat Mochan Temple', 'type': 'Darshan', 'badge_class': 'visit'},
            {'name': 'Sarnath (Dhamek Stupa)', 'type': 'Visit', 'badge_class': 'visit'},
            {'name': 'Dashashwamedh Ghat', 'type': 'Grand Ganga Aarti', 'badge_class': 'visit'},
            {'name': 'Varanasi', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Dashashwamedh Ganga Aarti',
                'image': 'varanasi-ganga-aarti-evening.jpg',
                'image_alt': 'Evening Ganga Aarti at Dashashwamedh Ghat in Varanasi',
                'caption': 'Maha Ganga Aarti at Dashashwamedh Ghat',
                'point': 'Grand evening Ganga worship with tiered brass lamps, conch shells, and chants.'
            },
            {
                'name': 'Sarnath (Dhamek Stupa)',
                'image': 'sarnath-dhamek-stupa.jpg',
                'image_alt': 'Dhamek Stupa at Sarnath near Varanasi',
                'caption': 'Dhamek Stupa at Sarnath',
                'point': 'Sacred Buddhist tirtha where Lord Buddha delivered his first sermon.'
            }
        ],
        'accommodation': {
            'night_stay': 'Varanasi',
            'type': 'Economy Hotel',
            'hotel_name': 'Hotel Kashi Inn / Hotel Ganges Grand (or similar)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 11,
        'title': 'Varanasi to Surat (Return Journey)',
        'starting_point': 'Varanasi',
        'destination': 'Surat, Gujarat',
        'intro': 'Breakfast, hotel check-out and transfer to Varanasi railway station. Morning train departure for Surat carrying sacred temple blessings and Prasad.',
        'route_summary': 'Varanasi Station ➔ Madhya Pradesh ➔ Surat, Gujarat (Train Journey)',
        'route_nodes': [
            {'name': 'Varanasi Station', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Interstate Transit', 'type': 'Train Journey', 'badge_class': 'visit'},
            {'name': 'Surat, Gujarat', 'type': 'Tour Concludes', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Return Journey & Prasad',
                'image': 'kashi-vishwanath-corridor.jpg',
                'image_alt': 'Return train journey to Surat carrying sacred blessings',
                'caption': 'Concluding the Grand 11-Day Eastern Pilgrimage',
                'point': 'Carrying sacred Gangasagar water, Jagannath Mahaprasad, Baidyanath Peda, and Kashi Bhasma home.'
            }
        ],
        'accommodation': {
            'night_stay': 'Train Journey to Surat',
            'type': 'Reserved Train Berth',
            'hotel_name': 'Indian Railways Express Train'
        },
        'meals': 'Breakfast & Meals on Train'
    }
]

PURI_PACKAGE_DETAILS = {
    'inclusions': [
        'Confirmed Train tickets: Surat to Puri, Bhubaneswar to Kolkata, Jasidih to Varanasi, and Varanasi to Surat (as per booked class)',
        'Dedicated group coach / vehicle for all local transfers and sightseeing in Puri, Konark, Bhubaneswar, Kolkata, Deoghar, and Varanasi',
        'Ferry boat tickets for Muriganga River crossing to Gangasagar and local Sagar Island vehicle transfers',
        'Economy lodging in clean hotels or guest houses (triple-sharing basis: 1 double bed + 1 extra mattress)',
        'Lunch and dinner according to the daily travel itinerary (Breakfast provided where included in package)',
        'Services of an experienced Swarnav tour coordinator accompanying the group from Surat',
        'Driver allowances, toll taxes, parking fees, and interstate vehicle permits across Odisha, West Bengal, Jharkhand & UP'
    ],
    'exclusions': [
        'Personal expenses such as laundry, room service, telephone calls, and personal shopping',
        'Temple VIP special puja tickets, Panda/Priest dakshina, and special darshan passes',
        'Entrance tickets / camera fees for monuments (Konark Sun Temple, Victoria Memorial, Sarnath Museum, etc.)',
        'Optional boat ride charges on River Ganga in Varanasi or Puri water sports',
        'Any cost arising due to natural disasters, train delays, or medical emergencies'
    ],
    'conditional_services': [
        {
            'service': 'Gujarat-Wide Onward / Return Travel',
            'condition': 'Transportation to and from Surat can be arranged for devotees travelling from anywhere in Gujarat (Ahmedabad, Vadodara, Rajkot, etc.).'
        },
        {
            'service': 'Twin / Double Sharing Room Upgrade',
            'condition': 'Available upon request for couples or families seeking 2-person private room occupancy (additional surcharge applies).'
        },
        {
            'service': '3AC Train Class Upgrade',
            'condition': 'Upgrade from Sleeper to 3-Tier AC train berths can be confirmed subject to railway seat availability.'
        }
    ],
    'important_notes': [
        'Package price, departure schedule, and room availability require final written confirmation before booking.',
        'Traditional dress is mandatory for entry into Shree Jagannath Temple (Puri) and Baba Baidyanath sanctum (Deoghar). Electronic devices and leather items are strictly prohibited inside the main temple premises.',
        'All sightseeing visits are subject to available time, traffic flow, and ferry tidal timings at Gangasagar.'
    ]
}

PURI_STAY_AND_TRAVEL = {
    'accommodation': {
        'category': 'Economy hotels or guest houses',
        'room_sharing': 'Triple-sharing basis, with three travellers accommodated in one room. The room includes one double bed and one extra mattress.',
        'private_room': 'A separate private room can be arranged upon request, subject to availability and an additional charge.',
        'hot_water': 'Hot water will be provided only where available at the property. In certain temple towns, it may be supplied in buckets or during morning hours.',
        'remote_limitations': 'Hotels and guest houses in pilgrimage towns like Puri and Deoghar offer clean, basic, and hygienic amenities.',
        'hotel_changes': 'The listed hotels are preferred options. A similar-category property will be provided if the listed hotel is unavailable.'
    },
    'meals': {
        'overview': 'Wholesome pure vegetarian meals prepared according to the travel and pilgrimage schedule.',
        'included_meals': 'Lunch and dinner according to the itinerary.',
        'breakfast_rule': 'Breakfast is provided only when explicitly included in the selected package.',
        'trek_days': 'On long transit days and the Gangasagar excursion, packed meals or food vouchers will be provided.',
        'extra_refreshments': 'Extra snacks, packaged drinking water, tea, and personal beverages are not included and must be arranged individually.'
    },
    'transportation': {
        'main_mode': 'Train and road transport',
        'train_journey': 'Surat–Puri, Bhubaneswar–Kolkata, Jasidih–Varanasi, and Varanasi–Surat by train in the confirmed class.',
        'road_transport': 'Bus or tempo traveller used for group sightseeing across Odisha, West Bengal, Jharkhand, and Uttar Pradesh.',
        'local_transport': 'Local e-rickshaws, shared autos, and Muriganga ferry boats utilized where large tour buses cannot enter.',
        'pickup_drop': 'Surat Railway Station or another confirmed location in Surat.',
        'gujarat_travellers': 'Transportation to and from Surat can be arranged upon request for devotees joining from anywhere in Gujarat or India. Applicable charges communicated separately.',
        'vehicle_allocation': 'Vehicle capacity is allocated according to the confirmed group size and state transport regulations.',
        'travel_time_notice': 'Travel and transit times may vary depending on train punctuality, road conditions, ferry tide timings, and temple queues.'
    }
}

PURI_TRAVEL_GUIDE = {
    'age_restrictions': {
        'guidance': 'The Yatra is open to travellers of all age groups.',
        'advisory': 'The tour involves interstate train journeys, ferry crossings at Gangasagar, and walking inside temple complexes. Senior citizens and children should travel with adequate preparation.',
        'safety_restriction': 'Participation may be adjusted if a traveller requires special medical care or wheelchair assistance.'
    },
    'health_requirements': [
        'Travellers should be comfortable with long train journeys, road travel, and temple walking queues.',
        'A basic medical check-up is recommended for senior citizens before departure.',
        'Travellers with chronic conditions (diabetes, blood pressure) must inform us during booking and carry their regular medicines.',
        'Carry ORS sachets, pain relief spray, and personal first-aid supplies for the journey.'
    ],
    'documents_required': [
        'Original Aadhaar card or government-issued photo ID for train travel and hotel check-in',
        'Tour booking confirmation receipt and train e-tickets',
        'Doctor’s prescription for regular medications',
        'Emergency contact numbers and personal identity card'
    ],
    'items_to_carry': [
        'Light cotton clothes for daytime travel and traditional attire for temple darshans',
        'Extra dry clothes and small towel for the holy Gangasagar ocean snan',
        'Comfortable slip-on walking shoes or sandals (easy to remove at temple gates)',
        'Personal medications, first-aid kit, and ORS packets',
        'Sun cap, sunglasses, umbrella, and mobile power bank',
        'Valid ID cards, train ticket copies, and sufficient cash'
    ],
    'packing_advice': 'Please pack lightly with one main trolley bag and one small day backpack per person.',
    'weather_info': 'Eastern coastal weather in Odisha and Bengal is warm and humid, while Deoghar and Varanasi have pleasant to warm temperatures depending on the season. Light cotton attire is recommended throughout the tour.'
}

PURI_POLICIES = {
    'booking_conditions': [
        'A 30% advance payment is required to confirm train berths and hotel bookings.',
        'The remaining balance must be paid at least 15 days before departure.',
        'Bookings made within 15 days of departure require full payment at the time of reservation.',
        'Confirmation is subject to train ticket and hotel room availability.',
        'Travellers must provide accurate government ID details for railway reservation.',
        'Panda/Priest dakshina, VIP puja passes, and personal expenses are not included in the standard package.',
        'Hotel rooms are provided on a triple-sharing basis (one double bed + one extra mattress).',
        'The itinerary may be adjusted due to train delays, ferry tide timings, temple schedules, or local administrative rules.',
        'The booking is considered confirmed only after the advance payment and official written confirmation have been issued.'
    ],
    'cancellation_brackets': [
        {
            'timeline': '30 days or more before departure',
            'deduction': '10% of total package cost (plus railway cancellation fees)',
            'refund_estimate': '90% of package cost (less railway cancellation fees)'
        },
        {
            'timeline': '16 to 29 days before departure',
            'deduction': '25% of total package cost (plus railway cancellation fees)',
            'refund_estimate': '75% of package cost (less railway cancellation fees)'
        },
        {
            'timeline': '8 to 15 days before departure',
            'deduction': '50% of total package cost',
            'refund_estimate': '50% of package cost'
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
        'Train cancellation charges are governed strictly by Indian Railways (IRCTC) refund rules.',
        'Approved refunds will normally be processed within 7–15 working days.',
        'If the tour is affected by severe weather, train cancellations, or administrative restrictions, alternative arrangements or refunds will follow respective service provider policies.',
        'If Swarnav cancels the tour for operational reasons, travellers may choose an alternative date or receive a full refund.'
    ]
}

PURI_NAV_TABS = [
    {'name': 'Overview', 'slug': 'overview', 'url_name': 'yatras:puri_overview'},
    {'name': '11-Day Itinerary', 'slug': 'itinerary', 'url_name': 'yatras:puri_itinerary'},
    {'name': 'Package Details', 'slug': 'package-details', 'url_name': 'yatras:puri_package_details'},
    {'name': 'Stay & Travel', 'slug': 'stay-and-travel', 'url_name': 'yatras:puri_stay_and_travel'},
    {'name': 'Travel Guide', 'slug': 'travel-guide', 'url_name': 'yatras:puri_travel_guide'},
    {'name': 'Policies', 'slug': 'policies', 'url_name': 'yatras:puri_policies'},
]

def get_puri_package():
    return PURI_PACKAGE

def get_puri_all_days():
    return PURI_ITINERARY_DAYS

def get_puri_day_by_number(day_number):
    for day in PURI_ITINERARY_DAYS:
        if day['day'] == day_number:
            return day
    return None

def get_puri_package_details():
    return PURI_PACKAGE_DETAILS

def get_puri_stay_and_travel():
    return PURI_STAY_AND_TRAVEL

def get_puri_travel_guide():
    return PURI_TRAVEL_GUIDE

def get_puri_policies():
    return PURI_POLICIES
