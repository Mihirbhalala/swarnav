from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import TourCategory
from yatras.models import (
    TourPackage,
    DhamDestination,
    ItineraryDay,
    PackageDetail,
    StayAndTravel,
    TravelGuide,
    PolicyAndFaq
)
from yatras.forms import (
    LineSeparatedListWidget,
    LineSeparatedListFormField,
    TourPackageForm,
    ItineraryDayForm
)
from yatras.admin import TourPackageAdmin
from django.contrib.admin.sites import AdminSite


class MockAdminSite(AdminSite):
    pass


class YatrasAdminAndFormsTests(TestCase):
    def setUp(self):
        self.category = TourCategory.objects.create(
            name="North India Tours",
            slug="north-india",
            tagline="Sacred Shrines",
            order=1
        )
        self.tour = TourPackage.objects.create(
            category=self.category,
            slug="char-dham-test",
            name="Test Char Dham",
            starting_price="₹30,000",
            duration_days=13,
            duration_nights=12,
            duration_display="13 Days / 12 Nights",
            highlights=["Highlight 1", "Highlight 2"],
            status="active"
        )
        self.dham = DhamDestination.objects.create(
            tour=self.tour,
            order=1,
            name="Yamunotri",
            significance="Sacred Source"
        )
        self.day = ItineraryDay.objects.create(
            tour=self.tour,
            day_number=1,
            title="Surat to Haridwar",
            schedule={
                "morning": "Morning train journey",
                "afternoon": "Midway meal",
                "evening": "Arrival in Haridwar",
                "notes": "Keep tickets ready"
            }
        )
        self.detail = PackageDetail.objects.create(
            tour=self.tour,
            inclusions=["Train ticket", "Hotel stay"],
            exclusions=["Personal shopping"]
        )

        self.superuser = User.objects.create_superuser('adminuser', 'admin@example.com', 'adminpass123')
        self.client = Client()
        self.client.login(username='adminuser', password='adminpass123')

    def test_line_separated_list_widget_formatting(self):
        widget = LineSeparatedListWidget()
        formatted = widget.format_value(["Item One", "Item Two", "Item Three"])
        self.assertEqual(formatted, "Item One\nItem Two\nItem Three")

    def test_line_separated_list_widget_parsing(self):
        widget = LineSeparatedListWidget()
        parsed = widget.value_from_datadict(
            {'highlights': "Item One\n\nItem Two\nItem Three  \n"},
            {},
            'highlights'
        )
        self.assertEqual(parsed, ["Item One", "Item Two", "Item Three"])

    def test_itinerary_day_form_deconstructs_and_reconstructs_schedule(self):
        # 1. Test initialization extracts schedule fields
        form = ItineraryDayForm(instance=self.day)
        self.assertEqual(form.fields['schedule_morning'].initial, "Morning train journey")
        self.assertEqual(form.fields['schedule_afternoon'].initial, "Midway meal")
        self.assertEqual(form.fields['schedule_evening'].initial, "Arrival in Haridwar")
        self.assertEqual(form.fields['schedule_notes'].initial, "Keep tickets ready")

        # 2. Test saving form updates schedule dict cleanly
        data = {
            'tour': self.tour.pk,
            'day_number': 1,
            'title': "Surat to Haridwar (Updated)",
            'starting_point': 'Surat',
            'destination': 'Haridwar',
            'intro': 'Starting journey',
            'route_summary': 'Surat -> Haridwar',
            'night_stay': 'Haridwar',
            'hotel_type': 'Economy',
            'hotel_name': 'Hotel Ganga',
            'meals': 'Dinner',
            'altitude': '300m',
            'schedule_morning': 'Updated morning schedule',
            'schedule_afternoon': 'Updated afternoon schedule',
            'schedule_evening': 'Updated evening schedule',
            'schedule_notes': 'Carry photo ID',
            'darshan_tips': 'Tip 1\nTip 2',
            'scenic_points': 'Point 1\nPoint 2',
            'places_covered': '[]',
            'route_nodes': '[]'
        }
        form_post = ItineraryDayForm(data=data, instance=self.day)
        self.assertTrue(form_post.is_valid(), form_post.errors)
        saved_day = form_post.save()
        self.assertEqual(saved_day.schedule['morning'], 'Updated morning schedule')
        self.assertEqual(saved_day.schedule['notes'], 'Carry photo ID')
        self.assertEqual(saved_day.darshan_tips, ['Tip 1', 'Tip 2'])

    def test_tour_duplication(self):
        admin_instance = TourPackageAdmin(TourPackage, MockAdminSite())
        cloned_tour = admin_instance._clone_tour(self.tour)

        # Check basic properties
        self.assertTrue(cloned_tour.pk)
        self.assertNotEqual(cloned_tour.pk, self.tour.pk)
        self.assertEqual(cloned_tour.status, 'draft')
        self.assertFalse(cloned_tour.is_active)
        self.assertFalse(cloned_tour.is_completed)
        self.assertIn("Copy of", cloned_tour.name)
        self.assertIn("copy", cloned_tour.slug)

        # Check related models cloned
        self.assertEqual(cloned_tour.dhams.count(), 1)
        self.assertEqual(cloned_tour.dhams.first().name, "Yamunotri")

        self.assertEqual(cloned_tour.itinerary_days.count(), 1)
        cloned_day = cloned_tour.itinerary_days.first()
        self.assertEqual(cloned_day.title, "Surat to Haridwar")
        self.assertEqual(cloned_day.schedule['morning'], "Morning train journey")

        self.assertTrue(hasattr(cloned_tour, 'package_detail'))
        self.assertEqual(cloned_tour.package_detail.inclusions, ["Train ticket", "Hotel stay"])

    def test_tour_duplicate_endpoint(self):
        url = reverse('admin:yatras_tourpackage_duplicate', args=[self.tour.pk])
        response = self.client.get(url, follow=False)
        self.assertEqual(response.status_code, 302)
        # Verify a new draft tour exists
        self.assertTrue(TourPackage.objects.filter(slug__contains="copy").exists())

    def test_tour_toggle_active_endpoint(self):
        admin_instance = TourPackageAdmin(TourPackage, MockAdminSite())
        
        # Initially self.tour has is_active=True
        self.assertTrue(self.tour.is_active)
        toggle_html = admin_instance.season_status_toggle(self.tour)
        self.assertIn('bg-emerald-500', toggle_html)
        self.assertIn('Active', toggle_html)

        # Call toggle endpoint
        url = reverse('admin:yatras_tourpackage_toggle_active', args=[self.tour.pk])
        response = self.client.get(url, follow=False)
        self.assertEqual(response.status_code, 302)

        self.tour.refresh_from_db()
        self.assertFalse(self.tour.is_active)
        self.assertEqual(self.tour.status, 'upcoming')

        # Now renders red cross
        toggle_html_inactive = admin_instance.season_status_toggle(self.tour)
        self.assertIn('bg-rose-500', toggle_html_inactive)
        self.assertIn('Not Active', toggle_html_inactive)

        # Toggle back to active
        response = self.client.get(url, follow=False)
        self.assertEqual(response.status_code, 302)
        self.tour.refresh_from_db()
        self.assertTrue(self.tour.is_active)
        self.assertEqual(self.tour.status, 'active')

    def test_tour_delete_action_rendering(self):
        admin_instance = TourPackageAdmin(TourPackage, MockAdminSite())
        del_html = admin_instance.delete_action(self.tour)
        self.assertIn(reverse('admin:yatras_tourpackage_delete', args=[self.tour.pk]), del_html)
        self.assertIn('Delete', del_html)

    def test_tour_package_image_url_and_absolute_url(self):
        # Manifest storage may add a content hash, e.g. kedarnath-temple.949051622a87.jpg
        self.assertRegex(self.tour.image_url, r"kedarnath-temple(\.[0-9a-f]+)?\.jpg$")
        self.assertIn("#tour-char-dham-test", self.tour.get_absolute_url())


class KashmirTourTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_kashmir_overview_page_loads(self):
        response = self.client.get(reverse('yatras:kashmir_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kashmir Paradise')
        self.assertContains(response, 'Opening New Batch in December')
        self.assertContains(response, 'Surat')
        self.assertContains(response, 'Mata Vaishno Devi')
        self.assertContains(response, 'Amritsar')

    def test_kashmir_itinerary_page_loads(self):
        response = self.client.get(reverse('yatras:kashmir_itinerary'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '11-Day')
        for day in range(1, 12):
            self.assertContains(response, f'Day {day}')

    def test_all_11_kashmir_day_detail_pages_load(self):
        for day_num in range(1, 12):
            url = reverse('yatras:kashmir_day_detail', kwargs={'day_number': day_num})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"Day {day_num} failed with status {response.status_code}")
            self.assertContains(response, f"Day {day_num}")

    def test_kashmir_day_detail_invalid_day_returns_404(self):
        url = reverse('yatras:kashmir_day_detail', kwargs={'day_number': 12})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_kashmir_package_details_page_loads(self):
        response = self.client.get(reverse('yatras:kashmir_package_details'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Package Inclusions')
        self.assertContains(response, 'Package Exclusions')

    def test_kashmir_stay_and_travel_page_loads(self):
        response = self.client.get(reverse('yatras:kashmir_stay_and_travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Accommodation Information')
        self.assertContains(response, 'Meal Arrangements')

    def test_kashmir_travel_guide_page_loads(self):
        response = self.client.get(reverse('yatras:kashmir_travel_guide'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Winter Preparation')
        self.assertContains(response, 'December Winter Weather Advisory')

    def test_kashmir_policies_page_loads(self):
        response = self.client.get(reverse('yatras:kashmir_policies'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Booking Terms &amp; Cancellation Policies')

    def test_homepage_shows_kashmir_tour_as_completed(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Opening New Batch in December')
        self.assertContains(response, reverse('yatras:kashmir_overview'))


class RameshwaramTourTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_rameshwaram_overview_page_loads(self):
        response = self.client.get(reverse('yatras:rameshwaram_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rameshwaram')
        self.assertContains(response, '30,000')
        self.assertContains(response, '12 Days')
        self.assertContains(response, 'Surat')
        self.assertContains(response, 'Madurai')
        self.assertContains(response, 'Meenakshi')

    def test_rameshwaram_itinerary_page_loads(self):
        response = self.client.get(reverse('yatras:rameshwaram_itinerary'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '12-Day')
        for day in range(1, 13):
            self.assertContains(response, f'Day {day}')

    def test_all_12_rameshwaram_day_detail_pages_load(self):
        for day_num in range(1, 13):
            url = reverse('yatras:rameshwaram_day_detail', kwargs={'day_number': day_num})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"Day {day_num} failed with status {response.status_code}")
            self.assertContains(response, f"Day {day_num}")

    def test_rameshwaram_day_detail_invalid_day_returns_404(self):
        url = reverse('yatras:rameshwaram_day_detail', kwargs={'day_number': 13})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

        url_zero = reverse('yatras:rameshwaram_day_detail', kwargs={'day_number': 0})
        response_zero = self.client.get(url_zero)
        self.assertEqual(response_zero.status_code, 404)

    def test_rameshwaram_package_details_page_loads(self):
        response = self.client.get(reverse('yatras:rameshwaram_package_details'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Package Inclusions')
        self.assertContains(response, 'Package Exclusions')
        self.assertContains(response, '30,000')

    def test_rameshwaram_stay_and_travel_page_loads(self):
        response = self.client.get(reverse('yatras:rameshwaram_stay_and_travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Accommodation Information')
        self.assertContains(response, 'Meal Arrangements')
        self.assertContains(response, 'Breakfast Policy')

    def test_rameshwaram_travel_guide_page_loads(self):
        response = self.client.get(reverse('yatras:rameshwaram_travel_guide'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Travel Guide')
        self.assertContains(response, 'dress code')

    def test_rameshwaram_policies_page_loads(self):
        response = self.client.get(reverse('yatras:rameshwaram_policies'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Booking Terms &amp; Cancellation Policies')

    def test_homepage_shows_rameshwaram_tour_as_completed(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rameshwaram')
        self.assertContains(response, '30,000')
        self.assertContains(response, reverse('yatras:rameshwaram_overview'))


class KeralaTourTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_kerala_overview_page_loads(self):
        response = self.client.get(reverse('yatras:kerala_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kerala')
        self.assertContains(response, '32,000')
        self.assertContains(response, '13 Days')
        self.assertContains(response, 'Surat')
        self.assertContains(response, 'Munnar')
        self.assertContains(response, 'Alleppey')

    def test_kerala_itinerary_page_loads(self):
        response = self.client.get(reverse('yatras:kerala_itinerary'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '13-Day')
        for day in range(1, 14):
            self.assertContains(response, f'Day {day}')

    def test_all_13_kerala_day_detail_pages_load(self):
        for day_num in range(1, 14):
            url = reverse('yatras:kerala_day_detail', kwargs={'day_number': day_num})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"Day {day_num} failed with status {response.status_code}")
            self.assertContains(response, f"Day {day_num}")

    def test_kerala_day_detail_invalid_day_returns_404(self):
        url = reverse('yatras:kerala_day_detail', kwargs={'day_number': 14})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

        url_zero = reverse('yatras:kerala_day_detail', kwargs={'day_number': 0})
        response_zero = self.client.get(url_zero)
        self.assertEqual(response_zero.status_code, 404)

    def test_kerala_package_details_page_loads(self):
        response = self.client.get(reverse('yatras:kerala_package_details'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Package Inclusions')
        self.assertContains(response, 'Package Exclusions')
        self.assertContains(response, '32,000')

    def test_kerala_stay_and_travel_page_loads(self):
        response = self.client.get(reverse('yatras:kerala_stay_and_travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Accommodation Information')
        self.assertContains(response, 'Meal Arrangements')
        self.assertContains(response, 'Breakfast Policy')

    def test_kerala_travel_guide_page_loads(self):
        response = self.client.get(reverse('yatras:kerala_travel_guide'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Travel Guide')
        self.assertContains(response, 'Padmanabhaswamy')

    def test_kerala_policies_page_loads(self):
        response = self.client.get(reverse('yatras:kerala_policies'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Booking Terms &amp; Cancellation Policies')

    def test_homepage_shows_kerala_tour_as_completed(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kerala')
        self.assertContains(response, '32,000')
        self.assertContains(response, reverse('yatras:kerala_overview'))


class TourDateAdminAndHighlightTests(TestCase):
    def setUp(self):
        self.category = TourCategory.objects.create(
            name="North India Tours",
            slug="north-india-date-test",
            tagline="Sacred Shrines",
            order=1
        )
        self.tour = TourPackage.objects.create(
            category=self.category,
            slug="char-dham-date-test",
            name="Test Date Tour",
            starting_price="₹30,000",
            duration_days=13,
            duration_nights=12,
            duration_display="13 Days / 12 Nights",
            is_active=True,
            status="active"
        )

    def test_tour_date_column_rendering(self):
        site = MockAdminSite()
        admin_obj = TourPackageAdmin(TourPackage, site)

        # 1. Active with specific date
        self.tour.is_active = True
        self.tour.tour_date = "15 Nov 2026"
        self.tour.save()
        html = admin_obj.tour_date_column(self.tour)
        self.assertIn("15 Nov 2026", str(html))
        self.assertIn("promptSetTourDate", str(html))

        # 2. Active with month
        self.tour.tour_date = "November 2026"
        self.tour.save()
        html_month = admin_obj.tour_date_column(self.tour)
        self.assertIn("November 2026", str(html_month))

        # 3. Active without date (shows prompt to add)
        self.tour.tour_date = ""
        self.tour.save()
        html_empty = admin_obj.tour_date_column(self.tour)
        self.assertIn("Add Date / Month", str(html_empty))

        # 4. Inactive tour
        self.tour.is_active = False
        self.tour.save()
        html_inactive = admin_obj.tour_date_column(self.tour)
        self.assertIn("Not Active", str(html_inactive))

    def test_set_date_view(self):
        admin_user = User.objects.create_superuser('admin_date_user', 'admin_date@example.com', 'password123')
        client = Client()
        client.force_login(admin_user)

        set_date_url = reverse('admin:yatras_tourpackage_set_date', args=[self.tour.id])

        # Set specific date
        response = client.post(set_date_url, {'tour_date': '20 Nov 2026'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.tour.refresh_from_db()
        self.assertEqual(self.tour.tour_date, '20 Nov 2026')
        self.assertTrue(self.tour.is_active)

        # Set month
        response = client.get(f"{set_date_url}?tour_date=December 2026", follow=True)
        self.assertEqual(response.status_code, 200)
        self.tour.refresh_from_db()
        self.assertEqual(self.tour.tour_date, 'December 2026')

    def test_homepage_highlights_active_tour_date(self):
        self.tour.is_active = True
        self.tour.tour_date = "15 Nov 2026"
        self.tour.save()

        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Tour Departure')
        self.assertContains(response, '15 Nov 2026')


