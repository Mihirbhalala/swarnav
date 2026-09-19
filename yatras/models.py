from django.db import models
from core.models import TourCategory


class TourPackage(models.Model):
    """Tour and Pilgrimage Packages offered by Swarnav."""
    STATUS_CHOICES = [
        ('active', 'Active / Complete Guide Available'),
        ('upcoming', 'Upcoming / Inquiries Open'),
        ('seasonal', 'Seasonal Bookings Open'),
        ('draft', 'Draft / Hidden'),
    ]

    category = models.ForeignKey(
        TourCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tours',
        help_text="Circuit category (e.g. North India, South India)"
    )
    slug = models.SlugField(max_length=150, unique=True, help_text="e.g. char-dham, jagannath-puri")
    name = models.CharField(max_length=200, help_text="e.g. Char Dham Yatra")
    subtitle = models.CharField(max_length=255, blank=True, help_text="e.g. Yamunotri • Gangotri • Kedarnath • Badrinath")
    tagline = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=150, blank=True, help_text="e.g. North India (Uttarakhand)")
    
    # Duration & Pricing
    duration_days = models.PositiveIntegerField(default=1)
    duration_nights = models.PositiveIntegerField(default=0)
    duration_display = models.CharField(max_length=100, blank=True, help_text="e.g. 13 Days / 12 Nights")
    starting_price = models.CharField(max_length=50, blank=True, help_text="e.g. ₹30,000")
    price_display = models.CharField(max_length=150, blank=True, help_text="e.g. Starting from ₹30,000 per person")
    price_note = models.CharField(max_length=150, blank=True, help_text="e.g. per person (Triple-sharing)")
    
    # Origins & Logistics
    starting_city = models.CharField(max_length=150, default="Surat, Gujarat")
    ending_city = models.CharField(max_length=150, default="Surat, Gujarat")
    origin = models.CharField(max_length=200, blank=True, help_text="e.g. Starts & Ends in Surat, Gujarat")
    home_city_connect = models.CharField(
        max_length=255,
        default="Train or flight from your home city can be arranged",
        help_text="Connectivity note for pilgrims from other cities"
    )
    
    # Summary Fields
    departures_summary = models.CharField(max_length=255, blank=True)
    departures_guidance = models.TextField(blank=True)
    accommodation_summary = models.TextField(blank=True)
    meals_summary = models.TextField(blank=True)
    transport_summary = models.TextField(blank=True)
    confirmation_note = models.TextField(blank=True)
    gujarat_support_note = models.TextField(blank=True)
    brief_guide = models.TextField(blank=True)
    
    # Structured List Fields (Stored as JSON for dynamic structured rendering)
    introduction = models.JSONField(default=list, blank=True, help_text="List of paragraphs")
    route_highlights = models.JSONField(default=list, blank=True, help_text="List of key stops/cities")
    highlights = models.JSONField(default=list, blank=True, help_text="Key highlights bullet points")
    
    # Media & Status
    image = models.CharField(max_length=255, default="images/kedarnath-temple.jpg", help_text="Static image path or asset URL")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    status_label = models.CharField(max_length=100, blank=True, help_text="e.g. Complete Guide Available")
    is_completed = models.BooleanField(default=False, help_text="Whether full multi-page portal is available")
    order = models.PositiveIntegerField(default=0, help_text="Ordering within its category")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tour Package"
        verbose_name_plural = "Tour Packages"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.duration_display})"


class DhamDestination(models.Model):
    """Key pilgrimage shrines / Dhams associated with a tour package."""
    tour = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='dhams')
    order = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=150)
    significance = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    highlight = models.CharField(max_length=150, blank=True)
    image = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Dham / Key Destination"
        verbose_name_plural = "Dhams / Key Destinations"
        ordering = ['order']

    def __str__(self):
        return f"Dham {self.order}: {self.name} ({self.tour.name})"


class ItineraryDay(models.Model):
    """Day-by-day itinerary plan for a tour package."""
    tour = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='itinerary_days')
    day_number = models.PositiveIntegerField(help_text="e.g. 1, 2, 3...")
    title = models.CharField(max_length=255, help_text="e.g. Surat to Haridwar")
    starting_point = models.CharField(max_length=150, blank=True, default='')
    destination = models.CharField(max_length=150, blank=True, default='')
    intro = models.TextField(blank=True, default='')
    route_summary = models.CharField(max_length=255, blank=True, default='', help_text="e.g. Surat ➔ Haridwar")
    
    # Stay & Food
    night_stay = models.CharField(max_length=150, blank=True, default='', help_text="e.g. Haridwar, Barkot")
    hotel_type = models.CharField(max_length=100, blank=True, default="Economy Hotel")
    hotel_name = models.CharField(max_length=255, blank=True, default='')
    meals = models.CharField(max_length=150, blank=True, default='', help_text="e.g. Lunch & Dinner")
    altitude = models.CharField(max_length=100, blank=True, default='', help_text="e.g. 3,583 m (11,755 ft)")
    
    # Detailed Schedules & Structured Info
    schedule = models.JSONField(default=dict, blank=True, help_text="Dict with morning, afternoon, evening, notes")
    darshan_tips = models.JSONField(default=list, blank=True, help_text="List of darshan tips")
    scenic_points = models.JSONField(default=list, blank=True, help_text="List of scenic points")
    places_covered = models.JSONField(default=list, blank=True, help_text="List of place objects with images and descriptions")
    route_nodes = models.JSONField(default=list, blank=True, help_text="List of route node objects for visual timeline")

    class Meta:
        verbose_name = "Itinerary Day"
        verbose_name_plural = "Itinerary Days"
        ordering = ['tour', 'day_number']
        unique_together = ('tour', 'day_number')

    def __str__(self):
        return f"{self.tour.name} - Day {self.day_number}: {self.title}"


class PackageDetail(models.Model):
    """Inclusions, exclusions, pricing breakdown, and booking guidelines."""
    tour = models.OneToOneField(TourPackage, on_delete=models.CASCADE, related_name='package_detail')
    inclusions = models.JSONField(default=list, blank=True)
    exclusions = models.JSONField(default=list, blank=True)
    pricing_structure = models.JSONField(default=list, blank=True)
    booking_guidelines = models.JSONField(default=list, blank=True)
    key_highlights = models.JSONField(default=list, blank=True)

    class Meta:
        verbose_name = "Package Details & Inclusions"
        verbose_name_plural = "Package Details & Inclusions"

    def __str__(self):
        return f"Package Details: {self.tour.name}"


class StayAndTravel(models.Model):
    """Accommodation, vehicle specs, baggage and meal rules."""
    tour = models.OneToOneField(TourPackage, on_delete=models.CASCADE, related_name='stay_and_travel')
    hotel_options = models.JSONField(default=list, blank=True)
    vehicle_guidelines = models.JSONField(default=list, blank=True)
    baggage_rules = models.JSONField(default=list, blank=True)
    meal_guidelines = models.JSONField(default=list, blank=True)

    class Meta:
        verbose_name = "Stay & Travel Configuration"
        verbose_name_plural = "Stay & Travel Configurations"

    def __str__(self):
        return f"Stay & Travel: {self.tour.name}"


class TravelGuide(models.Model):
    """Weather, packing list, registration, health and advisory."""
    tour = models.OneToOneField(TourPackage, on_delete=models.CASCADE, related_name='travel_guide')
    weather = models.JSONField(default=list, blank=True)
    packing_list = models.JSONField(default=list, blank=True)
    registration_process = models.JSONField(default=list, blank=True)
    medical_advisory = models.JSONField(default=list, blank=True)
    local_customs = models.JSONField(default=list, blank=True)
    senior_citizen_tips = models.JSONField(default=list, blank=True)

    class Meta:
        verbose_name = "Travel Guide & Preparation"
        verbose_name_plural = "Travel Guides & Preparation"

    def __str__(self):
        return f"Travel Guide: {self.tour.name}"


class PolicyAndFaq(models.Model):
    """Cancellation terms, payment guidelines, general terms and FAQs."""
    tour = models.OneToOneField(TourPackage, on_delete=models.CASCADE, related_name='policies')
    cancellation_policy = models.JSONField(default=list, blank=True)
    payment_terms = models.JSONField(default=list, blank=True)
    general_terms = models.JSONField(default=list, blank=True)
    faqs = models.JSONField(default=list, blank=True)

    class Meta:
        verbose_name = "Policies & FAQs"
        verbose_name_plural = "Policies & FAQs"

    def __str__(self):
        return f"Policies & FAQs: {self.tour.name}"
