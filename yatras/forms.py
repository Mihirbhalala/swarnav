import json
from django import forms
from django.core.files.storage import default_storage
from unfold.widgets import UnfoldAdminTextareaWidget, UnfoldAdminTextInputWidget

from .models import (
    TourPackage,
    DhamDestination,
    ItineraryDay,
    PackageDetail,
    StayAndTravel,
    TravelGuide,
    PolicyAndFaq
)


class LineSeparatedListWidget(UnfoldAdminTextareaWidget):
    """
    Friendly textarea widget that renders Python lists as one item per line,
    allowing non-technical admins to edit bullet lists without dealing with JSON syntax.
    """
    def format_value(self, value):
        if not value:
            return ""
        if isinstance(value, (list, tuple)):
            if all(isinstance(x, str) for x in value):
                return "\n".join(value)
            return json.dumps(value, indent=2, ensure_ascii=False)
        elif isinstance(value, str):
            try:
                parsed = json.loads(value)
                if isinstance(parsed, (list, tuple)) and all(isinstance(x, str) for x in parsed):
                    return "\n".join(parsed)
            except Exception:
                pass
            return value
        return super().format_value(value)

    def value_from_datadict(self, data, files, name):
        val = data.get(name)
        if not val or not val.strip():
            return []
        val = val.strip()
        # If user explicitly entered valid JSON array or object, parse it
        if (val.startswith('[') and val.endswith(']')) or (val.startswith('{') and val.endswith('}')):
            try:
                return json.loads(val)
            except Exception:
                pass
        # Plain text: Split line-by-line, ignore empty lines
        return [line.strip() for line in val.splitlines() if line.strip()]


class LineSeparatedListFormField(forms.CharField):
    """Form field for JSON fields that should be managed as plain-text line lists."""
    widget = LineSeparatedListWidget

    def to_python(self, value):
        if not value:
            return []
        if isinstance(value, (list, dict)):
            return value
        val = str(value).strip()
        if (val.startswith('[') and val.endswith(']')) or (val.startswith('{') and val.endswith('}')):
            try:
                return json.loads(val)
            except Exception:
                pass
        return [line.strip() for line in val.splitlines() if line.strip()]


class TourPackageForm(forms.ModelForm):
    """
    Enhanced, non-technical friendly admin form for Tour Packages.
    Replaces raw JSON fields with line-by-line textareas and adds image upload support.
    """
    image_file = forms.ImageField(
        required=False,
        label="Upload Tour Photo",
        help_text="Upload a photo from your computer/mobile (.jpg, .png, .webp). If uploaded, it will automatically become the tour cover photo."
    )
    
    highlights = LineSeparatedListFormField(
        required=False,
        label="Tour Highlights (One per line)",
        help_text="Type each highlight on a new line (e.g. All 4 Sacred Dhams darshan in traditional sequence)"
    )
    route_highlights = LineSeparatedListFormField(
        required=False,
        label="Route Cities & Stops (One per line)",
        help_text="Type each stop city on a new line (e.g. Surat, Haridwar, Barkot, Yamunotri...)"
    )
    introduction = LineSeparatedListFormField(
        required=False,
        label="Introduction Paragraphs (One per line)",
        help_text="Type or paste introduction paragraphs. Each line/block represents one paragraph."
    )

    class Meta:
        model = TourPackage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configure friendlier help texts and placeholders
        if 'name' in self.fields:
            self.fields['name'].widget.attrs.update({'placeholder': 'e.g. Char Dham Yatra'})
        if 'duration_display' in self.fields:
            self.fields['duration_display'].widget.attrs.update({'placeholder': 'e.g. 13 Days / 12 Nights'})
        if 'starting_price' in self.fields:
            self.fields['starting_price'].widget.attrs.update({'placeholder': 'e.g. ₹30,000'})
        if 'price_note' in self.fields:
            self.fields['price_note'].widget.attrs.update({'placeholder': 'e.g. per person (Triple-sharing)'})
        if 'status_label' in self.fields:
            self.fields['status_label'].widget.attrs.update({'placeholder': 'e.g. Next Confirmed Batch: 1st Nov – 13th Nov'})
        if 'tour_date' in self.fields:
            self.fields['tour_date'].widget.attrs.update({
                'placeholder': 'e.g. 15 Nov 2026, 1st Nov – 13th Nov, or November 2026',
            })
            self.fields['tour_date'].label = "Tour Departure Date / Month"
            self.fields['tour_date'].help_text = "When active, enter specific start date (e.g. 15 Nov 2026) or starting month (e.g. November 2026). This is highlighted on the website."

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            saved_path = default_storage.save(f"tours/{image_file.name}", image_file)
            instance.image = f"media/{saved_path}"
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class ItineraryDayForm(forms.ModelForm):
    """
    Friendly day itinerary form.
    Deconstructs the schedule JSON dictionary into 4 simple labeled schedule fields:
    Morning, Afternoon, Evening, and Notes.
    """
    schedule_morning = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. Early morning departure after breakfast towards Barkot'}),
        required=False,
        label="🌅 Morning Activity",
        help_text="What pilgrims do in the morning"
    )
    schedule_afternoon = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. Scenic lunch stop along the Yamuna river valley'}),
        required=False,
        label="☀️ Afternoon Activity",
        help_text="Lunch halt, midway sightseeing, or road transit"
    )
    schedule_evening = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. Hotel check-in, temple aarti & warm satvik dinner'}),
        required=False,
        label="🌙 Evening & Night Activity",
        help_text="Evening arrival, aarti, dinner, and night stay"
    )
    schedule_notes = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Carry warm thermals and keep government ID handy'}),
        required=False,
        label="💡 Important Day Note",
        help_text="Special advisory or packing reminder for this day"
    )

    darshan_tips = LineSeparatedListFormField(
        required=False,
        label="Darshan Tips (One per line)",
        help_text="Helpful tips for pilgrims for this day's temples (one tip per line)"
    )
    scenic_points = LineSeparatedListFormField(
        required=False,
        label="Scenic & Photography Points (One per line)",
        help_text="Key photo stops, river views, or viewpoints along the route"
    )

    class Meta:
        model = ItineraryDay
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Prefill schedule fields if instance exists
        if self.instance and self.instance.pk and isinstance(self.instance.schedule, dict):
            sched = self.instance.schedule
            self.fields['schedule_morning'].initial = sched.get('morning', '')
            self.fields['schedule_afternoon'].initial = sched.get('afternoon', '')
            self.fields['schedule_evening'].initial = sched.get('evening', '')
            self.fields['schedule_notes'].initial = sched.get('notes', '')

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Reconstruct schedule dictionary from individual fields
        instance.schedule = {
            'morning': self.cleaned_data.get('schedule_morning', '').strip(),
            'afternoon': self.cleaned_data.get('schedule_afternoon', '').strip(),
            'evening': self.cleaned_data.get('schedule_evening', '').strip(),
            'notes': self.cleaned_data.get('schedule_notes', '').strip(),
        }
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class PackageDetailForm(forms.ModelForm):
    """Line-by-line editor for Inclusions, Exclusions, and Booking Guidelines."""
    inclusions = LineSeparatedListFormField(
        required=False,
        label="Included Services (One per line)",
        help_text="Type each included service on a new line (e.g. Surat-to-Haridwar train transport, Daily satvik meals)"
    )
    exclusions = LineSeparatedListFormField(
        required=False,
        label="Excluded Services (One per line)",
        help_text="Type each excluded item on a new line (e.g. Helicopter tickets, Personal pony/palki charges)"
    )
    booking_guidelines = LineSeparatedListFormField(
        required=False,
        label="Booking Guidelines (One per line)",
        help_text="Terms or instructions for booking (one per line)"
    )
    key_highlights = LineSeparatedListFormField(
        required=False,
        label="Key Highlights (One per line)",
        help_text="Notable package features (one per line)"
    )

    class Meta:
        model = PackageDetail
        fields = '__all__'


class StayAndTravelForm(forms.ModelForm):
    """Line-by-line editor for Stay and Travel guidelines."""
    hotel_options = LineSeparatedListFormField(
        required=False,
        label="Hotel Options & Standards (One per line)",
        help_text="Describe hotel accommodation standards or property notes"
    )
    vehicle_guidelines = LineSeparatedListFormField(
        required=False,
        label="Vehicle & Transport Guidelines (One per line)",
        help_text="Bus, coach, or taxi details"
    )
    baggage_rules = LineSeparatedListFormField(
        required=False,
        label="Baggage Guidelines (One per line)",
        help_text="Luggage size or weight advice"
    )
    meal_guidelines = LineSeparatedListFormField(
        required=False,
        label="Meal & Dining Guidelines (One per line)",
        help_text="Satvik meal info, tea, breakfast notes"
    )

    class Meta:
        model = StayAndTravel
        fields = '__all__'


class TravelGuideForm(forms.ModelForm):
    """Line-by-line editor for Travel Preparation & Advice."""
    weather = LineSeparatedListFormField(
        required=False,
        label="Weather & Climate Advice (One per line)",
        help_text="Information about mountain temperatures and weather"
    )
    packing_list = LineSeparatedListFormField(
        required=False,
        label="What to Pack (One item per line)",
        help_text="Woollens, medicines, walking stick, rain poncho..."
    )
    registration_process = LineSeparatedListFormField(
        required=False,
        label="Registration Process Steps (One per line)",
        help_text="Steps for Yatra registration with QR code"
    )
    medical_advisory = LineSeparatedListFormField(
        required=False,
        label="Medical & Health Advisory (One per line)",
        help_text="High altitude and fitness advice"
    )
    local_customs = LineSeparatedListFormField(
        required=False,
        label="Temple Rules & Local Customs (One per line)",
        help_text="Dress codes, mobile phones inside sanctum, photography guidelines"
    )
    senior_citizen_tips = LineSeparatedListFormField(
        required=False,
        label="Senior Citizen Care (One per line)",
        help_text="Pony, doli, porter, and medicine tips for elders"
    )

    class Meta:
        model = TravelGuide
        fields = '__all__'


class PolicyAndFaqForm(forms.ModelForm):
    """Line-by-line editor for Cancellation Terms & Payment Policies."""
    cancellation_policy = LineSeparatedListFormField(
        required=False,
        label="Cancellation Policy (One rule per line)",
        help_text="Cancellation rules and refund timelines"
    )
    payment_terms = LineSeparatedListFormField(
        required=False,
        label="Payment Terms (One rule per line)",
        help_text="Advance deposit and balance payment terms"
    )
    general_terms = LineSeparatedListFormField(
        required=False,
        label="General Terms & Conditions (One rule per line)",
        help_text="General conditions of travel and operator liability"
    )

    class Meta:
        model = PolicyAndFaq
        fields = '__all__'
