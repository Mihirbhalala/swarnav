import logging
import urllib.parse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)


def send_admin_inquiry_notification(inquiry, site_url="http://127.0.0.1:8000"):
    """
    Send an email alert to the admin with complete inquiry details.
    Dispatches both HTML and plain-text formats.
    Handled with robust error catching so inquiry saving is never interrupted.
    """
    admin_email = getattr(settings, 'ADMIN_NOTIFICATION_EMAIL', 'admin@swarnavtravels.com')
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'Swarnav Tour & Travels <no-reply@swarnavtravels.com>')

    ref_id = f"SW-INQ-{inquiry.id:04d}"
    subject = f"🕉️ New Registration Inquiry #{ref_id}: {inquiry.name} - {inquiry.get_tour_display()}"
    base_url = getattr(settings, 'SITE_URL', None) or site_url
    admin_detail_url = f"{base_url}/admin/core/inquiry/{inquiry.id}/change/"

    # WhatsApp prefill link
    phone_clean = ''.join(filter(str.isdigit, inquiry.phone))
    if len(phone_clean) == 10:
        phone_clean = f"91{phone_clean}"
    greeting = f"Namaste {inquiry.name}, this is Swarnav Tour & Travels regarding your {inquiry.get_tour_display()} inquiry (#{ref_id})."
    whatsapp_url = f"https://wa.me/{phone_clean}?text={urllib.parse.quote(greeting)}"

    context = {
        'inquiry': inquiry,
        'inquiry_ref': ref_id,
        'admin_url': admin_detail_url,
        'whatsapp_url': whatsapp_url,
    }

    try:
        html_message = render_to_string('emails/admin_inquiry_notification.html', context)
        plain_message = (
            f"NEW REGISTRATION & BOOKING INQUIRY (#{ref_id})\n\n"
            f"Customer Name: {inquiry.name}\n"
            f"Phone / WhatsApp: {inquiry.phone}\n"
            f"Selected Tour: {inquiry.get_tour_display()}\n"
            f"Departure City: {inquiry.departure_city or 'Not specified'}\n"
            f"Total Pilgrims: {inquiry.total_pilgrims or '1'}\n"
            f"Notes / Message: {inquiry.message or 'None'}\n"
            f"Submitted: {inquiry.created_at}\n\n"
            f"View in Admin: {admin_detail_url}\n"
            f"Direct WhatsApp: {whatsapp_url}\n"
        )

        send_mail(
            subject=subject,
            message=plain_message,
            from_email=from_email,
            recipient_list=[admin_email],
            html_message=html_message,
            fail_silently=False,
        )
        logger.info("Admin inquiry notification email sent successfully for Inquiry #%s", inquiry.id)
        return True

    except Exception as exc:
        logger.exception("Failed to send admin notification email for Inquiry #%s: %s", inquiry.id, exc)
        return False
