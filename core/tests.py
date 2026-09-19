import json
import urllib.parse
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import mail
from core.models import Inquiry
from core.forms import InquiryForm, clean_indian_phone
from core.views import build_whatsapp_url
from core.email_utils import send_admin_inquiry_notification

User = get_user_model()




class InquiryModelAndFormTests(TestCase):
    """Unit tests for Inquiry model, phone validator, and InquiryForm."""

    def test_inquiry_creation_and_defaults(self):
        """Test Inquiry model creation, default status, and string representation."""
        inquiry = Inquiry.objects.create(
            tour='char-dham',
            name='Test Pilgrim',
            phone='+919876543210',
            departure_city='Surat',
            total_pilgrims=4,
            message='Need senior citizen assistance',
            consent_given=True
        )
        self.assertEqual(Inquiry.objects.count(), 1)
        self.assertEqual(inquiry.status, 'new')
        self.assertTrue(inquiry.consent_given)
        self.assertIn('Test Pilgrim', str(inquiry))
        self.assertIn('Char Dham', str(inquiry))

    def test_phone_validation_valid_formats(self):
        """Accept common valid Indian phone formats and normalize them."""
        valid_cases = [
            ('9876543210', '+919876543210'),
            ('+91 98765 43210', '+919876543210'),
            ('+919876543210', '+919876543210'),
            ('919876543210', '+919876543210'),
            ('09876543210', '+919876543210'),
            ('98765-43210', '+919876543210'),
            ('7890123456', '+917890123456'),
            ('6123456789', '+916123456789'),
        ]
        for raw, expected in valid_cases:
            with self.subTest(raw=raw):
                self.assertEqual(clean_indian_phone(raw), expected)

    def test_phone_validation_invalid_formats(self):
        """Reject alpha, too short, too long, or invalid prefix phone numbers."""
        invalid_cases = [
            '',
            'abc9876543',
            '12345',
            '1234567890',  # Does not start with 6-9
            '98765432109876',  # Excessively long
            'phone-number',
            '5555555555',  # Starts with 5
        ]
        for invalid in invalid_cases:
            with self.subTest(invalid=invalid):
                form = InquiryForm(data={
                    'tour': 'char-dham',
                    'name': 'Sample User',
                    'phone': invalid,
                    'consent_given': True,
                })
                self.assertFalse(form.is_valid())
                self.assertIn('phone', form.errors)

    def test_total_pilgrims_validation(self):
        """Total pilgrims must be at least 1 and within reasonable limits."""
        # Zero rejected
        form_zero = InquiryForm(data={
            'tour': 'char-dham',
            'name': 'Sample User',
            'phone': '9876543210',
            'total_pilgrims': 0,
            'consent_given': True,
        })
        self.assertFalse(form_zero.is_valid())
        self.assertIn('total_pilgrims', form_zero.errors)

        # Negative rejected
        form_neg = InquiryForm(data={
            'tour': 'char-dham',
            'name': 'Sample User',
            'phone': '9876543210',
            'total_pilgrims': -3,
            'consent_given': True,
        })
        self.assertFalse(form_neg.is_valid())
        self.assertIn('total_pilgrims', form_neg.errors)

        # Over upper limit rejected
        form_over = InquiryForm(data={
            'tour': 'char-dham',
            'name': 'Sample User',
            'phone': '9876543210',
            'total_pilgrims': 150,
            'consent_given': True,
        })
        self.assertFalse(form_over.is_valid())
        self.assertIn('total_pilgrims', form_over.errors)

    def test_missing_consent_rejected(self):
        """Consent must be checked; uncheck is invalid."""
        form = InquiryForm(data={
            'tour': 'char-dham',
            'name': 'Sample User',
            'phone': '9876543210',
            'consent_given': False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('consent_given', form.errors)

    def test_optional_fields_can_be_blank(self):
        """Departure city, total pilgrims, and message may be left blank."""
        form = InquiryForm(data={
            'tour': 'char-dham',
            'name': 'Sample User',
            'phone': '9876543210',
            'departure_city': '',
            'total_pilgrims': '',
            'message': '',
            'consent_given': True,
        })
        self.assertTrue(form.is_valid())
        inquiry = form.save()
        self.assertEqual(inquiry.departure_city, '')
        self.assertIsNone(inquiry.total_pilgrims)
        self.assertEqual(inquiry.message, '')


class InquirySubmissionViewTests(TestCase):
    """Tests for HTTP POST endpoints, database persistence, and WhatsApp link generation."""

    def setUp(self):
        self.client = Client()
        self.submit_url = reverse('core:submit_inquiry')

    def test_get_request_rejected_on_submit_inquiry(self):
        """submit-inquiry must only accept POST requests."""
        response = self.client.get(self.submit_url)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

    def test_valid_json_submission_creates_one_inquiry_and_returns_whatsapp_url(self):
        """Valid JSON AJAX POST creates exactly one inquiry in DB and returns encoded WhatsApp URL."""
        payload = {
            'tour': 'char-dham',
            'name': 'Amit Shah',
            'phone': '9876543210',
            'departure_city': 'Ahmedabad',
            'total_pilgrims': 3,
            'message': 'Planning for May batch',
            'consent_given': True,
        }
        response = self.client.post(
            self.submit_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('whatsapp_url', data)
        self.assertIn('wa.me/919586825353', data['whatsapp_url'])
        self.assertIn('success_url', data)

        # Database verification
        self.assertEqual(Inquiry.objects.count(), 1)
        inquiry = Inquiry.objects.first()
        self.assertEqual(inquiry.name, 'Amit Shah')
        self.assertEqual(inquiry.phone, '+919876543210')
        self.assertEqual(inquiry.departure_city, 'Ahmedabad')
        self.assertEqual(inquiry.total_pilgrims, 3)
        self.assertEqual(inquiry.status, 'new')
        self.assertTrue(inquiry.consent_given)

        # Email notification verification
        self.assertEqual(len(mail.outbox), 1)
        sent_mail = mail.outbox[0]
        self.assertIn('Amit Shah', sent_mail.subject)
        from django.conf import settings
        self.assertIn(settings.ADMIN_NOTIFICATION_EMAIL, sent_mail.to)
        self.assertIn('Ahmedabad', sent_mail.body)


    def test_invalid_json_submission_creates_no_record(self):
        """Invalid submission (missing name or invalid phone) must create 0 database records."""
        payload = {
            'tour': 'char-dham',
            'name': '',
            'phone': 'invalid-phone',
            'consent_given': False,
        }
        response = self.client.post(
            self.submit_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(Inquiry.objects.count(), 0)

    def test_whatsapp_message_encoding_and_content(self):
        """Verify build_whatsapp_url encodes reference ID, tour, name, phone, city, pilgrims, and notes."""
        inquiry = Inquiry.objects.create(
            tour='char-dham',
            name='Rajesh Kumar',
            phone='+919876543210',
            departure_city='Vadodara',
            total_pilgrims=5,
            message='Requires 2 ground floor rooms',
            consent_given=True
        )
        url = build_whatsapp_url(inquiry)
        self.assertTrue(url.startswith('https://wa.me/919586825353?text='))
        
        # Decode and verify text content
        query_part = url.split('text=')[1]
        decoded_text = urllib.parse.unquote(query_part)
        self.assertIn('Rajesh Kumar', decoded_text)
        self.assertIn('+919876543210', decoded_text)
        self.assertIn('Char Dham Yatra', decoded_text)
        self.assertIn('Vadodara', decoded_text)
        self.assertIn('5', decoded_text)
        self.assertIn('Requires 2 ground floor rooms', decoded_text)
        self.assertIn(f"SW-INQ-{inquiry.id:04d}", decoded_text)

    def test_inquiry_success_page_loads(self):
        """inquiry_success page displays reference ID, summary details, and return links."""
        inquiry = Inquiry.objects.create(
            tour='char-dham',
            name='Bhavin Patel',
            phone='+919876543210',
            departure_city='Surat',
            total_pilgrims=2,
            consent_given=True
        )
        success_url = reverse('core:inquiry_success', args=[inquiry.id])
        response = self.client.get(success_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"SW-INQ-{inquiry.id:04d}")
        self.assertContains(response, "Bhavin Patel")
        self.assertContains(response, "Continue to WhatsApp Desk")
        self.assertContains(response, reverse('yatras:char_dham_overview'))


class AdminSecurityAndAccessTests(TestCase):
    """Tests for Django Admin protection, role access, and actions."""

    def setUp(self):
        self.client = Client()
        self.admin_url = '/admin/'
        self.inquiry_changelist_url = '/admin/core/inquiry/'
        self.superuser = User.objects.create_superuser(
            username='adminuser',
            password='ComplexAdminPassword123!',
            email='admin@swarnavtravels.com'
        )
        self.inquiry = Inquiry.objects.create(
            tour='char-dham',
            name='Kishore Dave',
            phone='+919876543210',
            departure_city='Surat',
            total_pilgrims=4,
            message='Private inquiries note test',
            admin_notes='VIP customer contact on Monday',
            consent_given=True
        )

    def test_admin_requires_authentication(self):
        """Unauthenticated visitor cannot access admin changelist or detail view."""
        response = self.client.get(self.inquiry_changelist_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_superuser_can_view_inquiries_and_admin_notes(self):
        """Logged-in superuser can view inquiries in admin list and detail view."""
        self.client.login(username='adminuser', password='ComplexAdminPassword123!')
        response = self.client.get(self.inquiry_changelist_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kishore Dave')
        self.assertContains(response, 'Swarnav Administration')

        detail_url = f"/admin/core/inquiry/{self.inquiry.id}/change/"
        detail_resp = self.client.get(detail_url)
        self.assertEqual(detail_resp.status_code, 200)
        self.assertContains(detail_resp, 'VIP customer contact on Monday')
        self.assertContains(detail_resp, 'Open WhatsApp with Customer')

    def test_admin_actions(self):
        """Admin actions mark inquiry statuses cleanly."""
        self.client.login(username='adminuser', password='ComplexAdminPassword123!')
        
        # Test Contacted action
        self.client.post(self.inquiry_changelist_url, {
            'action': 'mark_as_contacted',
            '_selected_action': [str(self.inquiry.id)],
        })
        self.inquiry.refresh_from_db()
        self.assertEqual(self.inquiry.status, 'contacted')

        # Test Converted action
        self.client.post(self.inquiry_changelist_url, {
            'action': 'mark_as_converted',
            '_selected_action': [str(self.inquiry.id)],
        })
        self.inquiry.refresh_from_db()
        self.assertEqual(self.inquiry.status, 'converted')

        # Test Export to Excel Admin Action
        excel_resp = self.client.post(self.inquiry_changelist_url, {
            'action': 'export_selected_to_excel',
            '_selected_action': [str(self.inquiry.id)],
        })
        self.assertEqual(excel_resp.status_code, 200)
        self.assertEqual(excel_resp['Content-Type'], 'text/csv; charset=utf-8-sig')
        self.assertIn('attachment;', excel_resp['Content-Disposition'])
        self.assertContains(excel_resp, 'Kishore Dave')
        self.assertContains(excel_resp, 'Char Dham Yatra')

    def test_inquiry_pdf_view_renders(self):
        """Inquiry PDF summary slip page loads with voucher data."""
        pdf_url = reverse('core:inquiry_pdf', args=[self.inquiry.id])
        res = self.client.get(pdf_url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, f"SW-INQ-{self.inquiry.id:04d}")
        self.assertContains(res, "Kishore Dave")
        self.assertContains(res, "Print / Save as PDF")

    def test_excel_export_endpoint_requires_staff(self):
        """Direct Excel export endpoint requires staff authentication."""
        export_url = reverse('core:inquiry_export_excel')
        # Anonymous fails
        anon_resp = self.client.get(export_url)
        self.assertEqual(anon_resp.status_code, 302)

        # Superuser succeeds
        self.client.login(username='adminuser', password='ComplexAdminPassword123!')
        staff_resp = self.client.get(export_url)
        self.assertEqual(staff_resp.status_code, 200)
        self.assertEqual(staff_resp['Content-Type'], 'text/csv; charset=utf-8-sig')
        self.assertContains(staff_resp, 'Kishore Dave')

    def test_public_pages_do_not_expose_admin_notes(self):

        """Public views (home, char dham pages, success page) must never expose admin_notes."""
        public_urls = [
            reverse('core:home'),
            reverse('core:inquiry_success', args=[self.inquiry.id]),
            reverse('yatras:char_dham_overview'),
            reverse('yatras:char_dham_itinerary'),
        ]
        for url in public_urls:
            with self.subTest(url=url):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 200)
                self.assertNotContains(res, 'VIP customer contact on Monday')


class ExistingWebsitePagesTests(TestCase):
    """Ensure existing pages, navigation, and contact links remain functional."""

    def setUp(self):
        self.client = Client()

    def test_existing_pages_render_with_200(self):
        urls = [
            reverse('core:home'),
            reverse('yatras:char_dham_overview'),
            reverse('yatras:char_dham_itinerary'),
            reverse('yatras:char_dham_package_details'),
            reverse('yatras:char_dham_stay_and_travel'),
            reverse('yatras:char_dham_travel_guide'),
            reverse('yatras:char_dham_policies'),
        ]
        for url in urls:
            with self.subTest(url=url):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 200)
                # Ensure business phone and WhatsApp links exist
                self.assertContains(res, '+91 95868 25353')
                self.assertContains(res, 'wa.me/919586825353')


class AIAssistantEndpointTests(TestCase):
    """Test suite for AI Assistant RAG, Tools, and Chat endpoints."""

    def setUp(self):
        self.client = Client()
        from yatras.models import TourPackage, ItineraryDay
        self.tour = TourPackage.objects.create(
            name="Char Dham Yatra",
            slug="char-dham",
            duration_days=13,
            duration_nights=12,
            starting_price="₹30,000",
            status="active"
        )
        self.day7 = ItineraryDay.objects.create(
            tour=self.tour,
            day_number=7,
            title="Sonprayag to Kedarnath",
            starting_point="Sonprayag",
            destination="Kedarnath",
            altitude="3,583 m (11,755 ft)",
            night_stay="Kedarnath Base Camp",
            route_summary="Sonprayag ➔ Gaurikund ➔ Kedarnath (16 km Trek)"
        )

    def test_ai_chat_api_empty_message_returns_400(self):
        """Chat API rejects empty messages."""
        url = reverse('core:ai_chat_api')
        res = self.client.post(url, data=json.dumps({"message": ""}), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        data = res.json()
        self.assertFalse(data['success'])

    def test_ai_chat_api_valid_query_returns_success(self):
        """Chat API answers itinerary questions with grounded content."""
        url = reverse('core:ai_chat_api')
        res = self.client.post(
            url,
            data=json.dumps({"message": "What is the package price and route for Char Dham?"}),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data['success'])
        self.assertIn("reply", data)
        self.assertTrue(len(data['suggested_questions']) > 0)

    def test_ai_chat_api_records_lead_and_returns_whatsapp_card(self):
        """Providing contact intent creates a database Inquiry and generates WhatsApp link."""
        from core.models import Inquiry
        initial_count = Inquiry.objects.count()

        url = reverse('core:ai_chat_api')
        res = self.client.post(
            url,
            data=json.dumps({"message": "Please book 2 seats for Char Dham. My name is Jayesh and phone is 9876543210"}),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data['success'])
        self.assertIsNotNone(data.get('action_card'))
        self.assertEqual(data['action_card']['type'], 'lead_created')
        self.assertIn("whatsapp_link", data['action_card'])

        # Verify Inquiry was saved in DB
        self.assertEqual(Inquiry.objects.count(), initial_count + 1)
        new_inq = Inquiry.objects.latest('id')
        self.assertEqual(new_inq.phone, '9876543210')

    def test_ai_reset_api_clears_session(self):
        """Reset endpoint empties session conversation memory."""
        session = self.client.session
        session['ai_chat_history'] = [{"sender": "user", "text": "hello"}]
        session.save()

        url = reverse('core:ai_reset_api')
        res = self.client.post(url)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data['success'])

        # Verify session cleared
        updated_session = self.client.session
        self.assertEqual(updated_session.get('ai_chat_history'), [])
