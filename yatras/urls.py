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
]
