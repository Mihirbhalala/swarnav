import re
from django import forms
from .models import Inquiry


def clean_indian_phone(raw_phone):
    """
    Validate and normalize Indian phone numbers.
    Accepts:
    - 10-digit numbers starting with 6, 7, 8, 9 (e.g. 9586825353, 95868 25353, 95868-25353)
    - Numbers with +91 or 91 country code (e.g. +91 9586825353, 919586825353)
    Returns normalized 10-digit phone string with +91 prefix e.g. '+919586825353'.
    Raises forms.ValidationError for invalid numbers.
    """
    if not raw_phone:
        raise forms.ValidationError("Phone / WhatsApp number is required.")

    # Check for illegal alphabetic or special characters other than +, -, spaces, ()
    cleaned = raw_phone.strip()
    if re.search(r'[a-zA-Z]', cleaned):
        raise forms.ValidationError("Phone number cannot contain alphabetic characters.")

    # Remove spaces, hyphens, parentheses
    digits_only = re.sub(r'[\s\-\(\)\.]', '', cleaned)

    # Handle +91 prefix
    if digits_only.startswith('+91'):
        digits_only = digits_only[3:]
    elif digits_only.startswith('91') and len(digits_only) == 12:
        digits_only = digits_only[2:]
    elif digits_only.startswith('0') and len(digits_only) == 11:
        digits_only = digits_only[1:]

    # Now digits_only must be exactly 10 digits and start with 6, 7, 8, or 9
    if not re.match(r'^[6-9]\d{9}$', digits_only):
        raise forms.ValidationError(
            "Please enter a valid 10-digit Indian mobile / WhatsApp number (e.g., 9586825353 or +91 95868 25353)."
        )

    return f"+91{digits_only}"


class InquiryForm(forms.ModelForm):
    consent_given = forms.BooleanField(
        required=True,
        initial=False,
        error_messages={
            'required': 'You must agree to be contacted regarding this yatra inquiry.'
        },
        label="I agree that Swarnav may contact me regarding this yatra inquiry."
    )

    class Meta:
        model = Inquiry
        fields = [
            'tour',
            'name',
            'phone',
            'departure_city',
            'total_pilgrims',
            'message',
            'consent_given',
        ]
        widgets = {
            'tour': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Ramesh Patel'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 9586825353 or +91 95868 25353'}),
            'departure_city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Surat, Ahmedabad, Rajkot'}),
            'total_pilgrims': forms.NumberInput(attrs={'class': 'form-input', 'min': '1', 'max': '100', 'placeholder': 'e.g. 4'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'rows': '2', 'placeholder': 'Preferred month, train/flight requests, or senior citizen care...'}),
            'consent_given': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
        labels = {
            'tour': 'Select Your Tour *',
            'name': 'Your Full Name *',
            'phone': 'Phone / WhatsApp *',
            'departure_city': 'Departure City (Home City)',
            'total_pilgrims': 'Total Pilgrims',
            'message': 'Message / Preferred Month',
            'consent_given': 'I agree that Swarnav may contact me regarding this yatra inquiry.',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError("Your name is required.")
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters.")
        return name

    def clean_phone(self):
        raw_phone = self.cleaned_data.get('phone', '')
        return clean_indian_phone(raw_phone)

    def clean_total_pilgrims(self):
        count = self.cleaned_data.get('total_pilgrims')
        if count is not None:
            if count < 1:
                raise forms.ValidationError("Number of pilgrims must be at least 1.")
            if count > 100:
                raise forms.ValidationError("For groups over 100 pilgrims, please contact our coordinator directly.")
        return count

    def clean_tour(self):
        tour = self.cleaned_data.get('tour')
        if not tour:
            raise forms.ValidationError("Please select a tour destination.")
        return tour
