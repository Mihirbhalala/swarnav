"""
Source data for Kerala Tour Package (God's Own Country - 13 Days / 12 Nights).
Starting From ₹32,000/- Per Person.
Tour Origin & Return: Surat, Gujarat (with pan-Gujarat/India connectivity).
Meal Policy: Pure vegetarian lunch & dinner provided as per itinerary (Breakfast only if included in selected package).
"""

KERALA_PACKAGE = {
    'slug': 'kerala-tour',
    'name': 'Kerala Tour (God’s Own Country)',
    'tagline': 'Munnar Hills • Thekkady Wildlife • Alleppey Houseboat • Kovalam Beach • Fort Kochi',
    'region': 'South India (Kerala)',
    'duration_days': 13,
    'duration_nights': 12,
    'duration_display': '13 Days / 12 Nights',
    'starting_price': '₹32,000',
    'price_display': 'Starting from ₹32,000 per person',
    'price_note': 'per person (Triple-sharing basis)',
    'starting_city': 'Surat, Gujarat',
    'ending_city': 'Surat, Gujarat',
    'origin': 'Starts & Ends in Surat, Gujarat',
    'status': 'upcoming',
    'status_label': 'Upcoming Tour (Dates Announced Soon)',
    'image': 'images/kerala-backwaters.jpg',
    'departures_summary': 'Next departure date is not confirmed yet. Inquiries open.',
    'departures_guidance': 'Next Kerala tour date is not confirmed yet. Please contact our coordination team at +91 95868 25353 or on WhatsApp for upcoming batch updates.',
    'accommodation_summary': 'Deluxe hill resort in Munnar, nature hotel in Thekkady, traditional deluxe Kerala houseboat in Alleppey backwaters, beach hotel in Kovalam, city hotel in Kochi, and 4 nights in comfortable AC train berths.',
    'meals_summary': 'Wholesome pure vegetarian lunch and dinner prepared with Gujarati and North Indian taste preferences. Breakfast is provided if included in your selected package tier.',
    'transport_summary': 'Round-trip confirmed AC train travel (Surat to Kerala & Kochi to Surat) plus a dedicated air-conditioned coach for all mountain, forest, backwater, and coastal sightseeing.',
    'confirmation_note': 'Written booking voucher and confirmed train PNR will be issued within 24 hours of advance token confirmation.',
    'gujarat_support_note': 'Our tour managers escort the group from Surat station. Assistance is available for connecting passengers from Ahmedabad, Vadodara, and Mumbai.',
    'introduction': [
        "Welcome to Kerala — famously revered as 'God's Own Country'. This 13-day grand journey brings together the misty emerald tea hills of Munnar, aromatic spice plantations and Periyar wildlife sanctuary in Thekkady, the world-famous backwater houseboat cruise in Alleppey, golden crescent beaches in Kovalam, sacred darshan at Sree Padmanabhaswamy Temple, and colonial maritime charm in Fort Kochi.",
        "Starting and concluding seamlessly at Surat with confirmed AC train transit, this tour is designed for families, nature lovers, and senior citizens seeking relaxation, spiritual blessings, and natural splendor without transit stress.",
        "Every aspect of your trip — from pure vegetarian satvik meals to verified hotels, traditional backwater cruising, and on-ground tour coordinator support — is thoughtfully arranged by Swarnav Tour & Travels."
    ],
    'route_highlights': [
        'Surat',
        'Munnar',
        'Thekkady (Periyar)',
        'Alleppey (Backwaters)',
        'Kovalam',
        'Trivandrum',
        'Fort Kochi',
        'Surat'
    ],
    'highlights': [
        'Lush emerald green tea gardens and mountain viewpoints in Munnar (3 Nights)',
        'Mattupetty Dam, Echo Point, and scenic Kundala Lake',
        'Thekkady spice plantations and Periyar Wildlife Sanctuary forest area (2 Nights)',
        'Traditional Kerala Houseboat cruise through tranquil Alleppey backwaters (1 Night)',
        'Sun-kissed Kovalam Beach and historic Sree Padmanabhaswamy Temple in Trivandrum (2 Nights)',
        'Historic Fort Kochi heritage walk, St. Francis Church & iconic Chinese Fishing Nets',
        'Round-trip confirmed AC train journeys from Surat with dedicated AC bus coach in Kerala',
        'Pure veg lunch and dinner provided daily (Breakfast if included in package)'
    ],
    'dhams': [
        {
            'order': 1,
            'name': 'Munnar Hill Station',
            'significance': 'Western Ghats Tea Paradise',
            'description': 'Perched at 1,600 metres above sea level, Munnar features sprawling tea gardens, cascading waterfalls, misty mountain peaks, and refreshingly cool weather.',
            'highlight': 'Mattupetty Dam & Tea Plantations',
            'image': 'images/munnar-tea-gardens.jpg'
        },
        {
            'order': 2,
            'name': 'Thekkady & Periyar',
            'significance': 'Spice Capital & Wildlife Sanctuary',
            'description': 'Home to aromatic cardamom, pepper, and cinnamon plantations alongside the Periyar Tiger Reserve surrounding the serene Periyar Lake.',
            'highlight': 'Periyar Lake & Spice Markets',
            'image': 'images/thekkady-periyar-lake.jpg'
        },
        {
            'order': 3,
            'name': 'Alleppey Backwaters',
            'significance': 'Venice of the East',
            'description': 'A breathtaking network of tranquil lagoons, palm-fringed canals, and Vembanad Lake experienced aboard a traditional thatched-roof Kerala Houseboat.',
            'highlight': 'Overnight Houseboat Backwater Cruise',
            'image': 'images/kerala-backwaters.jpg'
        },
        {
            'order': 4,
            'name': 'Kovalam & Sree Padmanabhaswamy Temple',
            'significance': 'Golden Beaches & Divine Mahavishnu Shrine',
            'description': 'Famous crescent beach lined with swaying palms combined with darshan at the ancient, wealthiest temple of Lord Padmanabhaswamy in Trivandrum.',
            'highlight': 'Padmanabhaswamy Darshan & Kovalam Beach',
            'image': 'images/padmanabhaswamy-temple.jpg'
        },
        {
            'order': 5,
            'name': 'Fort Kochi',
            'significance': 'Historic Arabian Sea Port',
            'description': 'A vibrant colonial heritage hub showcasing centuries-old Chinese cantilever fishing nets, St. Francis Church, and spice trading history.',
            'highlight': 'Chinese Fishing Nets & Colonial Heritage',
            'image': 'images/kochi-fishing-nets.jpg'
        }
    ]
}

KERALA_ITINERARY_DAYS = [
    {
        'day': 1,
        'title': 'Surat to Kerala',
        'starting_point': 'Surat, Gujarat',
        'destination': 'En Route to Kerala',
        'intro': 'Begin your beautiful Kerala journey with an AC train journey from Surat towards Kerala. Enjoy the comfortable journey and scenic views along the way.',
        'route_summary': 'Surat Railway Station ➔ AC Train boarding ➔ Western Ghats Railway Route',
        'meals': 'Lunch & Dinner on Train (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Overnight AC Train',
            'type': '3-Tier AC Sleeper Train',
            'hotel_name': 'Indian Railways Express'
        },
        'route_nodes': [
            {'name': 'Surat Railway Station', 'badge_class': 'normal'},
            {'name': 'Panvel / Konkan Rail Corridor', 'badge_class': 'normal'},
            {'name': 'Overnight AC Train', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Surat Railway Station Departure',
                'point': 'Board the scheduled AC superfast express with Swarnav tour coordinators.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Train journey towards Kerala'
            },
            {
                'name': 'Scenic Western Ghats Rail Transit',
                'point': 'Relax comfortably in air-conditioned sleeper berths as scenic coastal vistas pass by.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Scenic rail corridor'
            }
        ]
    },
    {
        'day': 2,
        'title': 'Train Journey to Kerala',
        'starting_point': 'En Route South India',
        'destination': 'Kerala Rail Corridor',
        'intro': 'Continue your comfortable train journey towards Kerala. Enjoy the changing landscapes and relax during the journey.',
        'route_summary': 'Scenic Peninsular Rail Corridor ➔ Coastal Palm Groves ➔ Overnight AC Train',
        'meals': 'Lunch & Dinner on Train (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Overnight AC Train',
            'type': '3-Tier AC Sleeper Train',
            'hotel_name': 'Indian Railways Express'
        },
        'route_nodes': [
            {'name': 'Peninsular Rail Corridor', 'badge_class': 'normal'},
            {'name': 'Entering Lush Kerala Border', 'badge_class': 'normal'},
            {'name': 'Overnight AC Train', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Lush Green Rail Landscapes',
                'point': 'Witness scenic palm groves, backwaters, and village scenery as the train nears Kerala.',
                'image': 'images/kerala-backwaters.jpg',
                'image_alt': 'Lush Kerala landscapes'
            },
            {
                'name': 'Relaxed Rail Experience',
                'point': 'Enjoy onboard vegetarian meals and prepare for the upcoming hill station ascent.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Comfortable rail journey'
            }
        ]
    },
    {
        'day': 3,
        'title': 'Kerala Arrival & Transfer to Munnar',
        'starting_point': 'Kerala Railway Station',
        'destination': 'Munnar (1,600 m)',
        'intro': 'Arrive in Kerala and proceed towards the beautiful hill station of Munnar. Enjoy the scenic drive through winding roads, tea plantations and lush green mountains. Check in to the hotel and relax.',
        'route_summary': 'Kerala Arrival ➔ Dedicated AC Coach ➔ Cheeyappara & Valara Waterfalls ➔ Munnar',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Munnar',
            'type': 'Deluxe Hill Resort',
            'hotel_name': 'Hotel Tea County / Westwood Riverside'
        },
        'route_nodes': [
            {'name': 'Kerala Railway Station', 'badge_class': 'normal'},
            {'name': 'Cheeyappara Waterfalls', 'badge_class': 'normal'},
            {'name': 'Munnar Tea Valley', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Kerala Arrival & AC Coach Transfer',
                'point': 'Warm reception by our local tour coordinators at the railway station and board our AC touring coach.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Kerala arrival'
            },
            {
                'name': 'Cheeyappara & Valara Waterfalls',
                'point': 'En-route photo stop at magnificent cascading natural falls surrounded by dense greenery.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Cheeyappara waterfalls'
            },
            {
                'name': 'Munnar Tea Plantations Check-in',
                'point': 'Arrive in cool Munnar, check in to your resort, and enjoy tea valley views.',
                'image': 'images/munnar-tea-gardens.jpg',
                'image_alt': 'Munnar tea gardens'
            }
        ]
    },
    {
        'day': 4,
        'title': 'Munnar Local Sightseeing',
        'starting_point': 'Munnar',
        'destination': 'Munnar Valley Attractions',
        'intro': 'After breakfast, explore the beautiful hill station of Munnar. Visit the famous Mattupetty Dam, Echo Point, Kundala Lake and surrounding tea plantations. Enjoy the cool mountain climate and spectacular views of the Western Ghats.',
        'route_summary': 'Munnar Hotel ➔ Mattupetty Dam ➔ Echo Point ➔ Kundala Lake ➔ Tea Estates ➔ Munnar',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Munnar',
            'type': 'Deluxe Hill Resort',
            'hotel_name': 'Hotel Tea County / Westwood Riverside'
        },
        'route_nodes': [
            {'name': 'Munnar Hotel', 'badge_class': 'normal'},
            {'name': 'Mattupetty Dam', 'badge_class': 'normal'},
            {'name': 'Echo Point & Kundala Lake', 'badge_class': 'normal'},
            {'name': 'Munnar', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Mattupetty Dam',
                'point': 'Concrete gravity dam surrounded by rolling tea hills; optional speed boating available.',
                'image': 'images/munnar-tea-gardens.jpg',
                'image_alt': 'Mattupetty Dam Munnar'
            },
            {
                'name': 'Echo Point',
                'point': 'Natural acoustic phenomenon spot beside a serene lake amidst mist-covered hills.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Echo Point Munnar'
            },
            {
                'name': 'Kundala Lake',
                'point': 'Picturesque arch dam lake where Kashmiri-style Shikara pedal boats operate.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Kundala Lake'
            },
            {
                'name': 'Sprawling Tea Plantations',
                'point': 'Walk through manicured green tea slopes and capture memorable family photographs.',
                'image': 'images/munnar-tea-gardens.jpg',
                'image_alt': 'Munnar tea estate'
            }
        ]
    },
    {
        'day': 5,
        'title': 'Munnar Sightseeing & Leisure',
        'starting_point': 'Munnar',
        'destination': 'Munnar Valley & Local Markets',
        'intro': 'After breakfast, continue exploring Munnar and its beautiful natural surroundings. Visit popular viewpoints and enjoy the peaceful atmosphere of the tea estates. Spend the evening at leisure.',
        'route_summary': 'Munnar ➔ Pothamedu Viewpoint ➔ Tea Museum ➔ Munnar Town Market ➔ Resort',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Munnar',
            'type': 'Deluxe Hill Resort',
            'hotel_name': 'Hotel Tea County / Westwood Riverside'
        },
        'route_nodes': [
            {'name': 'Munnar Resort', 'badge_class': 'normal'},
            {'name': 'Pothamedu Viewpoint', 'badge_class': 'normal'},
            {'name': 'Munnar Town Bazaar', 'badge_class': 'normal'},
            {'name': 'Munnar', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Pothamedu & Blossom Viewpoints',
                'point': 'Panoramic vistas of cardamom, coffee, and tea valleys stretching across the Western Ghats.',
                'image': 'images/munnar-tea-gardens.jpg',
                'image_alt': 'Pothamedu Viewpoint'
            },
            {
                'name': 'Tata Tea Museum (KDHP)',
                'point': 'Learn about the century-old history of tea manufacturing and taste fresh Nilgiri blends.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Tea Museum Munnar'
            },
            {
                'name': 'Munnar Town Local Bazaar',
                'point': 'Shop for authentic homemade chocolates, pure eucalyptus oil, spices, and fresh tea leaves.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Munnar local market'
            }
        ]
    },
    {
        'day': 6,
        'title': 'Munnar to Thekkady',
        'starting_point': 'Munnar',
        'destination': 'Thekkady / Periyar',
        'intro': 'After breakfast, check out and proceed towards Thekkady, famous for its forests, wildlife and beautiful natural surroundings. On arrival, check in to the hotel and relax. In the evening, explore the local market and enjoy optional cultural activities.',
        'route_summary': 'Munnar ➔ Scenic Western Ghats Drive (110 km / 3.5 hrs) ➔ Thekkady (Kumily) ➔ Spice Market',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Thekkady',
            'type': 'Forest Nature Resort',
            'hotel_name': 'Hotel Elephant Court / The Peermade'
        },
        'route_nodes': [
            {'name': 'Munnar Check-out', 'badge_class': 'normal'},
            {'name': 'Western Ghats Ghat Road', 'badge_class': 'normal'},
            {'name': 'Thekkady (Kumily)', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Scenic Munnar to Thekkady Highway',
                'point': 'Drive along winding mountain roads with aromatic spice plantations lining both sides.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Munnar to Thekkady road'
            },
            {
                'name': 'Kumily Town & Local Spice Market',
                'point': 'Evening stroll through spice shops selling farm-fresh cardamom, black pepper, and cloves.',
                'image': 'images/thekkady-periyar-lake.jpg',
                'image_alt': 'Thekkady spice market'
            },
            {
                'name': 'Optional Kathakali & Kalaripayattu Show',
                'point': 'Experience traditional Kerala martial arts and classical masked dance drama.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Kathakali dance Kerala'
            }
        ]
    },
    {
        'day': 7,
        'title': 'Thekkady & Periyar Sightseeing',
        'starting_point': 'Thekkady',
        'destination': 'Periyar Wildlife Sanctuary',
        'intro': 'After breakfast, explore the famous Periyar Wildlife Sanctuary area. Enjoy the beautiful forest surroundings and, subject to availability and additional charges, you may opt for a Periyar Lake Boat Ride. Later, enjoy some leisure time exploring the local spice markets.',
        'route_summary': 'Thekkady ➔ Periyar Tiger Reserve Entry ➔ Periyar Lake ➔ Spice Plantation Tour ➔ Hotel',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Thekkady',
            'type': 'Forest Nature Resort',
            'hotel_name': 'Hotel Elephant Court / The Peermade'
        },
        'route_nodes': [
            {'name': 'Thekkady Hotel', 'badge_class': 'normal'},
            {'name': 'Periyar National Park', 'badge_class': 'normal'},
            {'name': 'Periyar Lake Boat Jetty', 'badge_class': 'normal'},
            {'name': 'Thekkady', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Periyar Wildlife Sanctuary',
                'point': 'Sprawling protected rainforest sanctuary known for wild elephants, sambar deer, and rare birds.',
                'image': 'images/thekkady-periyar-lake.jpg',
                'image_alt': 'Periyar Wildlife Sanctuary'
            },
            {
                'name': 'Periyar Lake Boat Ride (Optional)',
                'point': 'Scenic boat cruise on Periyar reservoir viewing submerged forest trees and wildlife along the shore.',
                'image': 'images/thekkady-periyar-lake.jpg',
                'image_alt': 'Periyar Lake boat cruise'
            },
            {
                'name': 'Guided Spice Plantation Walk',
                'point': 'Educational walk through aromatic gardens seeing cinnamon, vanilla, turmeric, and nutmeg growing.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Spice plantation walk'
            }
        ]
    },
    {
        'day': 8,
        'title': 'Thekkady to Alleppey',
        'starting_point': 'Thekkady',
        'destination': 'Alleppey (Alappuzha)',
        'intro': 'After breakfast, check out and proceed towards Alleppey, popularly known as the "Venice of the East." Enjoy the beautiful journey through Kerala\'s lush landscapes. On arrival, board your traditional Kerala Houseboat and enjoy a relaxing cruise through the backwaters.',
        'route_summary': 'Thekkady ➔ Descend Western Ghats ➔ Alleppey Boat Jetty ➔ Board Deluxe Houseboat',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Alleppey Backwaters',
            'type': 'Deluxe Kerala Houseboat (Kettuvallam)',
            'hotel_name': 'Private AC Deluxe Houseboat'
        },
        'route_nodes': [
            {'name': 'Thekkady Check-out', 'badge_class': 'normal'},
            {'name': 'Alleppey Finishing Point', 'badge_class': 'normal'},
            {'name': 'Vembanad Lake Houseboat Cruise', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Alleppey Backwaters Arrival',
                'point': 'Arrive in Alleppey and step aboard an authentic thatched-roof Kerala Kettuvallam houseboat.',
                'image': 'images/kerala-backwaters.jpg',
                'image_alt': 'Kerala backwaters Alleppey'
            },
            {
                'name': 'Vembanad Lake & Canals Cruise',
                'point': 'Glide through narrow palm-shaded canals, paddy fields below sea level, and tranquil village waterways.',
                'image': 'images/kerala-backwaters.jpg',
                'image_alt': 'Houseboat cruise backwaters'
            },
            {
                'name': 'Overnight Houseboat Stay',
                'point': 'Anchor amidst the serene backwaters under starry skies with freshly prepared pure veg dinner onboard.',
                'image': 'images/kerala-backwaters.jpg',
                'image_alt': 'Houseboat night stay'
            }
        ]
    },
    {
        'day': 9,
        'title': 'Alleppey to Kovalam',
        'starting_point': 'Alleppey Houseboat',
        'destination': 'Kovalam Beach',
        'intro': 'After breakfast, check out from the houseboat and proceed towards Kovalam, one of Kerala\'s most famous beach destinations. On arrival, check in to the hotel and enjoy the beautiful beach surroundings.',
        'route_summary': 'Alleppey Check-out ➔ Coastal Highway NH66 (160 km / 4 hrs) ➔ Kovalam Beach Resort',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Kovalam',
            'type': 'Beachside Hotel',
            'hotel_name': 'Hotel Sea Face / Uday Samudra Resort'
        },
        'route_nodes': [
            {'name': 'Alleppey Houseboat Check-out', 'badge_class': 'normal'},
            {'name': 'Kollam Coastal Highway', 'badge_class': 'normal'},
            {'name': 'Kovalam Beach', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Alleppey to Kovalam Coastal Drive',
                'point': 'Scenic highway transit past coastal fishing hamlets and coir processing centers.',
                'image': 'images/kerala-backwaters.jpg',
                'image_alt': 'Coastal highway drive'
            },
            {
                'name': 'Kovalam Beachfront Check-in',
                'point': 'Check in to your beach resort located within comfortable walking distance of the Arabian Sea.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Kovalam beachfront'
            },
            {
                'name': 'Lighthouse & Hawa Beach Leisure',
                'point': 'Relax on the golden sandy shores, enjoy cooling sea breezes, and watch the sun dip into the horizon.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Kovalam Lighthouse Beach'
            }
        ]
    },
    {
        'day': 10,
        'title': 'Kovalam & Trivandrum Sightseeing',
        'starting_point': 'Kovalam',
        'destination': 'Trivandrum City & Temples',
        'intro': 'After breakfast, explore Kovalam and nearby attractions. Later, proceed for sightseeing in Trivandrum. Visit the famous Sree Padmanabhaswamy Temple, Napier Museum and other important attractions.',
        'route_summary': 'Kovalam ➔ Sree Padmanabhaswamy Temple ➔ Napier Museum & Zoo ➔ Kovalam Beach',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Kovalam',
            'type': 'Beachside Hotel',
            'hotel_name': 'Hotel Sea Face / Uday Samudra Resort'
        },
        'route_nodes': [
            {'name': 'Kovalam Resort', 'badge_class': 'normal'},
            {'name': 'Sree Padmanabhaswamy Temple', 'badge_class': 'normal'},
            {'name': 'Napier Museum & Art Gallery', 'badge_class': 'normal'},
            {'name': 'Kovalam', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Sree Padmanabhaswamy Temple',
                'point': 'Sacred darshan of Lord Vishnu reclining on Anantha in one of India\'s most ancient 108 Divya Desams (traditional dress code mandatory).',
                'image': 'images/padmanabhaswamy-temple.jpg',
                'image_alt': 'Sree Padmanabhaswamy Temple'
            },
            {
                'name': 'Napier Museum & Art Gallery',
                'point': '19th-century Indo-Saracenic architectural landmark housing bronze idols and Kerala historical artifacts.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Napier Museum Trivandrum'
            },
            {
                'name': 'Kovalam Beach Sunset',
                'point': 'Evening relaxation along the illuminated promenade with sound of Arabian Sea waves.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Kovalam Beach sunset'
            }
        ]
    },
    {
        'day': 11,
        'title': 'Kovalam to Kochi',
        'starting_point': 'Kovalam',
        'destination': 'Kochi (Cochin)',
        'intro': 'After breakfast, check out and proceed towards Kochi, the historic port city of Kerala. On arrival, explore the famous Fort Kochi area and visit Chinese Fishing Nets, St. Francis Church and the local market.',
        'route_summary': 'Kovalam ➔ Kochi (210 km / 5 hrs) ➔ Fort Kochi ➔ Chinese Fishing Nets ➔ St. Francis Church',
        'meals': 'Lunch & Dinner (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Kochi',
            'type': 'City Deluxe Hotel',
            'hotel_name': 'Hotel Abad Plaza / Casino Hotel'
        },
        'route_nodes': [
            {'name': 'Kovalam Check-out', 'badge_class': 'normal'},
            {'name': 'Kochi City Check-in', 'badge_class': 'normal'},
            {'name': 'Fort Kochi & Chinese Fishing Nets', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Fort Kochi Historic Quarter',
                'point': 'Walk through colonial Portuguese, Dutch, and British influenced streets and heritage buildings.',
                'image': 'images/kochi-fishing-nets.jpg',
                'image_alt': 'Fort Kochi'
            },
            {
                'name': 'Iconic Chinese Fishing Nets (Cheena Vala)',
                'point': 'Historic shore-operated cantilever fishing nets introduced by 14th-century Chinese traders.',
                'image': 'images/kochi-fishing-nets.jpg',
                'image_alt': 'Chinese fishing nets Kochi'
            },
            {
                'name': 'St. Francis Church',
                'point': 'One of the oldest European churches in India where explorer Vasco da Gama was originally buried.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'St Francis Church Kochi'
            },
            {
                'name': 'Marine Drive Promenade',
                'point': 'Vibrant waterside promenade overlooking the Kochi backwaters and harbor shipping lanes.',
                'image': 'images/kochi-fishing-nets.jpg',
                'image_alt': 'Kochi Marine Drive'
            }
        ]
    },
    {
        'day': 12,
        'title': 'Kochi to Surat',
        'starting_point': 'Kochi (Ernakulam)',
        'destination': 'En Route to Surat',
        'intro': 'After breakfast, check out from the hotel and proceed towards the railway station. Begin your return journey from Kerala to Surat by AC train. Enjoy the journey and carry home wonderful memories of Kerala.',
        'route_summary': 'Kochi Check-out ➔ Ernakulam Railway Station ➔ Board Return AC Train towards Surat',
        'meals': 'Lunch & Dinner on Train (Breakfast if included in package)',
        'accommodation': {
            'night_stay': 'Overnight AC Train',
            'type': '3-Tier AC Sleeper Train',
            'hotel_name': 'Indian Railways Express'
        },
        'route_nodes': [
            {'name': 'Kochi Hotel Check-out', 'badge_class': 'normal'},
            {'name': 'Ernakulam Railway Station', 'badge_class': 'normal'},
            {'name': 'Return AC Train', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Ernakulam Station Departure',
                'point': 'Assisted boarding on the scheduled AC express train back to Gujarat.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Ernakulam station'
            },
            {
                'name': 'Comfortable Rail Journey Northbound',
                'point': 'Relax in comfortable AC sleeper berths and recount unforgettable memories of Kerala.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Rail return transit'
            }
        ]
    },
    {
        'day': 13,
        'title': 'Arrival at Surat',
        'starting_point': 'En Route Gujarat',
        'destination': 'Surat, Gujarat',
        'intro': 'Arrive in Surat and conclude your memorable Kerala Tour filled with beautiful memories of mountains, tea gardens, wildlife, backwaters and beaches.',
        'route_summary': 'Gujarat Border ➔ Surat Railway Station ➔ Tour Concludes',
        'meals': 'Breakfast (Lunch if included in package)',
        'accommodation': {
            'night_stay': 'Home Departure',
            'type': 'Tour Concludes at Surat',
            'hotel_name': 'Surat Railway Station'
        },
        'route_nodes': [
            {'name': 'Gujarat Rail Corridor', 'badge_class': 'normal'},
            {'name': 'Surat Railway Station', 'badge_class': 'normal'},
            {'name': 'Tour Concludes with Cherished Memories', 'badge_class': 'night-stay'}
        ],
        'places_covered': [
            {
                'name': 'Surat Railway Station Arrival',
                'point': 'Disembark at Surat with lifelong memories of Kerala’s hills, backwaters, wildlife, and beaches.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Surat Railway Station'
            },
            {
                'name': 'Onward Gujarat Dispersal',
                'point': 'Coordinated transfers available for connecting passengers to Ahmedabad, Vadodara, and Rajkot.',
                'image': 'images/nature-hero-bg.jpg',
                'image_alt': 'Onward transit'
            }
        ]
    }
]

KERALA_PACKAGE_DETAILS = {
    'inclusions': [
        'Confirmed Round-Trip AC Train Journey (Surat to Kerala & Kochi to Surat)',
        'Dedicated AC touring coach for all mountain, forest, and coastal transfers',
        '8 Nights Deluxe Hotel Accommodation (3N Munnar, 2N Thekkady, 2N Kovalam, 1N Kochi) on triple-sharing basis',
        '1 Night Traditional Kerala Houseboat stay in Alleppey Backwaters',
        '3 Nights comfortable travel in AC Train berths',
        'Pure vegetarian Lunch and Dinner provided daily with North Indian & Gujarati taste',
        'Breakfast provided if included in the selected package option',
        'Munnar sightseeing: Mattupetty Dam, Echo Point, Kundala Lake & Tea Estates',
        'Thekkady spice plantation visit and Periyar sanctuary area visit',
        'Kovalam beach sightseeing & Trivandrum Padmanabhaswamy Temple darshan assistance',
        'Fort Kochi heritage walk: Chinese Fishing Nets & St. Francis Church',
        'Dedicated Swarnav tour coordinator throughout the tour'
    ],
    'exclusions': [
        'Daily breakfast (unless specifically included in your selected package option)',
        'Personal expenses, laundry, extra snacks, and mineral water',
        'Entry tickets to monuments, museums, Tea Museum, and Kathakali shows',
        'Optional Periyar Lake wildlife boating tickets (arranged subject to forest dept slots)',
        'Special darshan tickets or pooja fees at Padmanabhaswamy Temple',
        'Porters, coolie charges, and personal tips',
        'Any cost arising due to natural calamities, landslides, or train delays'
    ],
    'conditional_services': [
        {
            'service': 'Daily Breakfast Inclusion Tier',
            'condition': 'Available as an upgrade package option at nominal additional cost providing daily buffet breakfast.'
        },
        {
            'service': 'Double / Twin Sharing Private Room',
            'condition': 'Available upon request for couples or families seeking a private room (+15% standard surcharge).'
        },
        {
            'service': 'Periyar Lake Forest Boating Tickets',
            'condition': 'Booked online or on-spot as per Kerala Forest Department availability and passenger request.'
        },
        {
            'service': 'Home City Railway/Flight Connectivity',
            'condition': 'Train or flight connections from Ahmedabad, Vadodara, Rajkot, or Mumbai to join at Surat can be arranged upon request.'
        }
    ],
    'important_notes': [
        'Strict traditional dress code is enforced at Sree Padmanabhaswamy Temple in Trivandrum (Dhoti for men with bare chest; Saree/Pavada for women).',
        'Standard hotel check-in time is 12:00 PM and check-out is 10:00 AM across Kerala resorts.',
        'Munnar hill station experiences cool temperatures (15°C–22°C); carrying light woolens or a light jacket is recommended.',
        'All passengers must carry original government-issued photo ID (Aadhaar Card) for train journeys and hotel check-ins.'
    ]
}

KERALA_STAY_AND_TRAVEL = {
    'accommodation': {
        'category': 'Deluxe Hill Resorts, Nature Lodges & Traditional Kerala Houseboat',
        'room_sharing': 'Standard package pricing is on a triple-sharing basis in spacious rooms with attached modern bathrooms.',
        'private_room': 'Double-sharing (twin room) for couples or single occupancy is available upon request with standard supplemental charges.',
        'hot_water': '24-hour hot water is available in Munnar, Thekkady, Kovalam, and Kochi hotels.',
        'remote_limitations': 'Alleppey houseboats operate air conditioning in bedrooms from 9:00 PM to 6:00 AM (full-time AC available upon request). Houseboats anchor in quiet backwater bays overnight.',
        'hotel_changes': 'Hotels listed are indicative; equivalent 3-star standard properties in the same category will be provided if required by operational adjustments.'
    },
    'meals': {
        'overview': 'Wholesome, freshly cooked pure vegetarian food curated specifically for Gujarati, Jain, and North Indian devotees.',
        'included_meals': 'Pure vegetarian lunch and dinner are included on all tour days as outlined in the day-by-day itinerary.',
        'breakfast_rule': 'Breakfast is provided if included in the selected package option. On train journey days, standard IRCTC pantry or onboard meal packets are provided.',
        'trek_days': 'During long sightseeing drives in Munnar and Thekkady, hot lunch is arranged at verified pure-vegetarian partner restaurants.',
        'extra_refreshments': 'Personal tea, coffee, cold drinks, packaged water bottles, and evening snacks outside scheduled meals are direct pilgrim expenses.'
    },
    'transportation': {
        'main_mode': 'Confirmed AC Sleeper Train + Dedicated AC Touring Coach',
        'train_journey': 'Round-trip confirmed 3-Tier AC train tickets between Surat and Kerala (outward to Kerala / return from Kochi Ernakulam).',
        'road_transport': 'Comfortable, sanitized air-conditioned 2x2 luxury coach for all transfers, hill curves, and local sightseeing in Kerala.',
        'local_transport': 'Traditional thatched-roof deluxe Houseboat cruise across Alleppey backwaters included.',
        'pickup_drop': 'Primary group assembly and return point is Surat Railway Station (Gujarat).',
        'gujarat_travellers': 'Devotees from Ahmedabad, Vadodara, Rajkot, Bhavnagar, and Mumbai can easily join the group at Surat or be ticketed directly from their nearest junction.',
        'travel_time_notice': 'Mountain ghat roads between Kochi, Munnar, and Thekkady involve sharp turns and steady speeds; passengers prone to motion sickness are advised to carry preventive medication.',
        'vehicle_allocation': 'Coaches are allocated based on final batch size with generous luggage space and experienced mountain drivers.'
    }
}

KERALA_TRAVEL_GUIDE = {
    'age_restrictions': {
        'guidance': 'Suitable for pilgrims of all ages, including senior citizens and young children.',
        'advisory': 'The itinerary features relaxed pacing with moderate walking in Munnar tea gardens and Fort Kochi.',
        'safety_restriction': 'Individuals with severe motion sickness should carry appropriate medication for Munnar winding ghat roads.'
    },
    'health_requirements': [
        'Carry regular personal prescription medicines for the entire 13-day duration.',
        'Keep motion sickness tablets handy for Munnar mountain ghat drives.',
        'Carry mosquito repellent lotion for Thekkady forest areas and Alleppey backwaters.',
        'Stay hydrated and carry electrolyte sachets during coastal sightseeing in Kovalam and Kochi.'
    ],
    'documents_required': [
        'Original Government Photo ID (Aadhaar Card / Voter ID / Passport) for all passengers.',
        'Multiple physical photocopies of Aadhaar cards for hotel and houseboat registrations.',
        'Confirmed Train E-ticket copies provided by Swarnav.',
        'Emergency contact list and doctor prescription copies.'
    ],
    'packing_advice': 'Light cotton clothes for coastal Kovalam and Kochi, light woolens/jacket for Munnar, traditional attire for temples, and comfortable walking footwear.',
    'items_to_carry': [
        'Traditional attire (Dhoti for men, Saree/Churidar with dupatta for women) for Padmanabhaswamy Temple',
        'Light sweater, shawl, or jacket for cool Munnar evenings (15°C)',
        'Comfortable walking shoes or sandals for sightseeing',
        'Sunscreen, sunglasses, wide-brim hat, and umbrella for tropical showers',
        'Mosquito repellent cream or spray for backwaters and nature reserves',
        'Mobile power bank, multi-plug adapter, and camera chargers',
        'Personal toiletry kit and reusable water bottle'
    ],
    'weather_info': 'Munnar hill station is pleasant and cool (15°C–22°C year-round). Coastal Kerala (Alleppey, Kovalam, Kochi) is warm and tropical (24°C–32°C). Light rain showers may occur; carrying a small umbrella is recommended.'
}

KERALA_POLICIES = {
    'booking_conditions': [
        'Advance Token: Booking is confirmed upon receipt of ₹5,000 per person advance token.',
        'Train Ticket Advance: Train reservation segment balance must be settled at the time of train booking opening (120 days prior).',
        'Final Balance: The remaining tour package amount must be paid at least 15 days prior to departure.',
        'Written Confirmation: An official digital booking receipt and trip invoice will be dispatched via WhatsApp and email.'
    ],
    'cancellation_brackets': [
        {
            'timeline': '30 or more days before departure',
            'deduction': '₹2,500 per person + actual IRCTC railway cancellation fees',
            'refund_estimate': 'Remaining balance refunded within 7 working days'
        },
        {
            'timeline': '15 to 29 days before departure',
            'deduction': '25% of total package cost + railway cancellation fees',
            'refund_estimate': '75% of package fee refunded'
        },
        {
            'timeline': '7 to 14 days before departure',
            'deduction': '50% of total package cost + railway cancellation fees',
            'refund_estimate': '50% of package fee refunded'
        },
        {
            'timeline': 'Less than 7 days or No-Show',
            'deduction': '100% of package cost (Non-refundable)',
            'refund_estimate': 'No refund applicable'
        }
    ],
    'cancellation_rules': [
        'Cancellation requests must be communicated in writing from the registered mobile number or email.',
        'IRCTC train cancellation deductions are governed strictly by Indian Railway refund rules.',
        'If the tour is cancelled or rescheduled by Swarnav due to operational constraints, 100% of the advance amount will be refunded or adjusted against an alternative batch.',
        'Unutilized services (meals, missed sightseeing, early check-out) are non-refundable.'
    ]
}

KERALA_NAV_TABS = [
    {'name': 'Overview', 'url_name': 'yatras:kerala_overview', 'slug': 'overview'},
    {'name': '13-Day Itinerary', 'url_name': 'yatras:kerala_itinerary', 'slug': 'itinerary'},
    {'name': 'Package Details', 'url_name': 'yatras:kerala_package_details', 'slug': 'package-details'},
    {'name': 'Stay & Travel', 'url_name': 'yatras:kerala_stay_and_travel', 'slug': 'stay-and-travel'},
    {'name': 'Travel Guide', 'url_name': 'yatras:kerala_travel_guide', 'slug': 'travel-guide'},
    {'name': 'Booking Policies', 'url_name': 'yatras:kerala_policies', 'slug': 'policies'},
]
