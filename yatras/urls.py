from django.urls import path
from . import views

app_name = 'yatras'

urlpatterns = [
    # --------------------------------------------------------------------------
    # Char Dham Yatra Routes
    # --------------------------------------------------------------------------
    path('char-dham/', views.char_dham_overview, name='char_dham_overview'),
    path('char-dham/itinerary/', views.char_dham_itinerary, name='char_dham_itinerary'),
    path('char-dham/itinerary/day/<int:day_number>/', views.char_dham_day_detail, name='char_dham_day_detail'),
    path('char-dham/package-details/', views.char_dham_package_details, name='char_dham_package_details'),
    path('char-dham/stay-and-travel/', views.char_dham_stay_and_travel, name='char_dham_stay_and_travel'),
    path('char-dham/travel-guide/', views.char_dham_travel_guide, name='char_dham_travel_guide'),
    path('char-dham/policies/', views.char_dham_policies, name='char_dham_policies'),

    # --------------------------------------------------------------------------
    # Jagannath Puri & Eastern Divine Pilgrimage Routes
    # --------------------------------------------------------------------------
    path('puri/', views.puri_overview, name='puri_overview'),
    path('puri/itinerary/', views.puri_itinerary, name='puri_itinerary'),
    path('puri/itinerary/day/<int:day_number>/', views.puri_day_detail, name='puri_day_detail'),
    path('puri/package-details/', views.puri_package_details, name='puri_package_details'),
    path('puri/stay-and-travel/', views.puri_stay_and_travel, name='puri_stay_and_travel'),
    path('puri/travel-guide/', views.puri_travel_guide, name='puri_travel_guide'),
    path('puri/policies/', views.puri_policies, name='puri_policies'),

    # --------------------------------------------------------------------------
    # Kashmir Paradise & Mata Vaishno Devi Tour Routes
    # --------------------------------------------------------------------------
    path('kashmir/', views.kashmir_overview, name='kashmir_overview'),
    path('kashmir/itinerary/', views.kashmir_itinerary, name='kashmir_itinerary'),
    path('kashmir/itinerary/day/<int:day_number>/', views.kashmir_day_detail, name='kashmir_day_detail'),
    path('kashmir/package-details/', views.kashmir_package_details, name='kashmir_package_details'),
    path('kashmir/stay-and-travel/', views.kashmir_stay_and_travel, name='kashmir_stay_and_travel'),
    path('kashmir/travel-guide/', views.kashmir_travel_guide, name='kashmir_travel_guide'),
    path('kashmir/policies/', views.kashmir_policies, name='kashmir_policies'),

    # --------------------------------------------------------------------------
    # Rameshwaram & South Circuit Pilgrimage Tour Routes
    # --------------------------------------------------------------------------
    path('rameshwaram/', views.rameshwaram_overview, name='rameshwaram_overview'),
    path('rameshwaram/itinerary/', views.rameshwaram_itinerary, name='rameshwaram_itinerary'),
    path('rameshwaram/itinerary/day/<int:day_number>/', views.rameshwaram_day_detail, name='rameshwaram_day_detail'),
    path('rameshwaram/package-details/', views.rameshwaram_package_details, name='rameshwaram_package_details'),
    path('rameshwaram/stay-and-travel/', views.rameshwaram_stay_and_travel, name='rameshwaram_stay_and_travel'),
    path('rameshwaram/travel-guide/', views.rameshwaram_travel_guide, name='rameshwaram_travel_guide'),
    path('rameshwaram/policies/', views.rameshwaram_policies, name='rameshwaram_policies'),

    # --------------------------------------------------------------------------
    # Kerala Tour (God’s Own Country - 13 Days / 12 Nights) Routes
    # --------------------------------------------------------------------------
    path('kerala/', views.kerala_overview, name='kerala_overview'),
    path('kerala/itinerary/', views.kerala_itinerary, name='kerala_itinerary'),
    path('kerala/itinerary/day/<int:day_number>/', views.kerala_day_detail, name='kerala_day_detail'),
    path('kerala/package-details/', views.kerala_package_details, name='kerala_package_details'),
    path('kerala/stay-and-travel/', views.kerala_stay_and_travel, name='kerala_stay_and_travel'),
    path('kerala/travel-guide/', views.kerala_travel_guide, name='kerala_travel_guide'),
    path('kerala/policies/', views.kerala_policies, name='kerala_policies'),
]
