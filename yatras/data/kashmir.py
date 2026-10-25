"""
Verified source data for Kashmir Paradise & Mata Vaishno Devi Tour.
11-Day comprehensive itinerary covering Surat, Katra (Vaishno Devi), Shivkhori,
Srinagar, Sonmarg, Gulmarg, Pahalgam, Dal Lake, and Amritsar Golden Temple.
"""

KASHMIR_PACKAGE = {
    'slug': 'kashmir-paradise',
    'name': 'Kashmir Paradise & Mata Vaishno Devi Tour',
    'subtitle': 'Surat • Katra (Vaishno Devi) • Shivkhori • Srinagar • Sonmarg • Gulmarg • Pahalgam • Amritsar',
    'tagline': 'Divine & Scenic 11-Day Grand Tour: Vaishno Devi, Heaven on Earth Kashmir & Amritsar',
    'duration_days': 11,
    'duration_nights': 10,
    'duration_display': '11 Days / 10 Nights',
    'starting_city': 'Surat, Gujarat',
    'ending_city': 'Surat, Gujarat',
    'starting_price': '₹30,000',
    'price_display': 'Starting from ₹30,000 per person',
    'departures_summary': 'Opening New Batch in December (Dates Announced Soon)',
    'departures_guidance': 'Our next dedicated winter batch for Kashmir is opening in December. Exact travel dates are currently being finalized. Pre-register or call Swarnav now to reserve your family seats!',
    'batch_badge': 'Opening New Batch in December',
    'accommodation_summary': 'Deluxe & Economy hotels in Katra, Srinagar & Amritsar (Triple-sharing basis) + 2 Overnight AC Train journeys',
    'meals_summary': 'Lunch and dinner provided as per itinerary (Breakfast only if included in selected package)',
    'transport_summary': 'Surat to Katra & Amritsar to Surat AC train journeys + Dedicated AC 2x2 luxury coach / Tempo Traveller for entire J&K and Punjab transit',
    'confirmation_note': 'Package price, December departure schedule, and room availability require final written confirmation before booking.',
    'gujarat_support_note': 'Main departure starts at Surat Railway Station. Transportation arrangements to and from Surat can be arranged for devotees travelling from Ahmedabad, Vadodara, Rajkot, Mumbai, or anywhere in Gujarat & India (charges applicable).',

    'introduction': [
        "The Kashmir Paradise & Mata Vaishno Devi Tour brings together the supreme spiritual blessings of Maa Vaishno Devi and holy Shivkhori with the breathtaking winter wonderland of Kashmir — rightfully hailed as 'Paradise on Earth'.",
        "Beginning with an AC train journey from Surat, pilgrims arrive at Katra for the sacred darshan of Mata Vaishno Devi at Trikuta Hills and the ancient cave shrine of Lord Shiva at Shivkhori.",
        "The journey then winds through the magnificent Pir Panjal range into the Kashmir Valley, where travellers witness snow-draped Sonmarg (Meadow of Gold), the world-famous Gulmarg ski meadows with optional Gondola rides, the alpine pine forests and Lidder River of Pahalgam, and an enchanting Shikara ride across Srinagar's Dal Lake.",
        "Culminating with a serene visit to Sri Harmandir Sahib (The Golden Temple) in Amritsar, this 11-day tour offers a seamless blend of spirituality, snow-capped mountain beauty, Gujarati culinary comfort, and dedicated on-ground tour coordination."
    ],

    'dhams': [
        {
            'order': '1',
            'name': 'Mata Vaishno Devi Shrine',
            'significance': 'Sacred Holy Cave Shrine at Trikuta Hills',
            'description': 'Revered Shakti shrine in Katra where millions seek the divine blessings of Maha Kali, Maha Lakshmi, and Maha Saraswati in holy Pindi form.',
            'highlight': 'Supreme Shakti Darshan',
            'image': 'vaishno-devi-temple.jpg'
        },
        {
            'order': '2',
            'name': 'Shivkhori Holy Cave',
            'significance': 'Natural Svayambhu Shiva Lingam Cave',
            'description': 'Ancient natural cave shrine near Ransoo village dedicated to Lord Shiva, famous for its self-manifested lingam and limestone stalactites.',
            'highlight': 'Ancient Shiva Cave',
            'image': 'lakhamandal-temple.jpg'
        },
        {
            'order': '3',
            'name': 'Gulmarg & Sonmarg Valleys',
            'significance': 'Himalayan Snow Meadows & Highest Gondola',
            'description': 'Unrivaled alpine meadows surrounded by snow peaks, pine forests, Thajiwas glacier vistas, and the thrilling Gulmarg Gondola cable car.',
            'highlight': 'Winter Snow Paradise',
            'image': 'gulmarg-snow-meadows.jpg'
        },
        {
            'order': '4',
            'name': 'Pahalgam & Srinagar Dal Lake',
            'significance': 'Valley of Shepherds & Iconic Shikara Waterways',
            'description': 'Lush Lidder River valleys in Betaab Valley, historic Mughal Gardens of Nishat & Shalimar, and traditional wooden Shikara cruising on tranquil Dal Lake.',
            'highlight': 'Iconic Valley Charm',
            'image': 'dal-lake-shikara.jpg'
        },
        {
            'order': '5',
            'name': 'Sri Harmandir Sahib (Amritsar)',
            'significance': 'The Holiest Golden Temple Shrine',
            'description': 'The eternal abode of peace and brotherhood, illuminated in gold around the sacred Amrit Sarovar lake with 24-hour Guru Ka Langar.',
            'highlight': 'Spiritual Grand Finale',
            'image': 'amritsar-golden-temple.jpg'
        }
    ],

    'route_highlights': [
        'Surat', 'Katra', 'Mata Vaishno Devi', 'Shivkhori', 'Srinagar', 
        'Sonmarg', 'Gulmarg', 'Pahalgam', 'Dal Lake', 'Amritsar', 'Surat'
    ]
}

KASHMIR_ITINERARY_DAYS = [
    {
        'day': 1,
        'title': 'Surat to Katra by AC Train',
        'starting_point': 'Surat Railway Station',
        'destination': 'Katra (En Route)',
        'intro': 'Begin your Kashmir journey with an AC train journey from Surat to Katra. Enjoy the overnight train journey towards the beautiful Jammu & Kashmir region.',
        'route_summary': 'Surat Railway Station ➔ North India Rail Route ➔ Katra (Overnight AC Train)',
        'route_nodes': [
            {'name': 'Surat Railway Station', 'type': 'Starting Point', 'badge_class': 'start'},
            {'name': 'Western & Northern Rail Route', 'type': 'Transit', 'badge_class': 'visit'},
            {'name': 'Overnight AC Train', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Surat Railway Station Departure',
                'image': 'gulmarg-snow-meadows.jpg',
                'image_alt': 'Train journey departure from Surat station towards Katra',
                'caption': 'All Aboard for Kashmir & Vaishno Devi',
                'point': 'Board your reserved AC train berths at Surat with our dedicated tour coordinator assistance.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight AC Train',
            'type': 'Reserved AC Train Berth',
            'hotel_name': 'Indian Railways AC Express Train'
        },
        'meals': 'Dinner provided on Train'
    },
    {
        'day': 2,
        'title': 'Arrival at Katra & Hotel Check-in',
        'starting_point': 'Katra Railway Station',
        'destination': 'Katra',
        'intro': 'Arrive at Katra and transfer to the hotel. Complete the check-in formalities and relax after the journey. Evening is free for leisure and preparation for the Vaishno Devi Yatra.',
        'route_summary': 'Katra Railway Station ➔ Hotel Check-in ➔ Katra Local Area & Market ➔ Katra Hotel',
        'route_nodes': [
            {'name': 'Katra Station', 'type': 'Arrival', 'badge_class': 'start'},
            {'name': 'Hotel Check-in', 'type': 'Rest', 'badge_class': 'visit'},
            {'name': 'Katra Local Area & Market', 'type': 'Leisure', 'badge_class': 'visit'},
            {'name': 'Katra Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Katra Local Area & Market',
                'image': 'vaishno-devi-temple.jpg',
                'image_alt': 'Katra base camp town market at the foothills of Trikuta Mountains',
                'caption': 'Katra Foothills Town',
                'point': 'Bustling pilgrimage base camp town filled with prasad shops, dry fruit bazaars, and yatra registration centers.'
            }
        ],
        'accommodation': {
            'night_stay': 'Katra',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Katra Continental / Hotel The Vaishnodevi (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 3,
        'title': 'Mata Vaishno Devi Holy Darshan',
        'starting_point': 'Katra Hotel',
        'destination': 'Holy Bhawan & Katra',
        'intro': 'Early morning, begin your spiritual journey to Mata Vaishno Devi Bhawan. Complete the sacred darshan and return to Katra. Evening at leisure.',
        'route_summary': 'Katra ➔ Ban Ganga ➔ Ardhkuwari ➔ Holy Bhawan Darshan ➔ Bhairon Temple ➔ Katra Hotel',
        'route_nodes': [
            {'name': 'Ban Ganga Base', 'type': 'Trek Start', 'badge_class': 'start'},
            {'name': 'Ardhkuwari Cave', 'type': 'Midpoint', 'badge_class': 'visit'},
            {'name': 'Mata Vaishno Devi Bhawan', 'type': 'Sacred Darshan', 'badge_class': 'visit'},
            {'name': 'Bhairon Baba Temple', 'type': 'Ropeway Visit', 'badge_class': 'visit'},
            {'name': 'Katra Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Mata Vaishno Devi Temple',
                'image': 'vaishno-devi-temple.jpg',
                'image_alt': 'Mata Vaishno Devi Bhawan lit up at Trikuta hills Katra',
                'caption': 'Mata Vaishno Devi Sanctum Sanctorum',
                'point': 'World-revered holy cave shrine in Trikuta Hills where the three sacred Pindis of Maha Kali, Maha Lakshmi, and Maha Saraswati are enshrined.'
            },
            {
                'name': 'Ardhkuwari & Bhairon Ghati',
                'image': 'vaishno-devi-temple.jpg',
                'image_alt': 'Ardhkuwari cave shrine and Bhairon Baba ropeway',
                'caption': 'Sacred Ardhkuwari & Bhairon Temple',
                'point': 'Historic pilgrimage halts along the sacred 13-km path with battery-car and ropeway access available.'
            }
        ],
        'accommodation': {
            'night_stay': 'Katra',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Katra Continental / Hotel The Vaishnodevi (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 4,
        'title': 'Excursion to Holy Shivkhori Cave Shrine',
        'starting_point': 'Katra',
        'destination': 'Shivkhori & Katra',
        'intro': 'After breakfast, proceed towards Shivkhori, a famous holy cave shrine dedicated to Lord Shiva. Enjoy the spiritual experience and return to Katra.',
        'route_summary': 'Katra Hotel ➔ Reasi Hills ➔ Ransoo Base Village ➔ Shivkhori Cave Darshan ➔ Katra Hotel',
        'route_nodes': [
            {'name': 'Katra', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Reasi Scenic Route', 'type': 'Transit', 'badge_class': 'visit'},
            {'name': 'Shivkhori Holy Cave', 'type': 'Shiva Darshan', 'badge_class': 'visit'},
            {'name': 'Katra Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Shivkhori',
                'image': 'lakhamandal-temple.jpg',
                'image_alt': 'Shivkhori ancient Shiva cave temple in Jammu',
                'caption': 'Svayambhu Shiva Cave Shrine',
                'point': 'A 200-meter-long natural limestone cave housing a 4-foot natural Svayambhu Shiva Lingam constantly dripping with natural water.'
            }
        ],
        'accommodation': {
            'night_stay': 'Katra',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Katra Continental / Hotel The Vaishnodevi (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 5,
        'title': 'Scenic Mountain Journey from Katra to Srinagar',
        'starting_point': 'Katra',
        'destination': 'Srinagar',
        'intro': 'After breakfast, check out from the hotel and begin your scenic journey from Katra to Srinagar. Enjoy beautiful mountain landscapes along the way. On arrival, check in to the Srinagar hotel and relax.',
        'route_summary': 'Katra ➔ Udhampur ➔ Chenani-Nashri Tunnel ➔ Banihal Tunnel ➔ Qazigund ➔ Srinagar Hotel',
        'route_nodes': [
            {'name': 'Katra Hotel Checkout', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Chenani-Nashri Tunnel', 'type': 'Engineering Marvel', 'badge_class': 'visit'},
            {'name': 'Banihal Pir Panjal Pass', 'type': 'Gateway to Kashmir', 'badge_class': 'visit'},
            {'name': 'Srinagar Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Katra to Srinagar Highway & Chenani-Nashri Tunnel',
                'image': 'kashmir-valley.jpg',
                'image_alt': 'Scenic mountain highway from Jammu into Kashmir valley',
                'caption': 'Scenic Himalayan Mountain Highway',
                'point': 'Pass through India’s longest road tunnel and traverse the majestic Pir Panjal mountain range into the emerald Kashmir valley.'
            },
            {
                'name': 'Srinagar Valley Arrival',
                'image': 'dal-lake-shikara.jpg',
                'image_alt': 'Welcoming sunset over Srinagar valley and Dal Lake',
                'caption': 'Welcome to Srinagar (Paradise on Earth)',
                'point': 'Check in to your hotel in Srinagar, enjoy traditional warm Kashmiri hospitality, and rest for the excursions ahead.'
            }
        ],
        'accommodation': {
            'night_stay': 'Srinagar',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Grand Habib / Royal Batoo / Hotel Solar Residency (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 6,
        'title': 'Full-Day Excursion to Sonmarg (Meadow of Gold)',
        'starting_point': 'Srinagar',
        'destination': 'Sonmarg & Srinagar',
        'intro': 'After breakfast, proceed for a full-day excursion to Sonmarg, known for its breathtaking Himalayan landscapes. Enjoy the beautiful valleys, mountains and scenic surroundings before returning to Srinagar.',
        'route_summary': 'Srinagar ➔ Wayil Bridge ➔ Sindh River Valley ➔ Sonmarg Meadows ➔ Thajiwas Glacier View ➔ Srinagar Hotel',
        'route_nodes': [
            {'name': 'Srinagar Hotel', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Sindh Valley Scenic Drive', 'type': 'Transit', 'badge_class': 'visit'},
            {'name': 'Sonmarg Golden Meadow', 'type': 'Sightseeing', 'badge_class': 'visit'},
            {'name': 'Thajiwas Glacier Point', 'type': 'Excursion', 'badge_class': 'visit'},
            {'name': 'Srinagar Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Sonmarg',
                'image': 'sonmarg-glacier-valley.jpg',
                'image_alt': 'Sonmarg alpine valley with snow-capped Himalayan peaks and Thajiwas glacier',
                'caption': 'Sonmarg - The Golden Meadow',
                'point': 'Magnificent alpine valley at 2,740 m altitude surrounded by pine forests, roaring Sindh River, and snow-clad Himalayan peaks.'
            },
            {
                'name': 'Local Sightseeing & Thajiwas Glacier View',
                'image': 'sonmarg-glacier-valley.jpg',
                'image_alt': 'Pony ride track leading towards Thajiwas Glacier in Sonmarg',
                'caption': 'Thajiwas Glacier Excursion',
                'point': 'Visitors can take an optional pony ride or scenic snow walk up to the foot of Thajiwas Glacier (optional, direct payment).'
            }
        ],
        'accommodation': {
            'night_stay': 'Srinagar',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Grand Habib / Royal Batoo / Hotel Solar Residency (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 7,
        'title': 'Full-Day Excursion to Gulmarg & Gondola Snow Meadows',
        'starting_point': 'Srinagar',
        'destination': 'Gulmarg & Srinagar',
        'intro': "After breakfast, proceed to Gulmarg, one of Kashmir's most beautiful destinations. Enjoy the spectacular mountain scenery and lush meadows. Optional activities such as the Gondola ride can be enjoyed at an additional cost. Return to Srinagar in the evening.",
        'route_summary': 'Srinagar ➔ Tangmarg Pine Slopes ➔ Gulmarg Meadows ➔ Gondola Cable Car ➔ Srinagar Hotel',
        'route_nodes': [
            {'name': 'Srinagar', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Tangmarg', 'type': 'Pine Ascent', 'badge_class': 'visit'},
            {'name': 'Gulmarg Town & Golf Course', 'type': 'Meadows', 'badge_class': 'visit'},
            {'name': 'Gulmarg Gondola Base', 'type': 'Cable Car Peak', 'badge_class': 'visit'},
            {'name': 'Srinagar Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Gulmarg',
                'image': 'gulmarg-snow-meadows.jpg',
                'image_alt': 'Gulmarg snow-covered meadows and pine slopes with Gondola line',
                'caption': 'Gulmarg - Meadow of Flowers & Snow',
                'point': 'Internationally acclaimed hill station situated at 2,650 m with vast alpine meadows and panoramic views of Mount Nanga Parbat.'
            },
            {
                'name': 'Gulmarg Meadows & Gondola Area',
                'image': 'gulmarg-snow-meadows.jpg',
                'image_alt': 'Gulmarg Gondola cable car ascending towards Apharwat Peak',
                'caption': 'World Famous Gulmarg Gondola',
                'point': 'Ride the world’s second-highest operating cable car to Kongdoori (Phase 1) and Apharwat Peak (Phase 2) for breathtaking snow sports and views.'
            }
        ],
        'accommodation': {
            'night_stay': 'Srinagar',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Grand Habib / Royal Batoo / Hotel Solar Residency (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 8,
        'title': 'Full-Day Excursion to Pahalgam (Valley of Shepherds)',
        'starting_point': 'Srinagar',
        'destination': 'Pahalgam & Srinagar',
        'intro': 'After breakfast, proceed for a full-day excursion to Pahalgam. Enjoy the beautiful valleys, pine forests, rivers and breathtaking Himalayan scenery. Explore the local sightseeing points before returning to Srinagar.',
        'route_summary': 'Srinagar ➔ Pampore Saffron Fields ➔ Awantipora Ruins ➔ Anantnag ➔ Pahalgam Valley ➔ Srinagar Hotel',
        'route_nodes': [
            {'name': 'Srinagar', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Pampore Saffron Town', 'type': 'En Route Halt', 'badge_class': 'visit'},
            {'name': 'Pahalgam Town & Lidder River', 'type': 'Valley Excursion', 'badge_class': 'visit'},
            {'name': 'Betaab Valley & Local Sightseeing', 'type': 'Scenic Point', 'badge_class': 'visit'},
            {'name': 'Srinagar Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Pahalgam & Lidder River',
                'image': 'pahalgam-betaab-valley.jpg',
                'image_alt': 'Pahalgam river and pine valley with mountains',
                'caption': 'Pahalgam - Valley of Shepherds',
                'point': 'Serene mountain resort at the confluence of the Lidder and Sheshnag streams, celebrated for pristine air, pine woods, and trout streams.'
            },
            {
                'name': 'Betaab Valley / Local Sightseeing',
                'image': 'pahalgam-betaab-valley.jpg',
                'image_alt': 'Betaab Valley in Pahalgam with verdant meadows and mountain peaks',
                'caption': 'Betaab Valley & Local Points',
                'point': 'Famous scenic shooting valley named after the Bollywood hit Betaab, offering picture-postcard views of snow ranges and weeping willows.'
            }
        ],
        'accommodation': {
            'night_stay': 'Srinagar',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Grand Habib / Royal Batoo / Hotel Solar Residency (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 9,
        'title': 'Srinagar Local Sightseeing, Mughal Gardens & Dal Lake',
        'starting_point': 'Srinagar Hotel',
        'destination': 'Srinagar',
        'intro': 'After breakfast, explore the beautiful city of Srinagar. Visit the famous Dal Lake, Mughal Gardens and other local attractions. Enjoy the scenic beauty of Kashmir and spend some time exploring the local markets.',
        'route_summary': 'Srinagar Hotel ➔ Dal Lake Shikara ➔ Nishat Bagh ➔ Shalimar Bagh ➔ Shankaracharya Temple ➔ Kashmiri Bazaars',
        'route_nodes': [
            {'name': 'Dal Lake Shikara Ghat', 'type': 'Waterway Cruise', 'badge_class': 'start'},
            {'name': 'Nishat Garden (Garden of Bliss)', 'type': 'Mughal Heritage', 'badge_class': 'visit'},
            {'name': 'Shalimar Garden (Abode of Love)', 'type': 'Mughal Heritage', 'badge_class': 'visit'},
            {'name': 'Srinagar Local Bazaars', 'type': 'Shopping & Leisure', 'badge_class': 'visit'},
            {'name': 'Srinagar Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Dal Lake Shikara Ride',
                'image': 'dal-lake-shikara.jpg',
                'image_alt': 'Traditional decorated Shikara boat on tranquil Dal Lake Srinagar',
                'caption': 'Romantic Dal Lake Shikara Ride',
                'point': 'Experience an unforgettable hour-long glide on a traditional wooden Shikara past floating flower gardens and Char Chinar.'
            },
            {
                'name': 'Nishat Garden & Shalimar Garden',
                'image': 'dal-lake-shikara.jpg',
                'image_alt': 'Terraced Mughal Gardens Nishat and Shalimar in Srinagar',
                'caption': 'Historic Royal Mughal Gardens',
                'point': 'Centuries-old terraced gardens built by Emperor Jahangir and Asif Khan with gushing water channels and majestic Chinar trees.'
            },
            {
                'name': 'Srinagar Local Sightseeing & Markets',
                'image': 'kashmir-valley.jpg',
                'image_alt': 'Kashmiri handicrafts, pashmina shawls, and dry fruit shops',
                'caption': 'Kashmiri Handicrafts & Dry Fruits',
                'point': 'Browse Lal Chowk and local markets for authentic saffron, walnut kernels, almonds, embroidered Pashmina shawls, and Kashmiri kahwa.'
            }
        ],
        'accommodation': {
            'night_stay': 'Srinagar',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Grand Habib / Royal Batoo / Hotel Solar Residency (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 10,
        'title': 'Scenic Journey from Srinagar to Amritsar & Golden Temple',
        'starting_point': 'Srinagar',
        'destination': 'Amritsar',
        'intro': 'After breakfast, check out from the hotel and begin your journey from Srinagar to Amritsar. Enjoy the scenic journey and arrive in Amritsar. Evening at leisure.',
        'route_summary': 'Srinagar ➔ Jammu Highway ➔ Pathankot ➔ Amritsar Hotel Check-in ➔ Sri Harmandir Sahib (Golden Temple)',
        'route_nodes': [
            {'name': 'Srinagar Hotel Checkout', 'type': 'Departure', 'badge_class': 'start'},
            {'name': 'Jammu & Punjab Highway', 'type': 'Scenic Transit', 'badge_class': 'visit'},
            {'name': 'Amritsar Hotel Check-in', 'type': 'Arrival', 'badge_class': 'visit'},
            {'name': 'Sri Harmandir Sahib (Golden Temple)', 'type': 'Sacred Darshan', 'badge_class': 'visit'},
            {'name': 'Amritsar Hotel', 'type': 'Night Stay', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Srinagar to Amritsar Journey',
                'image': 'amritsar-golden-temple.jpg',
                'image_alt': 'Scenic road journey descending into the fertile plains of Punjab',
                'caption': 'Scenic Transit to Amritsar',
                'point': 'Travel through Jammu and Punjab into the spiritual heartland of Amritsar, checking in to your comfortable hotel.'
            },
            {
                'name': 'Sri Harmandir Sahib (Golden Temple)',
                'image': 'amritsar-golden-temple.jpg',
                'image_alt': 'Golden Temple illuminated in gold at night across the Amrit Sarovar',
                'caption': 'Illuminated Sri Harmandir Sahib',
                'point': 'Evening visit to the holiest Sikh gurudwara, illuminated in pure gold with soul-stirring Gurbani kirtan and holy Amrit Sarovar parikrama.'
            }
        ],
        'accommodation': {
            'night_stay': 'Amritsar',
            'type': 'Deluxe / Economy Hotel',
            'hotel_name': 'Hotel Sapphire / Hotel Golden Tulip / Hotel City Park (or similar property)'
        },
        'meals': 'Lunch & Dinner'
    },
    {
        'day': 11,
        'title': 'Amritsar to Surat Return Journey by AC Train',
        'starting_point': 'Amritsar Railway Station',
        'destination': 'Surat, Gujarat',
        'intro': 'After breakfast, complete your return journey from Amritsar to Surat by AC train, carrying beautiful memories of your Kashmir adventure.',
        'route_summary': 'Amritsar Hotel Checkout ➔ Amritsar Railway Station ➔ Return AC Train ➔ Surat, Gujarat',
        'route_nodes': [
            {'name': 'Amritsar Hotel', 'type': 'Checkout', 'badge_class': 'start'},
            {'name': 'Amritsar Railway Station', 'type': 'Boarding', 'badge_class': 'visit'},
            {'name': 'AC Train Interstate Transit', 'type': 'Journey', 'badge_class': 'visit'},
            {'name': 'Surat, Gujarat', 'type': 'Tour Concludes', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Amritsar to Surat Return Train',
                'image': 'amritsar-golden-temple.jpg',
                'image_alt': 'Return train journey carrying cherished memories of Kashmir and Vaishno Devi',
                'caption': 'Return Home with Cherished Memories',
                'point': 'Board your scheduled return AC train from Amritsar to Surat carrying unforgettable memories, blessings of Maa Vaishno Devi, and winter stories of Kashmir.'
            }
        ],
        'accommodation': {
            'night_stay': 'Overnight AC Train',
            'type': 'Reserved AC Train Berth',
            'hotel_name': 'Indian Railways AC Express Train'
        },
        'meals': 'Lunch & Dinner on Train (Breakfast if included in package)'
    }
]

KASHMIR_PACKAGE_DETAILS = {
    'inclusions': [
        'Confirmed AC Train tickets for Surat to Katra and Amritsar to Surat journeys (as per selected class).',
        '3 Nights accommodation in Katra in clean, vetted economy/deluxe hotel (triple-sharing basis).',
        '5 Nights accommodation in Srinagar in verified premium hotel with mountain & valley vistas.',
        '1 Night accommodation in Amritsar close to Sri Harmandir Sahib (Golden Temple).',
        '2 Nights comfortable overnight AC train journeys in reserved berths.',
        'Wholesome pure vegetarian lunch and dinner provided daily as per itinerary (Breakfast only if included in selected package).',
        'Dedicated AC 2x2 luxury coach / sanitized Tempo Traveller for all highway journeys, local sightseeing, and border transits.',
        'Traditional 1-hour Shikara ride on Srinagar’s world-famous Dal Lake.',
        'Excursions to Sonmarg (Meadow of Gold), Gulmarg (Snow Meadows), and Pahalgam (Betaab Valley).',
        'Experienced Swarnav tour coordinator accompanying the group from Surat for full trip support.',
        'Driver allowances, state road taxes, interstate permits, highway tolls, and vehicle parking charges.'
    ],
    'exclusions': [
        'Gulmarg Gondola cable car ride tickets (Phase 1 & Phase 2 must be booked directly online via J&K Cable Car Portal).',
        'Pony / horse / palki / pitthu / battery car charges at Vaishno Devi, Shivkhori, Sonmarg, Gulmarg, or Pahalgam.',
        'Union taxi charges inside Pahalgam (Betaab Valley / Aru / Chandanwari) as outside vehicles are restricted by local union.',
        'Monument, garden entry fees, museum passes, and personal photography permits.',
        'Special VIP darshan tickets, personal puja rituals, and dakshina to priests or pandits.',
        'Daily breakfast (unless explicitly opted and included in the selected package tier).',
        'Packaged mineral water bottles, tea/snacks outside the designated meal plan, and personal room service.',
        'Winter clothing rental charges (gum boots, snow overcoats, gloves at Tangmarg/Gulmarg).',
        'GST and government travel taxes as applicable at billing.',
        'Any expenses arising from unforeseen delays, train rescheduling, snow landslides, roadblocks, or flight diversions.'
    ],
    'conditional_services': [
        {
            'service': 'Vaishno Devi Helicopter / Battery Car / Ropeway',
            'condition': 'Available directly through the Shri Mata Vaishno Devi Shrine Board (SMVDSB) website. Our tour coordinator assists senior pilgrims with registration and boarding.'
        },
        {
            'service': 'Gulmarg Gondola Booking',
            'condition': 'Gondola tickets should be booked at least 15–30 days in advance via the official J&K tourism portal due to heavy winter demand.'
        },
        {
            'service': 'Private Twin-Sharing Room',
            'condition': 'Standard package is triple-sharing (1 double bed + 1 extra mattress). Private twin-sharing room available on supplementary charge.'
        },
        {
            'service': 'Connecting Travel from Gujarat Cities',
            'condition': 'Pickup/drop connectivity from Ahmedabad, Vadodara, Rajkot, Bhavnagar, or Mumbai to Surat station can be seamlessly arranged.'
        },
        {
            'service': 'Daily Breakfast Inclusion',
            'condition': 'Breakfast can be included in the package on prior selection/customization at the time of booking.'
        }
    ],
    'important_notes': [
        'December is winter in Kashmir: heavy woolens, thermal inners, snow caps, mufflers, and sturdy walking shoes are mandatory.',
        'Original Aadhaar Card or government-issued photo ID is mandatory for all passengers for train boarding and hotel check-in.',
        'Senior citizens planning the Vaishno Devi yatra are advised to carry walking sticks and pre-book battery cars or ponies if required.',
        'Mobile postpaid connections (Jio, Airtel, BSNL) work across Jammu & Kashmir. Prepaid SIM cards from other states do not work in J&K due to national security norms.'
    ]
}

KASHMIR_STAY_AND_TRAVEL = {
    'accommodation': {
        'category': 'Deluxe & Economy Hotels in Katra, Srinagar, and Amritsar',
        'room_sharing': 'Triple-sharing basis (3 adults per room: 1 double bed + 1 comfortable extra mattress). Double/Twin sharing available on request with extra supplement.',
        'private_room': 'Private double-bed rooms can be arranged upon prior request subject to hotel availability and nominal additional tariff.',
        'hot_water': 'Running hot water or geyser facilities provided in all hotel rooms, essential for winter mountain temperatures.',
        'remote_limitations': 'All properties are vetted for clean bedding, western-style bathrooms, reliable heating/electric blankets, and courteous hospitality.',
        'hotel_changes': 'If any listed property is unavailable due to operational reasons, a hotel of identical or higher category will be arranged.'
    },
    'meals': {
        'overview': 'Wholesome pure vegetarian lunch and dinner prepared daily according to the travel and excursion schedule.',
        'included_meals': 'Lunch and dinner provided according to the itinerary.',
        'breakfast_rule': 'Breakfast is provided only when explicitly included in the selected package.',
        'trek_days': 'On long transit days and excursions, hot meals, packed food or food vouchers will be coordinated.',
        'extra_refreshments': 'Extra snacks, packaged drinking water, tea, and personal beverages are not included and must be arranged individually.'
    },
    'transportation': {
        'main_mode': 'AC Train journeys + Dedicated Mountain Coach',
        'train_journey': 'Surat to Katra and Amritsar to Surat in confirmed AC class (3-Tier AC or Sleeper based on chosen tier).',
        'road_transport': 'Comfortable 2x2 luxury AC coach or Tempo Traveller with experienced hill drivers for Katra, Srinagar, Sonmarg, Gulmarg, Pahalgam, and Amritsar.',
        'local_transport': 'Shikara boats on Dal Lake included; local union cabs and ponies for remote glacier view points available at standard local rates.',
        'pickup_drop': 'Surat Railway Station main assembly point with coordinator support.',
        'gujarat_travellers': 'Devotees from Ahmedabad, Vadodara, Rajkot, Surat, and Mumbai are supported with connecting train/flight bookings to merge with the main group.',
        'vehicle_allocation': 'Vehicle size (Force Urbania, Tempo Traveller, or 2x2 Deluxe Coach) is assigned according to the confirmed batch size.',
        'travel_time_notice': 'Travel times on Jammu–Srinagar highway can vary according to winter weather conditions, tunnel clearances, and traffic controls.'
    }
}

KASHMIR_TRAVEL_GUIDE = {
    'age_restrictions': {
        'guidance': 'This tour is family-friendly and suitable for all age groups from children to senior citizens.',
        'advisory': 'The Vaishno Devi darshan involves trekking or pony rides; seniors can comfortably use battery cars or the ropeway from Bhawan to Bhairon Ghati.',
        'safety_restriction': 'Travellers with severe asthma or cardiovascular issues should consult their physician before undertaking high-altitude cable car rides at Gulmarg Phase 2.'
    },
    'health_requirements': [
        'Travellers should be prepared for cold winter conditions in Kashmir in December.',
        'Carry a sufficient 15-day personal supply of regular medicines (BP, diabetes, cardiac, arthritis).',
        'Carry cold-weather essentials: lip balm, petroleum jelly, moisturizers, pain sprays, and digestive tablets.',
        'Keep body hydrated with warm water, herbal teas, or Kashmiri Kahwa during mountain road transits.'
    ],
    'documents_required': [
        'Original Aadhaar Card or Voter ID / Passport (mandatory for all travellers for train journey and hotel verification).',
        'Shri Mata Vaishno Devi Shrine Board Yatra Parchi / RFID card (collected at Katra base).',
        'Pre-booked Gulmarg Gondola e-tickets (if Phase 1/Phase 2 booked in advance).',
        'Doctor’s emergency medical prescription for senior family members.'
    ],
    'items_to_carry': [
        'Heavy winter jacket / padded snow parka, windproof outer layer, and thermal innerwear (at least 2–3 pairs).',
        'Woolen sweaters, fleece jackets, woolen beanies/monkey caps, neck mufflers, and insulated snow gloves.',
        'Comfortable walking shoes with good grip and 4–5 pairs of warm woolen socks.',
        'Postpaid mobile SIM (Airtel / Jio / BSNL) — Prepaid non-J&K SIM cards do not receive network coverage in Jammu & Kashmir.',
        'Power bank for smartphones, extra camera batteries, and waterproof pouch for mobile phones.',
        'Sufficient cash for local pony rides, union taxis, dry fruits, and handicraft shopping.'
    ],
    'packing_advice': 'Pack one sturdy trolley bag per person with warm layers and one small day backpack for train journeys, Shikara rides, and the Vaishno Devi trek.',
    'weather_info': 'December in Kashmir brings delightful winter chill and the onset of fresh snowfall! Katra experiences cool temperatures (8°C to 18°C), while Srinagar, Gulmarg, and Sonmarg experience cold winter weather (-2°C to 10°C). Warm woolen clothing is essential throughout the tour.'
}

KASHMIR_POLICIES = {
    'booking_conditions': [
        'A 30% advance deposit per person is required to confirm railway berth reservations and hotel bookings.',
        'The remaining balance payment must be cleared at least 15 days prior to the scheduled departure date.',
        'Bookings made within 15 days of departure require 100% full payment at the time of reservation.',
        'Train seat allocation and berths are subject to Indian Railways passenger reservation quotas and availability.',
        'Aadhaar card details with correct full names and ages are mandatory at the time of booking for railway tickets.',
        'Hotel accommodation is provided on a triple-sharing basis (one double bed + one extra mattress) unless private room supplement is paid.',
        'The tour itinerary may be adapted or re-routed by the tour manager in case of heavy snowfall, highway roadblocks, or local administrative guidelines.',
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
        'If the tour is disrupted due to extreme weather, sudden natural roadblocks, or government advisories, Swarnav will coordinate best available alternatives per hotel and transport partner rules.',
        'If Swarnav cancels the tour due to operational constraints, travellers will receive a 100% full refund or option to reschedule to another batch.'
    ]
}

KASHMIR_NAV_TABS = [
    {'name': 'Overview', 'slug': 'overview', 'url_name': 'yatras:kashmir_overview'},
    {'name': '11-Day Itinerary', 'slug': 'itinerary', 'url_name': 'yatras:kashmir_itinerary'},
    {'name': 'Package Details', 'slug': 'package-details', 'url_name': 'yatras:kashmir_package_details'},
    {'name': 'Stay & Travel', 'slug': 'stay-and-travel', 'url_name': 'yatras:kashmir_stay_and_travel'},
    {'name': 'Travel Guide', 'slug': 'travel-guide', 'url_name': 'yatras:kashmir_travel_guide'},
    {'name': 'Policies', 'slug': 'policies', 'url_name': 'yatras:kashmir_policies'},
]

def get_kashmir_package():
    return KASHMIR_PACKAGE

def get_kashmir_all_days():
    return KASHMIR_ITINERARY_DAYS

def get_kashmir_day_by_number(day_number):
    for day in KASHMIR_ITINERARY_DAYS:
        if day['day'] == day_number:
            return day
    return None

def get_kashmir_package_details():
    return KASHMIR_PACKAGE_DETAILS

def get_kashmir_stay_and_travel():
    return KASHMIR_STAY_AND_TRAVEL

def get_kashmir_travel_guide():
    return KASHMIR_TRAVEL_GUIDE

def get_kashmir_policies():
    return KASHMIR_POLICIES
