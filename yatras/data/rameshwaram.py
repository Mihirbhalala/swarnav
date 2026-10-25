"""
Verified source data for Rameshwaram & South Divine Pilgrimage Tour.
12-Day comprehensive itinerary covering Surat, Madurai (Meenakshi Amman),
Pamban Bridge, Rameshwaram (Ramanathaswamy Jyotirlinga, 22 Theerthams),
Dhanushkodi (Arichal Munai / Ram Setu), Tiruchendur Murugan, Kanyakumari (Triveni Sangam),
and Trivandrum (Sree Padmanabhaswamy Temple & Kovalam).
"""

RAMESHWARAM_PACKAGE = {
    'slug': 'rameshwaram-circuit',
    'name': 'Rameshwaram & South Divine Pilgrimage',
    'subtitle': 'Madurai • Rameshwaram • Dhanushkodi • Tiruchendur • Kanyakumari • Trivandrum',
    'tagline': 'Sacred 12-Day Grand South Pilgrimage across Tamil Nadu & Kerala Coastal Tirthas',
    'duration_days': 12,
    'duration_nights': 11,
    'duration_display': '12 Days / 11 Nights',
    'starting_city': 'Surat, Gujarat',
    'ending_city': 'Surat, Gujarat',
    'starting_price': '₹30,000',
    'price_display': 'Starting from ₹30,000 per person',
    'departures_summary': 'Monthly Scheduled Departures & Festival Batches',
    'departures_guidance': 'Regular group departures are available each month. Please contact Swarnav directly for upcoming calendar departure dates and confirmed seat availability.',
    'batch_badge': 'Monthly Departures Open',
    'accommodation_summary': 'Deluxe & Economy hotels in Madurai, Rameshwaram, Kanyakumari & Trivandrum (Triple-sharing basis) + 3 Nights AC Train journeys',
    'meals_summary': 'Lunch and dinner provided as per itinerary (Breakfast only if included in selected package)',
    'transport_summary': 'Surat to Madurai & Madurai to Surat confirmed AC train journeys + Dedicated AC 2x2 luxury coach / sanitized Tempo Traveller for all South Indian local and interstate transits',
    'confirmation_note': 'Package price, departure schedule, and room availability require final written confirmation before booking.',
    'gujarat_support_note': 'Main departure starts at Surat Railway Station. Transportation arrangements to and from Surat can be arranged for devotees travelling from Ahmedabad, Vadodara, Rajkot, Mumbai, or anywhere in Gujarat & India (charges applicable).',

    'introduction': [
        "The Rameshwaram & South Divine Pilgrimage is one of India's most sacred coastal yatras, uniting the ancient spiritual power of Lord Shiva's holy Jyotirlinga with the supreme blessings of Goddess Meenakshi, Lord Murugan, and Lord Padmanabhaswamy.",
        "Commencing with an AC train journey from Surat, pilgrims journey to the historic city of Madurai to seek darshan at the world-renowned Meenakshi Amman Temple, famed for its towering sculpted gopurams and centuries of Dravidian spiritual heritage.",
        "Crossing the iconic Pamban Sea Bridge, the yatra enters holy Rameshwaram island — an original Char Dham shrine and sacred Jyotirlinga abode where Lord Rama worshipped Lord Shiva. Pilgrims take the sacred sea bath at Agni Theertham, undergo the purifying 22 temple well snan, and marvel at the breathtaking coastal confluence at Dhanushkodi and Arichal Munai (starting point of Ram Setu).",
        "The pilgrimage continues along the southern coastline to the ancient seashore temple of Tiruchendur Murugan, the three-ocean Triveni Sangam and Vivekananda Rock Memorial at Kanyakumari, and the majestic Sree Padmanabhaswamy Temple in Trivandrum before returning comfortably to Surat."
    ],

    'dhams': [
        {
            'order': '1',
            'name': 'Sri Ramanathaswamy Jyotirlinga',
            'significance': 'Original Char Dham & Sacred Southern Jyotirlinga',
            'description': 'Revered island temple where Lord Rama consecrated the Shiva Lingam. Renowned for its world-famous third corridor of 1,212 carved pillars and 22 sacred cleansing wells (Theerthams).',
            'highlight': 'Supreme Shiva Jyotirlinga',
            'image': 'rameshwaram-temple.jpg'
        },
        {
            'order': '2',
            'name': 'Madurai Meenakshi Amman Temple',
            'significance': 'Ancient Shakta Tirtha & Dravidian Masterpiece',
            'description': 'Historic temple city dedicated to Goddess Meenakshi and Lord Sundareswarar with 14 towering sculpted Gopurams, the Golden Lotus sacred pond, and vibrant spiritual rituals.',
            'highlight': 'Sacred Devi Shrine',
            'image': 'madurai-meenakshi-temple.jpg'
        },
        {
            'order': '3',
            'name': 'Dhanushkodi & Arichal Munai (Ram Setu)',
            'significance': 'Sacred Confluence & Starting Point of Ram Setu',
            'description': 'Breathtaking coastal tip where the Bay of Bengal (Mahodadhi) and Indian Ocean (Ratnakara) meet, marking the sacred path where the Vanara Sena built the bridge to Lanka.',
            'highlight': 'Sacred Ram Setu Point',
            'image': 'dhanushkodi-arichal-munai.jpg'
        },
        {
            'order': '4',
            'name': 'Kanyakumari Triveni Sangam & Rock Memorial',
            'significance': 'Confluence of Three Oceans & Devi Kanya Kumari',
            'description': 'India’s southernmost tip where the Arabian Sea, Bay of Bengal, and Indian Ocean merge. Features the offshore Vivekananda Rock Memorial and 133-ft stone Thiruvalluvar Statue.',
            'highlight': 'Three Oceans Confluence',
            'image': 'kanyakumari-rock-memorial.jpg'
        },
        {
            'order': '5',
            'name': 'Sree Padmanabhaswamy Temple (Trivandrum)',
            'significance': 'Supreme Abode of Lord Vishnu in Ananthasayanam',
            'description': 'Ancient Divya Desam temple in Kerala where Lord Padmanabha reclines on the multi-hooded serpent Adisesha, observed through three sanctum doorways.',
            'highlight': 'Divine Vishnu Abode',
            'image': 'padmanabhaswamy-temple.jpg'
        }
    ],

    'route_highlights': [
        'Surat', 'Madurai', 'Rameshwaram', 'Pamban Bridge', 'Dhanushkodi', 
        'Tiruchendur', 'Kanyakumari', 'Trivandrum', 'Kovalam Beach', 'Madurai', 'Surat'
    ]
}

RAMESHWARAM_ITINERARY_DAYS = [
    {
        'day': 1,
        'title': 'Surat to Madurai by AC Train',
        'starting_point': 'Surat Railway Station',
        'destination': 'Madurai (En Route)',
        'intro': 'Begin your South India spiritual journey with an AC train journey from Surat towards Madurai. Enjoy the comfortable overnight journey.',
        'route_summary': 'Surat Railway Station ➔ Western & Southern Rail Route ➔ Overnight AC Train',
        'route_nodes': [
            {'name': 'Surat Railway Station', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Western & Southern Rail Route', 'type': 'Transit', 'badge_class': 'visit'},
            {'name': 'Overnight AC Train', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Surat Railway Station Departure',
                'image': 'madurai-meenakshi-temple.jpg',
                'image_alt': 'Pilgrimage train departure from Surat station towards Tamil Nadu',
                'caption': 'All Aboard for South India Pilgrimage',
                'point': 'Board your confirmed AC train berths at Surat with our experienced tour coordinator assistance.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight AC Train',
            'type': 'Reserved AC Train Berth',
            'hotel_name': 'Indian Railways AC Express Train'
        },
        'meals': 'Lunch & Dinner on Train (Breakfast if included in package)'
    },
    {
        'day': 2,
        'title': 'Train Journey to Madurai',
        'starting_point': 'Train Transit',
        'destination': 'Madurai (En Route)',
        'intro': 'Continue your comfortable train journey towards Madurai. Enjoy the scenic views during the journey and spend the night travelling towards your destination.',
        'route_summary': 'Peninsular India Rail Route ➔ Tamil Nadu Transit ➔ Overnight AC Train',
        'route_nodes': [
            {'name': 'Peninsular India Railway Route', 'type': 'Scenic Transit', 'badge_class': 'start'},
            {'name': 'Andhra & Tamil Nadu Rail Corridors', 'type': 'Transit', 'badge_class': 'visit'},
            {'name': 'Overnight AC Train', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Peninsular Scenic Train Route',
                'image': 'madurai-meenakshi-temple.jpg',
                'image_alt': 'Train journey traversing through lush green fields and hills of South India',
                'caption': 'Scenic Rail Route to Madurai',
                'point': 'Relax, enjoy warm satvik meals, and connect with fellow devotees as the train traverses picturesque South Indian plains.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight AC Train',
            'type': 'Reserved AC Train Berth',
            'hotel_name': 'Indian Railways AC Express Train'
        },
        'meals': 'Lunch & Dinner on Train (Breakfast if included in package)'
    },
    {
        'day': 3,
        'title': 'Arrival in Madurai & Meenakshi Amman Temple',
        'starting_point': 'Madurai Junction Station',
        'destination': 'Madurai',
        'intro': 'Arrive in Madurai and transfer to the hotel. After freshening up, begin sightseeing of the historic city. Visit the famous Meenakshi Amman Temple, Thirumalai Nayak Palace and other important attractions.',
        'route_summary': 'Madurai Station ➔ Hotel Check-in ➔ Meenakshi Amman Temple ➔ Thirumalai Nayak Palace ➔ Madurai Hotel',
        'route_nodes': [
            {'name': 'Madurai Junction', 'type': 'Arrival', 'badge_class': 'start'},
            {'name': 'Hotel Check-in & Rest', 'type': 'Halt', 'badge_class': 'visit'},
            {'name': 'Meenakshi Amman Temple', 'type': 'Main Darshan', 'badge_class': 'visit'},
            {'name': 'Thirumalai Nayak Palace', 'type': 'Heritage Visit', 'badge_class': 'visit'},
            {'name': 'Madurai Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Meenakshi Amman Temple',
                'image': 'madurai-meenakshi-temple.jpg',
                'image_alt': 'Towering gopurams of Meenakshi Amman Temple in Madurai reflecting in temple pond',
                'caption': 'Historic Meenakshi Amman Temple',
                'point': 'Ancient 2,500-year-old architectural marvel dedicated to Goddess Parvati (Meenakshi) and Lord Shiva (Sundareswarar) with intricately carved multi-tiered gopurams.'
            },
            {
                'name': 'Thirumalai Nayak Palace',
                'image': 'madurai-meenakshi-temple.jpg',
                'image_alt': 'Colossal stone pillars of Thirumalai Nayak Palace Madurai',
                'caption': '17th-Century Royal Nayak Palace',
                'point': 'Stunning Indo-Saracenic palace built by King Thirumalai Nayak in 1636, noted for giant circular pillars and grand courtyards.'
            }
        ],
        'accommodation': {
            'night_stay': 'Madurai',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Royal Court / Hotel Supreme / Hotel Madurai Residency (or similar property)'
        },
        'meals': 'Lunch & Dinner (Breakfast if included in package)'
    },
    {
        'day': 4,
        'title': 'Madurai to Rameshwaram & Pamban Bridge',
        'starting_point': 'Madurai',
        'destination': 'Rameshwaram',
        'intro': 'After breakfast, proceed towards the sacred city of Rameshwaram. En route, enjoy the scenic views and cross the famous Pamban Bridge. After hotel check-in, visit Agni Theertham and relax.',
        'route_summary': 'Madurai Hotel ➔ Ramanathapuram ➔ Pamban Sea Bridge ➔ Rameshwaram Hotel ➔ Agni Theertham',
        'route_nodes': [
            {'name': 'Madurai', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Pamban Ocean Bridge', 'type': 'Iconic Crossing', 'badge_class': 'visit'},
            {'name': 'Rameshwaram Hotel Check-in', 'type': 'Arrival', 'badge_class': 'visit'},
            {'name': 'Agni Theertham', 'type': 'Sacred Sea Beach', 'badge_class': 'visit'},
            {'name': 'Rameshwaram Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Pamban Bridge Crossing',
                'image': 'rameshwaram-temple.jpg',
                'image_alt': 'Historic Pamban bridge connecting Indian mainland to Rameshwaram island across the ocean',
                'caption': 'Engineering Wonder Pamban Bridge',
                'point': 'Cross India’s first sea bridge spanning over 2 km across the Palk Strait, offering panoramic views of blue ocean waters and coastal horizons.'
            },
            {
                'name': 'Agni Theertham',
                'image': 'rameshwaram-temple.jpg',
                'image_alt': 'Devotees taking sacred holy dip at Agni Theertham sea beach Rameshwaram',
                'caption': 'Holy Agni Theertham Ocean Beach',
                'point': 'Sacred sea shore located directly in front of the eastern temple tower where pilgrims take the customary holy snan before entering Ramanathaswamy Temple.'
            }
        ],
        'accommodation': {
            'night_stay': 'Rameshwaram',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Daiwik / Hotel Temple Tower / Hotel Rameshwaram Grand (or similar property)'
        },
        'meals': 'Lunch & Dinner (Breakfast if included in package)'
    },
    {
        'day': 5,
        'title': 'Rameshwaram Temple Darshan & 22 Theerthams',
        'starting_point': 'Rameshwaram Hotel',
        'destination': 'Rameshwaram',
        'intro': 'Begin the day with Ramanathaswamy Temple Darshan. Later, visit important spiritual and local attractions including Gandhamadhana Parvatham and Panchmukhi Hanuman Temple.',
        'route_summary': 'Agni Theertham Snan ➔ Ramanathaswamy Temple 22 Kund Snan ➔ Main Sanctum Darshan ➔ Gandhamadhana Parvatham ➔ Panchmukhi Hanuman',
        'route_nodes': [
            {'name': 'Agni Theertham', 'type': 'Purifying Snan', 'badge_class': 'start'},
            {'name': 'Ramanathaswamy Temple 22 Wells', 'type': 'Holy Kund Bath', 'badge_class': 'visit'},
            {'name': 'Sri Ramanatha Jyotirlinga', 'type': 'Supreme Darshan', 'badge_class': 'visit'},
            {'name': 'Gandhamadhana Parvatham', 'type': 'Hilltop View', 'badge_class': 'visit'},
            {'name': 'Panchmukhi Hanuman Temple', 'type': 'Floating Stone', 'badge_class': 'visit'},
            {'name': 'Rameshwaram Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Sri Ramanathaswamy Temple & Pillared Corridor',
                'image': 'rameshwaram-temple.jpg',
                'image_alt': 'Grand pillared corridor of Ramanathaswamy Temple in Rameshwaram',
                'caption': 'Sri Ramanathaswamy Jyotirlinga Sanctum',
                'point': 'One of the 12 sacred Jyotirlingas and Char Dham pilgrimage sites, celebrated for the holy Jyotirlinga installed by Lord Rama and the longest temple corridor in the world with 1,212 pillars.'
            },
            {
                'name': '22 Holy Theerthams (Sacred Wells)',
                'image': 'rameshwaram-temple.jpg',
                'image_alt': 'Holy water from 22 theerthams inside Ramanathaswamy temple complex',
                'caption': 'Purifying 22 Theertham Snan',
                'point': 'Devotees are bathed with water drawn from 22 ancient freshwater wells within the temple premises, believed to bestow health and wash away past karmas.'
            },
            {
                'name': 'Gandhamadhana Parvatham & Panchmukhi Hanuman',
                'image': 'rameshwaram-temple.jpg',
                'image_alt': 'Gandhamadhana Parvatham hill with footprints of Lord Rama and floating stone of Ram Setu',
                'caption': 'Rama Footprints & Floating Stone',
                'point': 'Highest point on Rameshwaram island housing the chakra with the footprints of Lord Rama, followed by the Panchmukhi Hanuman temple featuring genuine floating stones used to build Ram Setu.'
            }
        ],
        'accommodation': {
            'night_stay': 'Rameshwaram',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Daiwik / Hotel Temple Tower / Hotel Rameshwaram Grand (or similar property)'
        },
        'meals': 'Lunch & Dinner (Breakfast if included in package)'
    },
    {
        'day': 6,
        'title': 'Dhanushkodi Excursion & Arichal Munai (Ram Setu)',
        'starting_point': 'Rameshwaram',
        'destination': 'Dhanushkodi & Rameshwaram',
        'intro': 'After breakfast, proceed for a full-day excursion to Dhanushkodi and Arichal Munai. Enjoy the unique coastal scenery and visit important attractions around Dhanushkodi. Return to Rameshwaram in the evening.',
        'route_summary': 'Rameshwaram ➔ Kothandaramaswamy Temple ➔ Dhanushkodi Ruins ➔ Arichal Munai Ocean Tip ➔ Rameshwaram Hotel',
        'route_nodes': [
            {'name': 'Rameshwaram', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Kothandaramaswamy Temple', 'type': 'Darshan', 'badge_class': 'visit'},
            {'name': 'Dhanushkodi Ghost Town Ruins', 'type': 'Historical Site', 'badge_class': 'visit'},
            {'name': 'Arichal Munai (Ram Setu Tip)', 'type': 'Ocean Confluence', 'badge_class': 'visit'},
            {'name': 'Rameshwaram Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Dhanushkodi & Ghost Town Ruins',
                'image': 'dhanushkodi-arichal-munai.jpg',
                'image_alt': 'Dhanushkodi coastal beach with ruins of church and railway station destroyed in 1964 cyclone',
                'caption': 'Dhanushkodi Historical Ghost Town',
                'point': 'Historic seaside settlement submerged in the 1964 cyclone, preserving atmospheric ruins of a Portuguese church, railway station, and post office amidst golden sandbars.'
            },
            {
                'name': 'Arichal Munai (Ram Setu Point)',
                'image': 'dhanushkodi-arichal-munai.jpg',
                'image_alt': 'Arichal Munai the southernmost tip where Indian Ocean and Bay of Bengal waters meet',
                'caption': 'Arichal Munai - Ram Setu Origin',
                'point': 'The very tip of Indian territory where the shallow limestone shoals of Ram Setu (Adam’s Bridge) lead towards Sri Lanka across calm turquoise ocean waters.'
            },
            {
                'name': 'Kothandaramaswamy Temple',
                'image': 'dhanushkodi-arichal-munai.jpg',
                'image_alt': 'Kothandaramaswamy temple surrounded by sea water on way to Dhanushkodi',
                'caption': 'Kothandaramaswamy Temple',
                'point': 'Historic 500-year-old temple standing amidst the sea, celebrated as the sacred location where Vibhishana surrendered to Lord Rama and was crowned king of Lanka.'
            }
        ],
        'accommodation': {
            'night_stay': 'Rameshwaram',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Daiwik / Hotel Temple Tower / Hotel Rameshwaram Grand (or similar property)'
        },
        'meals': 'Lunch & Dinner (Breakfast if included in package)'
    },
    {
        'day': 7,
        'title': 'Rameshwaram to Kanyakumari via Tiruchendur',
        'starting_point': 'Rameshwaram',
        'destination': 'Kanyakumari',
        'intro': 'After breakfast, check out and proceed towards Kanyakumari. En route, visit the famous Tiruchendur Murugan Temple. Continue your journey to Kanyakumari and check in to the hotel.',
        'route_summary': 'Rameshwaram ➔ Ramanathapuram ➔ Tuticorin ➔ Tiruchendur Murugan Temple ➔ Kanyakumari Hotel',
        'route_nodes': [
            {'name': 'Rameshwaram', 'type': 'Checkout', 'badge_class': 'start'},
            {'name': 'Tuticorin Coast Road', 'type': 'Transit', 'badge_class': 'visit'},
            {'name': 'Tiruchendur Murugan Temple', 'type': 'Seashore Temple Darshan', 'badge_class': 'visit'},
            {'name': 'Kanyakumari Hotel Check-in', 'type': 'Arrival', 'badge_class': 'visit'},
            {'name': 'Kanyakumari Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Tiruchendur Murugan Temple',
                'image': 'kanyakumari-rock-memorial.jpg',
                'image_alt': 'Tiruchendur Murugan temple located directly on the shores of the Bay of Bengal',
                'caption': 'Lord Murugan Seashore Temple',
                'point': 'One of the six holy Arupadai Veedu abodes of Lord Murugan, constructed directly on the seashore where Lord Murugan vanquished the demon Surapadman.'
            },
            {
                'name': 'Scenic Coastal Highway to Kanyakumari',
                'image': 'kanyakumari-rock-memorial.jpg',
                'image_alt': 'Coastal highway passing windmills and palm groves into Kanyakumari',
                'caption': 'Scenic Tamil Nadu Coastline',
                'point': 'Travel along the fertile coastal plains past vast salt pans, banana plantations, and iconic windmill farms into southernmost India.'
            }
        ],
        'accommodation': {
            'night_stay': 'Kanyakumari',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Sea View / Hotel Sparsa / Hotel Tri Sea (or similar property)'
        },
        'meals': 'Lunch & Dinner (Breakfast if included in package)'
    },
    {
        'day': 8,
        'title': 'Kanyakumari Sunrise & Local Sightseeing',
        'starting_point': 'Kanyakumari',
        'destination': 'Kanyakumari',
        'intro': 'Start the day with the beautiful Kanyakumari Sunrise. After breakfast, visit Vivekananda Rock Memorial, Thiruvalluvar Statue, Bhagavathi Amman Temple and other attractions. Enjoy the beautiful coastal scenery and sunset.',
        'route_summary': 'Sunrise Point ➔ Ferry to Vivekananda Rock & Thiruvalluvar Statue ➔ Bhagavathi Amman Temple ➔ Gandhi Memorial ➔ Sunset Point',
        'route_nodes': [
            {'name': 'Triveni Sunrise Point', 'type': 'Morning View', 'badge_class': 'start'},
            {'name': 'Vivekananda Rock Memorial', 'type': 'Ferry Excursion', 'badge_class': 'visit'},
            {'name': 'Thiruvalluvar Stone Statue', 'type': 'Island Monument', 'badge_class': 'visit'},
            {'name': 'Bhagavathi Amman Temple', 'type': 'Shakti Darshan', 'badge_class': 'visit'},
            {'name': 'Sunset View Point', 'type': 'Evening View', 'badge_class': 'visit'},
            {'name': 'Kanyakumari Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Vivekananda Rock Memorial & Thiruvalluvar Statue',
                'image': 'kanyakumari-rock-memorial.jpg',
                'image_alt': 'Vivekananda Rock Memorial and Thiruvalluvar statue standing in the ocean at Kanyakumari',
                'caption': 'Vivekananda Rock Memorial',
                'point': 'Majestic ocean memorial built in 1970 on the sacred offshore rock where Swami Vivekananda meditated and attained enlightenment, alongside the 133-ft statue of saint-poet Thiruvalluvar.'
            },
            {
                'name': 'Bhagavathi Amman Temple (Devi Kanya Kumari)',
                'image': 'kanyakumari-rock-memorial.jpg',
                'image_alt': 'Historic Bhagavathi Amman temple sanctum in Kanyakumari',
                'caption': '3,000-Year-Old Devi Temple',
                'point': 'Ancient 3,000-year-old seashore shrine dedicated to the Virgin Goddess Kanya Kumari, famous for her diamond nose ring which is said to shine visibly across the sea.'
            },
            {
                'name': 'Triveni Sangam Beach & Sunset View Point',
                'image': 'kanyakumari-rock-memorial.jpg',
                'image_alt': 'Confluence of three oceans at Triveni Sangam beach with multi-colored sand',
                'caption': 'Triveni Three-Ocean Confluence',
                'point': 'The sacred point where the Arabian Sea, Indian Ocean, and Bay of Bengal converge, famed for multi-colored sands, glorious sunrise, and sunset over the ocean waters.'
            }
        ],
        'accommodation': {
            'night_stay': 'Kanyakumari',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Sea View / Hotel Sparsa / Hotel Tri Sea (or similar property)'
        },
        'meals': 'Lunch & Dinner (Breakfast if included in package)'
    },
    {
        'day': 9,
        'title': 'Kanyakumari to Trivandrum & Padmanabhaswamy Temple',
        'starting_point': 'Kanyakumari',
        'destination': 'Trivandrum',
        'intro': 'After breakfast, proceed towards Trivandrum. Visit the famous Sree Padmanabhaswamy Temple and explore the city. Later, enjoy some leisure time at Kovalam Beach.',
        'route_summary': 'Kanyakumari ➔ Suchindram Temple ➔ Trivandrum ➔ Sree Padmanabhaswamy Temple ➔ Kovalam Beach ➔ Trivandrum Hotel',
        'route_nodes': [
            {'name': 'Kanyakumari', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Suchindram Thanumalayan Temple', 'type': 'En Route Halt', 'badge_class': 'visit'},
            {'name': 'Sree Padmanabhaswamy Temple', 'type': 'Royal Darshan', 'badge_class': 'visit'},
            {'name': 'Kovalam Beach', 'type': 'Evening Leisure', 'badge_class': 'visit'},
            {'name': 'Trivandrum Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Sree Padmanabhaswamy Temple',
                'image': 'padmanabhaswamy_temple.jpg',
                'image_alt': 'Sree Padmanabhaswamy Temple in Trivandrum reflecting across the sacred pond',
                'caption': 'Grand Padmanabhaswamy Temple',
                'point': 'World-famous Kerala-Dravidian royal temple housing the magnificent 18-foot idol of Lord Vishnu reclining on Adisesha, observed through three sanctum doors.'
            },
            {
                'name': 'Kovalam Beach',
                'image': 'padmanabhaswamy_temple.jpg',
                'image_alt': 'Crescent coastline of Kovalam lighthouse beach with coconut palms',
                'caption': 'Kovalam Arabian Sea Coastline',
                'point': 'Famous crescent beach in Kerala shaded by thousands of coconut palms, ideal for relaxing by the Arabian Sea waves after temple darshan.'
            }
        ],
        'accommodation': {
            'night_stay': 'Trivandrum',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Apollo Dimora / Hotel SP Grand Days / Hotel Residency Tower (or similar property)'
        },
        'meals': 'Lunch & Dinner (Breakfast if included in package)'
    },
    {
        'day': 10,
        'title': 'Trivandrum to Madurai Scenic Return Drive',
        'starting_point': 'Trivandrum',
        'destination': 'Madurai',
        'intro': 'After breakfast, check out and begin your journey towards Madurai. Enjoy the scenic South Indian landscapes along the way. On arrival, check in to the hotel and relax.',
        'route_summary': 'Trivandrum ➔ Western Ghats Foothills ➔ Nagercoil ➔ Tirunelveli ➔ Madurai Hotel Check-in',
        'route_nodes': [
            {'name': 'Trivandrum Hotel', 'type': 'Checkout', 'badge_class': 'start'},
            {'name': 'Kerala-Tamil Nadu Interstate Highway', 'type': 'Scenic Transit', 'badge_class': 'visit'},
            {'name': 'Madurai Hotel Check-in', 'type': 'Arrival', 'badge_class': 'visit'},
            {'name': 'Madurai Local Markets', 'type': 'Shopping & Leisure', 'badge_class': 'visit'},
            {'name': 'Madurai Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Trivandrum to Madurai Highway',
                'image': 'madurai-meenakshi-temple.jpg',
                'image_alt': 'Scenic drive across Tamil Nadu plains and Western Ghats',
                'caption': 'Scenic Peninsular Highway Drive',
                'point': 'Traverse the scenic mountain gap between Kerala and Tamil Nadu, arriving in historic Madurai for evening leisure and souvenir shopping.'
            }
        ],
        'accommodation': {
            'night_stay': 'Madurai',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Royal Court / Hotel Supreme / Hotel Madurai Residency (or similar property)'
        },
        'meals': 'Lunch & Dinner (Breakfast if included in package)'
    },
    {
        'day': 11,
        'title': 'Madurai to Surat Return Journey by AC Train',
        'starting_point': 'Madurai Junction Station',
        'destination': 'Surat (En Route)',
        'intro': 'After breakfast, check out from the hotel and proceed to Madurai Railway Station. Begin your return journey to Surat by AC train.',
        'route_summary': 'Madurai Hotel Checkout ➔ Madurai Railway Station ➔ Return AC Train ➔ Interstate Journey',
        'route_nodes': [
            {'name': 'Madurai Hotel Checkout', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Madurai Junction Station', 'type': 'Boarding', 'badge_class': 'visit'},
            {'name': 'Return AC Train Interstate Journey', 'type': 'Journey', 'badge_class': 'visit'},
            {'name': 'Overnight AC Train', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Madurai Junction Railway Station Departure',
                'image': 'madurai-meenakshi-temple.jpg',
                'image_alt': 'Boarding return AC train from Madurai junction towards Gujarat',
                'caption': 'Boarding Return AC Train',
                'point': 'Board your reserved berths in the confirmed AC train towards Gujarat with warm coordinator assistance and railway meal service.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight AC Train',
            'type': 'Reserved AC Train Berth',
            'hotel_name': 'Indian Railways AC Express Train'
        },
        'meals': 'Lunch & Dinner on Train (Breakfast if included in package)'
    },
    {
        'day': 12,
        'title': 'Arrival at Surat Railway Station',
        'starting_point': 'Train Transit',
        'destination': 'Surat, Gujarat',
        'intro': 'Arrive at Surat and conclude your memorable Rameshwaram and South India pilgrimage tour with beautiful memories.',
        'route_summary': 'Western Railway Route ➔ Surat Railway Station (Tour Concludes)',
        'route_nodes': [
            {'name': 'Western Railway Route', 'type': 'Morning Journey', 'badge_class': 'start'},
            {'name': 'Surat Railway Station', 'type': 'Tour Concludes', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Surat Railway Station Arrival',
                'image': 'rameshwaram-temple.jpg',
                'image_alt': 'Arrival at Surat station carrying sacred Rameshwaram prasad and memories',
                'caption': 'Tour Concludes in Surat',
                'point': 'Arrive in Surat with the divine blessings of Lord Ramanatha Swamy, Meenakshi Amman, and Lord Padmanabha, carrying cherished memories for a lifetime.'
            }
        ],
        'accommodation': {
            'night_stay': 'Surat (Tour Concludes)',
            'type': 'Return to Home City',
            'hotel_name': 'Tour Concludes at Surat Railway Station'
        },
        'meals': 'Breakfast on Train (Lunch if included in package)'
    }
]

RAMESHWARAM_PACKAGE_DETAILS = {
    'inclusions': [
        'Confirmed AC Train tickets for Surat to Madurai and Madurai to Surat journeys (as per selected class).',
        '2 Nights accommodation in Madurai in vetted economy/deluxe hotel (triple-sharing basis).',
        '3 Nights accommodation in Rameshwaram close to Sri Ramanathaswamy Temple.',
        '2 Nights accommodation in Kanyakumari near Triveni Sangam seashore.',
        '1 Night accommodation in Trivandrum near temple and beach attractions.',
        '3 Nights comfortable overnight AC train journeys in reserved berths.',
        'Wholesome pure vegetarian lunch and dinner provided daily as per itinerary (Breakfast only if included in selected package).',
        'Dedicated AC 2x2 luxury coach / sanitized Tempo Traveller for all highway journeys, local sightseeing, and border transits.',
        'Excursions to Dhanushkodi, Arichal Munai, Tiruchendur Murugan Sea Temple, and Kovalam Beach.',
        'Experienced Swarnav tour coordinator accompanying the group from Surat for full trip support.',
        'Driver allowances, state road taxes, interstate permits, highway tolls, and vehicle parking charges.'
    ],
    'exclusions': [
        'Daily breakfast (unless explicitly opted and included in the selected package tier).',
        'Special VIP darshan tickets, quick darshan passes, and personal puja dakshina to priests or pandits.',
        'Special temple dress attire (traditional veshti/dhoti or angavastram required for entry at Padmanabhaswamy and Ramanathaswamy).',
        'Ferry tickets for Vivekananda Rock Memorial and Thiruvalluvar Statue in Kanyakumari (direct payment at ferry counter).',
        'Packaged mineral water bottles, tea/snacks outside the designated meal plan, and personal room service.',
        'Auto rickshaw / local shuttle fees where large tour coaches cannot enter narrow temple lanes.',
        'Personal laundry, luggage porter charges, and monument camera permits.',
        'GST and government travel taxes as applicable at billing.',
        'Any expenses arising from unforeseen delays, train rescheduling, strikes, or roadblocks.'
    ],
    'conditional_services': [
        {
            'service': 'Daily Breakfast Inclusion',
            'condition': 'Breakfast can be included in the package on prior selection/customization at the time of booking.'
        },
        {
            'service': '22 Holy Wells (Theertham Snan) Escort',
            'condition': 'Our tour coordinator assists groups through the 22 Kund snan sequence at Ramanathaswamy Temple with authorized temple assistants.'
        },
        {
            'service': 'Private Twin-Sharing Room',
            'condition': 'Standard package is triple-sharing (1 double bed + 1 extra mattress). Private twin-sharing room available on supplementary charge.'
        },
        {
            'service': 'Connecting Travel from Gujarat Cities',
            'condition': 'Pickup/drop connectivity from Ahmedabad, Vadodara, Rajkot, Bhavnagar, or Mumbai to Surat station can be seamlessly arranged.'
        }
    ],
    'important_notes': [
        'Temple Dress Code Strictness: Men must wear dhoti/veshti (or pyjama with shirt removed inside Padmanabhaswamy and Ramanathaswamy sanctums). Women must wear sarees or churidar with dupatta. Western attire (jeans, shorts) is strictly prohibited by temple trusts.',
        'Original Aadhaar Card or government-issued photo ID is mandatory for all passengers for train boarding and hotel check-in.',
        'Senior citizens are advised to carry walking sticks and lightweight slip-on footwear for temple walks.',
        'Electronic devices, mobile phones, cameras, and leather items are strictly prohibited inside Meenakshi Amman Temple and Sree Padmanabhaswamy Temple.'
    ]
}

RAMESHWARAM_STAY_AND_TRAVEL = {
    'accommodation': {
        'category': 'Deluxe & Economy Hotels in Madurai, Rameshwaram, Kanyakumari, and Trivandrum',
        'room_sharing': 'Triple-sharing basis (3 adults per room: 1 double bed + 1 comfortable extra mattress). Double/Twin sharing available on request with extra supplement.',
        'private_room': 'Private double-bed rooms can be arranged upon prior request subject to hotel availability and nominal additional tariff.',
        'hot_water': 'Running hot water or geyser facilities provided in all hotel rooms.',
        'remote_limitations': 'All properties are vetted for clean bedding, attached western-style bathrooms, reliable AC, and courteous hospitality.',
        'hotel_changes': 'If any listed property is unavailable due to operational reasons, a hotel of identical or higher category will be arranged.'
    },
    'meals': {
        'overview': 'Wholesome pure vegetarian lunch and dinner prepared daily according to the travel and excursion schedule.',
        'included_meals': 'Lunch and dinner provided according to the itinerary.',
        'breakfast_rule': 'Breakfast is provided only when explicitly included in the selected package.',
        'trek_days': 'On long transit days and excursions, hot meals, packed food or food vouchers will be coordinated.',
        'extra_refreshments': 'Extra snacks, packaged drinking water, South Indian filter coffee outside hotels, and personal beverages are paid directly by travellers.'
    },
    'transportation': {
        'main_mode': 'AC Train journeys + Dedicated AC Coach',
        'train_journey': 'Surat to Madurai and Madurai to Surat in confirmed AC class (3-Tier AC or Sleeper based on chosen tier).',
        'road_transport': 'Comfortable 2x2 luxury AC coach or sanitized Tempo Traveller with experienced drivers for Madurai, Rameshwaram, Dhanushkodi, Tiruchendur, Kanyakumari, and Trivandrum.',
        'local_transport': 'Local island shuttles used where large buses cannot enter narrow temple roads; ferry to Vivekananda Rock available at standard counter rates.',
        'pickup_drop': 'Surat Railway Station main assembly point with coordinator support.',
        'gujarat_travellers': 'Devotees from Ahmedabad, Vadodara, Rajkot, Surat, and Mumbai are supported with connecting train/flight bookings to merge with the main group.',
        'vehicle_allocation': 'Vehicle size (Force Urbania, Tempo Traveller, or 2x2 Deluxe Coach) is assigned according to the confirmed batch size.',
        'travel_time_notice': 'Travel times on Tamil Nadu and Kerala coastal highways can vary according to temple festival traffic, railway crossings, and tide conditions.'
    }
}

RAMESHWARAM_TRAVEL_GUIDE = {
    'age_restrictions': {
        'guidance': 'This tour is family-friendly and suitable for devotees of all age groups from children to senior citizens.',
        'advisory': 'The tour involves walking in temple corridors and queue lines. Wheelchair assistance and battery buggies are available at Ramanathaswamy Temple and Meenakshi Temple.',
        'safety_restriction': 'Travellers with difficulty walking should be accompanied by family members or opt for local helper assistance.'
    },
    'health_requirements': [
        'Travellers should be comfortable with long train journeys and warm coastal South Indian climate.',
        'Carry a sufficient personal supply of regular medicines (BP, diabetes, cardiac, arthritis).',
        'Keep body well hydrated with water, tender coconut water, and buttermilk during temple visits.',
        'Carry essential first aid: ORS packets, motion sickness pills, pain balms, and digestive tablets.'
    ],
    'documents_required': [
        'Original Aadhaar Card or Voter ID / Passport (mandatory for all travellers for train journey and hotel verification).',
        'Tour booking confirmation voucher and train e-tickets.',
        'Doctor’s emergency medical prescription for senior family members.'
    ],
    'items_to_carry': [
        'Traditional clothing: Traditional dhotis/veshtis for men (with angavastram), and sarees/churidars with dupattas for women.',
        'Extra set of quick-drying cotton clothes and small towel for the 22 holy wells (theertham snan) in Rameshwaram.',
        'Comfortable slip-on footwear or sandals that can be easily removed at temple footwear counters.',
        'Sun cap, sunglasses, cotton scarf, and umbrella for protection from tropical coastal sun.',
        'Power bank for mobile phones, extra camera batteries, and waterproof pouch for phones during holy baths.',
        'Sufficient cash for local temple coconut/flower offerings, priest dakshina, and souvenir shopping.'
    ],
    'packing_advice': 'Pack one sturdy trolley bag per person and one small day backpack for train transit and the 22 Kund holy snan in Rameshwaram.',
    'weather_info': 'South India coastal weather is pleasantly warm and tropical year-round (24°C to 34°C) with refreshing sea breezes in Rameshwaram and Kanyakumari. Light, breathable cotton clothing is recommended throughout the tour.'
}

RAMESHWARAM_POLICIES = {
    'booking_conditions': [
        'A 30% advance deposit per person is required to confirm railway berth reservations and hotel bookings.',
        'The remaining balance payment must be cleared at least 15 days prior to the scheduled departure date.',
        'Bookings made within 15 days of departure require 100% full payment at the time of reservation.',
        'Train seat allocation and berths are subject to Indian Railways passenger reservation quotas and availability.',
        'Aadhaar card details with correct full names and ages are mandatory at the time of booking for railway tickets.',
        'Hotel accommodation is provided on a triple-sharing basis (one double bed + one extra mattress) unless private room supplement is paid.',
        'The tour itinerary may be adapted or re-routed by the tour manager in case of temple festival crowds, train delays, or administrative guidelines.',
        'Bookings are confirmed only upon issuance of the official Swarnav booking voucher and receipt.'
    ],
    'cancellation_brackets': [
        {
            'timeline': '30 days or more before departure',
            'deduction': '10% of total package cost (plus Indian Railways cancellation deduction)',
            'refund_estimate': '90% of package cost (less railway cancellation fees)'
        },
        {
            'timeline': '16 to 29 days before departure',
            'deduction': '25% of total package cost (plus Indian Railways cancellation deduction)',
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
            'timeline': 'No-show or leaving the tour mid-way',
            'deduction': '100% of total package cost',
            'refund_estimate': 'No refund for unutilized services or hotel nights'
        }
    ],
    'cancellation_rules': [
        'All cancellation requests must be submitted in writing via registered WhatsApp or email to Swarnav Tour & Travels.',
        'Train ticket cancellation charges are governed strictly as per Indian Railways (IRCTC) standard refund policies.',
        'Approved refund amounts will be processed via original bank transfer within 7 to 15 working days.',
        'If the tour is disrupted due to extreme weather, train rescheduling, or government advisories, Swarnav will coordinate best available alternatives per hotel and transport partner rules.',
        'If Swarnav cancels the tour due to operational constraints, travellers will receive a 100% full refund or option to reschedule to another batch.'
    ]
}

RAMESHWARAM_NAV_TABS = [
    {'name': 'Overview', 'slug': 'overview', 'url_name': 'yatras:rameshwaram_overview'},
    {'name': '12-Day Itinerary', 'slug': 'itinerary', 'url_name': 'yatras:rameshwaram_itinerary'},
    {'name': 'Package Details', 'slug': 'package-details', 'url_name': 'yatras:rameshwaram_package_details'},
    {'name': 'Stay & Travel', 'slug': 'stay-and-travel', 'url_name': 'yatras:rameshwaram_stay_and_travel'},
    {'name': 'Travel Guide', 'slug': 'travel-guide', 'url_name': 'yatras:rameshwaram_travel_guide'},
    {'name': 'Policies', 'slug': 'policies', 'url_name': 'yatras:rameshwaram_policies'},
]

def get_rameshwaram_package():
    return RAMESHWARAM_PACKAGE

def get_rameshwaram_all_days():
    return RAMESHWARAM_ITINERARY_DAYS

def get_rameshwaram_day_by_number(day_number):
    for day in RAMESHWARAM_ITINERARY_DAYS:
        if day['day'] == day_number:
            return day
    return None

def get_rameshwaram_package_details():
    return RAMESHWARAM_PACKAGE_DETAILS

def get_rameshwaram_stay_and_travel():
    return RAMESHWARAM_STAY_AND_TRAVEL

def get_rameshwaram_travel_guide():
    return RAMESHWARAM_TRAVEL_GUIDE

def get_rameshwaram_policies():
    return RAMESHWARAM_POLICIES
