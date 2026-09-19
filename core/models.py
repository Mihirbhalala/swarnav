from django.db import models


class TourCategory(models.Model):
    """Regional pilgrimage & tour categories (e.g., North India, South India, East India, Nepal)."""
    name = models.CharField(max_length=150, help_text="e.g. North India Tours")
    slug = models.SlugField(max_length=150, unique=True, help_text="e.g. north-india")
    tagline = models.CharField(max_length=255, blank=True, help_text="e.g. Himalayan Holy Shrines & Mountain Valleys")
    badge = models.CharField(max_length=100, blank=True, help_text="e.g. Sacred Garhwal & Kashmir")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order on homepage")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tour Category"
        verbose_name_plural = "Tour Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class WhyChooseUs(models.Model):
    """Key trust points and value propositions displayed on the homepage."""
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=50, default="🛡️", help_text="Emoji or icon name (e.g. 🚆, 🛡️, 🍲)")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Why Choose Us Feature"
        verbose_name_plural = "Why Choose Us Features"
        ordering = ['order']

    def __str__(self):
        return f"{self.icon} {self.title}"


class Inquiry(models.Model):
    """
    Customer pilgrimage and tour inquiry submissions.
    Securely stores validated inquiries from the public website and modal.
    """
    TOUR_CHOICES = [
        ('char-dham', 'Char Dham Yatra (13 Days – ₹30,000)'),
        ('panch-kedar', 'Panch Kedar Yatra (10 Days – ₹26,500)'),
        ('kashmir-paradise', 'Kashmir Tour (7 Days – ₹22,500)'),
        ('rameshwaram-circuit', 'Rameshwaram & South Circuit (8 Days – ₹24,000)'),
        ('kerala-tour', 'Kerala Tour (6 Days – ₹19,500)'),
        ('jagannath-puri', 'Jagannath Puri Odisha (11 Days – ₹24,500)'),
        ('jharkhand-tour', 'Jharkhand Spiritual Yatra (5 Days – ₹14,500)'),
        ('nepal-pashupatinath-muktinath', 'Nepal Pashupatinath Muktinath (8 Days – ₹34,500)'),
        ('general', 'General Pilgrimage Inquiry'),
    ]

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('follow_up', 'Follow-up'),
        ('converted', 'Converted'),
        ('closed', 'Closed'),
        ('spam', 'Spam'),
    ]

    tour = models.CharField(
        max_length=50,
        choices=TOUR_CHOICES,
        default='char-dham',
        verbose_name="Selected Tour"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Full Name"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone / WhatsApp Number"
    )
    departure_city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Departure City",
        help_text="Pilgrim's departure or home city (optional)"
    )
    total_pilgrims = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Total Pilgrims",
        help_text="Number of pilgrims travelling (optional)"
    )
    message = models.TextField(
        blank=True,
        verbose_name="Message / Preferred Month",
        help_text="Preferred travel month, train/flight requests or special requirements (optional)"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="Inquiry Status"
    )
    admin_notes = models.TextField(
        blank=True,
        verbose_name="Private Admin Notes",
        help_text="Private internal notes visible only to administrators"
    )
    consent_given = models.BooleanField(
        default=False,
        verbose_name="Consent Given",
        help_text="Whether the customer agreed to be contacted regarding this inquiry"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )

    class Meta:
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"Inquiry #{self.id}: {self.name} - {self.get_tour_display()}"



class Testimonial(models.Model):
    """Pilgrim testimonials and reviews."""
    pilgrim_name = models.CharField(max_length=150)
    city = models.CharField(max_length=100, blank=True, help_text="e.g. Surat, Ahmedabad, Mumbai")
    yatra_name = models.CharField(max_length=200, help_text="e.g. Char Dham Yatra")
    rating = models.PositiveSmallIntegerField(default=5, help_text="1 to 5 stars")
    review_text = models.TextField()
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.pilgrim_name} ({self.yatra_name}) - {self.rating}★"
