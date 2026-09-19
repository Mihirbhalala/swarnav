import csv
from django.http import HttpResponse
from django.utils import timezone


def export_inquiries_to_excel_response(queryset, filename_prefix="swarnav_inquiries"):
    """
    Export an Inquiry queryset as an Excel-compatible CSV file (with UTF-8 BOM).
    Opens cleanly in Microsoft Excel, Google Sheets, and LibreOffice.
    """
    timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.csv"

    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    writer = csv.writer(response)
    # Header Row
    writer.writerow([
        'Inquiry ID',
        'Reference Number',
        'Submission Date & Time (IST)',
        'Customer Name',
        'Phone / WhatsApp',
        'Selected Tour',
        'Departure City',
        'Total Pilgrims',
        'Status',
        'Consent Given',
        'Customer Message / Requirements',
        'Admin Notes',
        'Last Updated'
    ])

    for inq in queryset:
        created_str = inq.created_at.strftime("%d-%b-%Y %I:%M %p") if inq.created_at else ""
        updated_str = inq.updated_at.strftime("%d-%b-%Y %I:%M %p") if inq.updated_at else ""
        writer.writerow([
            inq.id,
            f"SW-INQ-{inq.id:04d}",
            created_str,
            inq.name,
            inq.phone,
            inq.get_tour_display(),
            inq.departure_city or "Not specified",
            inq.total_pilgrims if inq.total_pilgrims is not None else "Not specified",
            inq.get_status_display(),
            "Yes" if inq.consent_given else "No",
            inq.message or "",
            inq.admin_notes or "",
            updated_str
        ])

    return response
