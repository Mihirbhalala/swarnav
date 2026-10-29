from django.db import migrations

OLD_GUIDANCE = "at +91 95868 25353 or on WhatsApp"
NEW_GUIDANCE = "at +91 97274 23555 or on WhatsApp at +91 96241 68555"
OLD_NUMBER = "+91 95868 25353"
CALL_NUMBER = "+91 97274 23555"

TEXT_FIELDS = [
    "departures_guidance",
    "accommodation_summary",
    "meals_summary",
    "transport_summary",
    "confirmation_note",
    "gujarat_support_note",
    "brief_guide",
]


def update_contact_numbers(apps, schema_editor):
    """Replace the old single contact number in seeded tour text with the new call/WhatsApp numbers."""
    TourPackage = apps.get_model("yatras", "TourPackage")
    for tour in TourPackage.objects.all():
        changed = []
        for field in TEXT_FIELDS:
            value = getattr(tour, field) or ""
            if OLD_NUMBER in value:
                setattr(tour, field, value.replace(OLD_GUIDANCE, NEW_GUIDANCE).replace(OLD_NUMBER, CALL_NUMBER))
                changed.append(field)
        if changed:
            tour.save(update_fields=changed)


class Migration(migrations.Migration):

    dependencies = [
        ("yatras", "0004_tourpackage_tour_date"),
    ]

    operations = [
        migrations.RunPython(update_contact_numbers, migrations.RunPython.noop),
    ]
