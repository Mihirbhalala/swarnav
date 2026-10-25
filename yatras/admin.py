import copy
from django.contrib import admin, messages
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import path, reverse
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from unfold.decorators import display, action

from .models import (
    TourPackage,
    DhamDestination,
    ItineraryDay,
    PackageDetail,
    StayAndTravel,
    TravelGuide,
    PolicyAndFaq
)
from .forms import (
    TourPackageForm,
    ItineraryDayForm,
    PackageDetailForm,
    StayAndTravelForm,
    TravelGuideForm,
    PolicyAndFaqForm
)


# -----------------------------------------------------------------------------
# Unfold Tabbed Inlines (Presented as clean top-level tabs on the tour page)
# -----------------------------------------------------------------------------

class DhamDestinationInline(TabularInline):
    model = DhamDestination
    extra = 0
    tab = True
    fields = ('order', 'name', 'significance', 'highlight', 'image')
    ordering = ('order',)
    verbose_name = "Shrine / Stop"
    verbose_name_plural = "Dhams & Key Stops"


class ItineraryDayInline(TabularInline):
    model = ItineraryDay
    form = ItineraryDayForm
    extra = 0
    tab = True
    fields = ('day_number', 'title', 'starting_point', 'destination', 'night_stay', 'meals')
    ordering = ('day_number',)
    show_change_link = True
    verbose_name = "Itinerary Day"
    verbose_name_plural = "Day-by-Day Schedule"


class PackageDetailInline(StackedInline):
    model = PackageDetail
    form = PackageDetailForm
    can_delete = False
    max_num = 1
    tab = True
    verbose_name = "Inclusions & Exclusions"
    verbose_name_plural = "Inclusions & Booking Details"


class StayAndTravelInline(StackedInline):
    model = StayAndTravel
    form = StayAndTravelForm
    can_delete = False
    max_num = 1
    tab = True
    verbose_name = "Hotel & Travel Spec"
    verbose_name_plural = "Hotels & Transport Spec"


class TravelGuideInline(StackedInline):
    model = TravelGuide
    form = TravelGuideForm
    can_delete = False
    max_num = 1
    tab = True
    verbose_name = "Travel Preparation"
    verbose_name_plural = "Pilgrim Guide & Preparation"


class PolicyAndFaqInline(StackedInline):
    model = PolicyAndFaq
    form = PolicyAndFaqForm
    can_delete = False
    max_num = 1
    tab = True
    verbose_name = "Cancellation & Policies"
    verbose_name_plural = "Cancellation & Payment Policies"


# -----------------------------------------------------------------------------
# Main Tour Package Admin
# -----------------------------------------------------------------------------

@admin.register(TourPackage)
class TourPackageAdmin(ModelAdmin):
    form = TourPackageForm
    list_display = (
        'image_thumbnail',
        'name',
        'category',
        'is_active_toggle',
        'tour_date_column',
        'duration_display',
        'starting_price',
        'delete_action',
        'quick_actions'
    )
    class Media:
        js = ('js/admin_tour_date.js',)
    list_filter = ('is_active', 'category', 'status', 'is_completed', 'region')
    search_fields = ('name', 'subtitle', 'tagline', 'region', 'starting_city', 'brief_guide')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    readonly_fields = ('image_preview', 'active_status_banner')

    inlines = [
        DhamDestinationInline,
        ItineraryDayInline,
        PackageDetailInline,
        StayAndTravelInline,
        TravelGuideInline,
        PolicyAndFaqInline
    ]

    fieldsets = (
        ('Basic Information & Cover', {
            'classes': ('tab',),
            'fields': (
                'name',
                'slug',
                'category',
                'subtitle',
                'tagline',
                'region',
                'image_file',
                'image_preview',
                'image',
                'order'
            )
        }),
        ('Duration & Pricing', {
            'classes': ('tab',),
            'fields': (
                ('duration_days', 'duration_nights', 'duration_display'),
                ('starting_price', 'price_display', 'price_note')
            )
        }),
        ('Travel Logistics & Connectivity', {
            'classes': ('tab',),
            'fields': (
                ('starting_city', 'ending_city'),
                'origin',
                'home_city_connect',
                'departures_summary',
                'departures_guidance',
                'gujarat_support_note'
            )
        }),
        ('Summaries & Notes', {
            'classes': ('tab',),
            'fields': (
                'accommodation_summary',
                'meals_summary',
                'transport_summary',
                'confirmation_note',
                'brief_guide'
            )
        }),
        ('Bullet Lists (Line by Line)', {
            'classes': ('tab',),
            'fields': ('highlights', 'route_highlights', 'introduction')
        }),
        ('Publication & Season Batch', {
            'classes': ('tab',),
            'fields': (
                'active_status_banner',
                'is_active',
                'tour_date',
                'status',
                'status_label',
                'is_completed'
            )
        }),
    )

    actions = ['duplicate_selected_tours', 'mark_as_active', 'mark_as_upcoming']

    # Custom routes
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:tour_id>/duplicate/',
                self.admin_site.admin_view(self.duplicate_tour_view),
                name='yatras_tourpackage_duplicate',
            ),
            path(
                '<int:tour_id>/toggle-active/',
                self.admin_site.admin_view(self.toggle_active_view),
                name='yatras_tourpackage_toggle_active',
            ),
            path(
                '<int:tour_id>/set-date/',
                self.admin_site.admin_view(self.set_date_view),
                name='yatras_tourpackage_set_date',
            ),
        ]
        return custom_urls + urls

    def set_date_view(self, request, tour_id):
        """Quickly update or set the departure date / month for a tour from the changelist."""
        tour = get_object_or_404(TourPackage, pk=tour_id)
        if request.method in ['POST', 'GET']:
            new_date = (request.POST.get('tour_date') or request.GET.get('tour_date') or '').strip()
            tour.tour_date = new_date
            # If admin set a date, ensure tour is active
            if new_date and not tour.is_active:
                tour.is_active = True
                if tour.status in ['upcoming', 'draft']:
                    tour.status = 'active'
            tour.save()
            if new_date:
                self.message_user(
                    request,
                    f"✓ Tour departure date / month for '{tour.name}' set to: '{new_date}' (Live on website)",
                    level=messages.SUCCESS
                )
            else:
                self.message_user(
                    request,
                    f"ℹ️ Cleared departure date for '{tour.name}'.",
                    level=messages.INFO
                )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER') or reverse('admin:yatras_tourpackage_changelist'))

    def toggle_active_view(self, request, tour_id):
        """1-click toggle to activate or deactivate a yatra according to the season."""
        tour = get_object_or_404(TourPackage, pk=tour_id)
        tour.is_active = not tour.is_active
        if tour.is_active:
            if tour.status in ['upcoming', 'draft']:
                tour.status = 'active'
            self.message_user(
                request,
                f"✓ '{tour.name}' is now ACTIVE for the season! Batches are open. You can set its departure date/month in the column.",
                level=messages.SUCCESS
            )
        else:
            tour.status = 'upcoming'
            self.message_user(
                request,
                f"✗ '{tour.name}' is now DEACTIVATED (Season Closed / Not Active Yet).",
                level=messages.WARNING
            )
        tour.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER') or reverse('admin:yatras_tourpackage_changelist'))

    def duplicate_tour_view(self, request, tour_id):
        """View handler that duplicates a tour and redirects directly to editing the copy."""
        original_tour = get_object_or_404(TourPackage, pk=tour_id)
        new_tour = self._clone_tour(original_tour)
        self.message_user(
            request,
            f"✓ Duplicated '{original_tour.name}'! You are now editing the new draft copy.",
            level=messages.SUCCESS
        )
        change_url = reverse('admin:yatras_tourpackage_change', args=[new_tour.pk])
        return HttpResponseRedirect(change_url)

    def _clone_tour(self, original):
        """Deep copy a tour with all associated dhams, days, inclusions, and policies."""
        new_tour = TourPackage.objects.get(pk=original.pk)
        new_tour.pk = None
        new_tour.id = None

        # Build clean unique slug
        base_slug = f"{original.slug}-copy"
        slug = base_slug
        idx = 1
        while TourPackage.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{idx}"
            idx += 1
        new_tour.slug = slug
        new_tour.name = f"Copy of {original.name}"
        new_tour.status = 'draft'
        new_tour.status_label = 'Draft - Under Preparation'
        new_tour.is_active = False
        new_tour.is_completed = False

        # Put at the end of category ordering
        max_order = TourPackage.objects.filter(category=original.category).aggregate(models.Max('order'))['order__max'] or 0
        new_tour.order = max_order + 1
        new_tour.save()

        # Clone Dham Destinations
        for dham in original.dhams.all():
            DhamDestination.objects.create(
                tour=new_tour,
                order=dham.order,
                name=dham.name,
                significance=dham.significance,
                description=dham.description,
                highlight=dham.highlight,
                image=dham.image,
            )

        # Clone Itinerary Days
        for day in original.itinerary_days.all():
            ItineraryDay.objects.create(
                tour=new_tour,
                day_number=day.day_number,
                title=day.title,
                starting_point=day.starting_point,
                destination=day.destination,
                intro=day.intro,
                route_summary=day.route_summary,
                night_stay=day.night_stay,
                hotel_type=day.hotel_type,
                hotel_name=day.hotel_name,
                meals=day.meals,
                altitude=day.altitude,
                schedule=copy.deepcopy(day.schedule),
                darshan_tips=copy.deepcopy(day.darshan_tips),
                scenic_points=copy.deepcopy(day.scenic_points),
                places_covered=copy.deepcopy(day.places_covered),
                route_nodes=copy.deepcopy(day.route_nodes),
            )

        # Clone PackageDetail
        if hasattr(original, 'package_detail'):
            pd = original.package_detail
            PackageDetail.objects.create(
                tour=new_tour,
                inclusions=copy.deepcopy(pd.inclusions),
                exclusions=copy.deepcopy(pd.exclusions),
                pricing_structure=copy.deepcopy(pd.pricing_structure),
                booking_guidelines=copy.deepcopy(pd.booking_guidelines),
                key_highlights=copy.deepcopy(pd.key_highlights),
            )

        # Clone StayAndTravel
        if hasattr(original, 'stay_and_travel'):
            st = original.stay_and_travel
            StayAndTravel.objects.create(
                tour=new_tour,
                hotel_options=copy.deepcopy(st.hotel_options),
                vehicle_guidelines=copy.deepcopy(st.vehicle_guidelines),
                baggage_rules=copy.deepcopy(st.baggage_rules),
                meal_guidelines=copy.deepcopy(st.meal_guidelines),
            )

        # Clone TravelGuide
        if hasattr(original, 'travel_guide'):
            tg = original.travel_guide
            TravelGuide.objects.create(
                tour=new_tour,
                weather=copy.deepcopy(tg.weather),
                packing_list=copy.deepcopy(tg.packing_list),
                registration_process=copy.deepcopy(tg.registration_process),
                medical_advisory=copy.deepcopy(tg.medical_advisory),
                local_customs=copy.deepcopy(tg.local_customs),
                senior_citizen_tips=copy.deepcopy(tg.senior_citizen_tips),
            )

        # Clone PolicyAndFaq
        if hasattr(original, 'policies'):
            pf = original.policies
            PolicyAndFaq.objects.create(
                tour=new_tour,
                cancellation_policy=copy.deepcopy(pf.cancellation_policy),
                payment_terms=copy.deepcopy(pf.payment_terms),
                general_terms=copy.deepcopy(pf.general_terms),
                faqs=copy.deepcopy(pf.faqs),
            )

        return new_tour

    @display(description="Photo")
    def image_thumbnail(self, obj):
        url = obj.image_url
        return format_html(
            '<img src="{}" class="w-12 h-9 object-cover rounded shadow-sm border border-slate-200 dark:border-slate-700" alt="{}">',
            url,
            obj.name
        )

    @display(description="Current Image Preview")
    def image_preview(self, obj):
        if obj and obj.pk and obj.image:
            return format_html(
                '<div class="flex items-center gap-3">'
                '<img src="{}" class="h-24 w-36 object-cover rounded-lg shadow border border-slate-200 dark:border-slate-700">'
                '<span class="text-xs text-slate-500 font-mono">{}</span>'
                '</div>',
                obj.image_url,
                obj.image
            )
        return "No image selected"

    @display(description="Active Status", ordering="is_active")
    def is_active_toggle(self, obj):
        toggle_url = reverse('admin:yatras_tourpackage_toggle_active', args=[obj.pk])
        if obj.is_active:
            # Solid High-Visibility Green Tick Badge
            return format_html(
                '<a href="{}" class="yatra-status-active bg-emerald-500" style="display: inline-flex; align-items: center; gap: 7px; padding: 6px 14px; border-radius: 9999px; background-color: #16a34a !important; color: #ffffff !important; text-decoration: none !important; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif; font-size: 12px; font-weight: 800; letter-spacing: 0.04em; box-shadow: 0 2px 6px rgba(22, 163, 74, 0.45); border: 2px solid #ffffff; cursor: pointer; white-space: nowrap;" title="Yatra is ACTIVE (Click to Deactivate)">'
                '<span style="display: inline-flex; align-items: center; justify-content: center; width: 18px; height: 18px; min-width: 18px; border-radius: 50%; background-color: #ffffff; color: #16a34a;">'
                '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" style="display: block;">'
                '<polyline points="20 6 9 17 4 12"></polyline>'
                '</svg>'
                '</span>'
                '<span style="color: #ffffff !important; font-weight: 800;">Active</span>'
                '</a>',
                toggle_url
            )
        else:
            # Solid High-Visibility Red Cross Badge
            return format_html(
                '<a href="{}" class="yatra-status-inactive bg-rose-500" style="display: inline-flex; align-items: center; gap: 7px; padding: 6px 14px; border-radius: 9999px; background-color: #dc2626 !important; color: #ffffff !important; text-decoration: none !important; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif; font-size: 12px; font-weight: 800; letter-spacing: 0.04em; box-shadow: 0 2px 6px rgba(220, 38, 38, 0.45); border: 2px solid #ffffff; cursor: pointer; white-space: nowrap;" title="Yatra is NOT ACTIVE (Click to Activate)">'
                '<span style="display: inline-flex; align-items: center; justify-content: center; width: 18px; height: 18px; min-width: 18px; border-radius: 50%; background-color: #ffffff; color: #dc2626;">'
                '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" style="display: block;">'
                '<line x1="18" y1="6" x2="6" y2="18"></line>'
                '<line x1="6" y1="6" x2="18" y2="18"></line>'
                '</svg>'
                '</span>'
                '<span style="color: #ffffff !important; font-weight: 800;">Not Active</span>'
                '</a>',
                toggle_url
            )

    @display(description="Tour Date / Month", ordering="tour_date")
    def tour_date_column(self, obj):
        set_date_url = reverse('admin:yatras_tourpackage_set_date', args=[obj.pk])
        safe_name = obj.name.replace("'", "\\'").replace('"', '&quot;')
        safe_date = (obj.tour_date or "").replace("'", "\\'").replace('"', '&quot;')

        if obj.is_active:
            if obj.tour_date:
                return format_html(
                    '<div style="display: inline-flex; align-items: center; gap: 6px;">'
                    '<span style="display: inline-flex; align-items: center; gap: 6px; padding: 5px 12px; border-radius: 9999px; background: #ecfdf5; border: 1.5px solid #10b981; color: #047857; font-weight: 800; font-size: 12px; box-shadow: 0 1px 3px rgba(16, 185, 129, 0.2); white-space: nowrap;">'
                    '<span style="font-size: 13px;">📅</span>'
                    '<span>{}</span>'
                    '</span>'
                    '<button type="button" onclick="promptSetTourDate(\'{}\', \'{}\', \'{}\')" style="padding: 4px 6px; border-radius: 6px; background: #ffffff; border: 1px solid #cbd5e1; color: #475569; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; box-shadow: 0 1px 2px rgba(0,0,0,0.05); transition: all 0.15s;" onmouseover="this.style.backgroundColor=\'#f1f5f9\'; this.style.color=\'#15803d\';" onmouseout="this.style.backgroundColor=\'#ffffff\'; this.style.color=\'#475569\';" title="Edit Departure Date or Month">'
                    '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>'
                    '</button>'
                    '</div>',
                    obj.tour_date,
                    set_date_url,
                    safe_name,
                    safe_date
                )
            else:
                return format_html(
                    '<button type="button" onclick="promptSetTourDate(\'{}\', \'{}\', \'\')" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; background: #fffbeb; border: 1.5px dashed #f59e0b; color: #b45309; font-weight: 800; font-size: 12px; cursor: pointer; white-space: nowrap; box-shadow: 0 1px 3px rgba(245, 158, 11, 0.15); transition: all 0.15s;" onmouseover="this.style.backgroundColor=\'#fef3c7\'; this.style.borderColor=\'#d97706\';" onmouseout="this.style.backgroundColor=\'#fffbeb\'; this.style.borderColor=\'#f59e0b\';" title="Click to add specific date or month for this active tour">'
                    '<span style="font-size: 13px;">➕</span>'
                    '<span>Add Date / Month</span>'
                    '</button>',
                    set_date_url,
                    safe_name
                )
        else:
            return format_html(
                '<span style="display: inline-flex; align-items: center; gap: 4px; padding: 4px 10px; border-radius: 9999px; background: #f1f5f9; color: #94a3b8; font-size: 11px; font-weight: 600; white-space: nowrap;" title="Tour is inactive. Click \'Not Active\' in Active Status column to activate and set date.">'
                '<span>— Not Active —</span>'
                '</span>'
            )

    season_status_toggle = is_active_toggle  # Backward compatibility alias

    @display(description="Current Status Indicator")
    def active_status_banner(self, obj):
        if not obj or not obj.pk:
            return "Save package first"
        toggle_url = reverse('admin:yatras_tourpackage_toggle_active', args=[obj.pk])
        if obj.is_active:
            return format_html(
                '<div style="display: inline-flex; align-items: center; gap: 12px; padding: 12px 20px; border-radius: 12px; background-color: #dcfce7 !important; border: 2px solid #16a34a; box-shadow: 0 2px 8px rgba(22, 163, 74, 0.2); margin-bottom: 8px;">'
                '<span style="display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px; min-width: 32px; border-radius: 50%; background-color: #16a34a; color: #ffffff;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" style="display: block;"><polyline points="20 6 9 17 4 12"></polyline></svg>'
                '</span>'
                '<div>'
                '<div style="font-weight: 800; font-size: 14px; color: #15803d; letter-spacing: 0.02em;">✓ YATRA IS ACTIVE (LIVE ON WEBSITE)</div>'
                '<div style="font-size: 12px; color: #166534; margin-top: 2px;">Pilgrims can view and inquire for this package. <a href="{}" style="color: #dc2626; font-weight: 800; text-decoration: underline; margin-left: 8px;">Click here to Deactivate (Mark Not Active)</a></div>'
                '</div>'
                '</div>',
                toggle_url
            )
        else:
            return format_html(
                '<div style="display: inline-flex; align-items: center; gap: 12px; padding: 12px 20px; border-radius: 12px; background-color: #fee2e2 !important; border: 2px solid #dc2626; box-shadow: 0 2px 8px rgba(220, 38, 38, 0.2); margin-bottom: 8px;">'
                '<span style="display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px; min-width: 32px; border-radius: 50%; background-color: #dc2626; color: #ffffff;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" style="display: block;"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>'
                '</span>'
                '<div>'
                '<div style="font-weight: 800; font-size: 14px; color: #b91c1c; letter-spacing: 0.02em;">✗ YATRA IS NOT ACTIVE (SEASON CLOSED / UPCOMING)</div>'
                '<div style="font-size: 12px; color: #991b1b; margin-top: 2px;">This circuit is marked as not active / upcoming. <a href="{}" style="color: #16a34a; font-weight: 800; text-decoration: underline; margin-left: 8px;">Click here to Activate (Mark Active)</a></div>'
                '</div>'
                '</div>',
                toggle_url
            )

    @display(description="Delete")
    def delete_action(self, obj):
        delete_url = reverse('admin:yatras_tourpackage_delete', args=[obj.pk])
        return format_html(
            '<a href="{}" class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-red-50 text-red-600 hover:bg-red-600 hover:text-white border border-red-200 dark:bg-red-950/50 dark:text-red-400 dark:border-red-800 dark:hover:bg-red-600 dark:hover:text-white transition shadow-sm group" title="Delete \'{}\'" aria-label="Delete \'{}\'">'
            '<svg class="w-4 h-4 transition-transform group-hover:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            '<polyline points="3 6 5 6 21 6"></polyline>'
            '<path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>'
            '<line x1="10" y1="11" x2="10" y2="17"></line>'
            '<line x1="14" y1="11" x2="14" y2="17"></line>'
            '</svg>'
            '</a>',
            delete_url,
            obj.name,
            obj.name
        )

    @display(description="Actions")
    def quick_actions(self, obj):
        view_url = obj.get_absolute_url()
        duplicate_url = reverse('admin:yatras_tourpackage_duplicate', args=[obj.pk])
        delete_url = reverse('admin:yatras_tourpackage_delete', args=[obj.pk])
        return format_html(
            '<div class="flex items-center gap-1.5">'
            '<a href="{}" target="_blank" class="inline-flex items-center gap-1 px-2.5 py-1 text-xs font-semibold rounded bg-amber-50 text-amber-800 hover:bg-amber-100 dark:bg-amber-900/30 dark:text-amber-300" title="View tour on live website">👁️ View</a>'
            '<a href="{}" class="inline-flex items-center gap-1 px-2.5 py-1 text-xs font-semibold rounded bg-blue-50 text-blue-700 hover:bg-blue-100 dark:bg-blue-900/30 dark:text-blue-300" title="Duplicate as new draft yatra">📋 Duplicate</a>'
            '<a href="{}" class="inline-flex items-center gap-1 px-2.5 py-1 text-xs font-semibold rounded bg-red-50 text-red-600 hover:bg-red-600 hover:text-white border border-red-200 dark:bg-red-950/40 dark:text-red-400 dark:border-red-800 transition" title="Delete this Yatra">🗑️ Delete</a>'
            '</div>',
            view_url,
            duplicate_url,
            delete_url
        )

    @admin.action(description="📋 Duplicate selected tour(s) as Drafts")
    def duplicate_selected_tours(self, request, queryset):
        count = 0
        for tour in queryset:
            self._clone_tour(tour)
            count += 1
        self.message_user(request, f"✓ Successfully created {count} new tour draft duplicate(s).")

    @admin.action(description="✓ Activate selected yatras (Batches Open)")
    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True, status='active')
        self.message_user(request, f"✓ {queryset.count()} yatra(s) activated for the season.")

    @admin.action(description="✗ Deactivate selected yatras (Season Closed / Not Active)")
    def mark_as_upcoming(self, request, queryset):
        queryset.update(is_active=False, status='upcoming')
        self.message_user(request, f"✗ {queryset.count()} yatra(s) deactivated (marked as Not Active / Upcoming).")


# -----------------------------------------------------------------------------
# Itinerary Day Admin
# -----------------------------------------------------------------------------

@admin.register(ItineraryDay)
class ItineraryDayAdmin(ModelAdmin):
    form = ItineraryDayForm
    list_display = ('tour', 'day_badge', 'title', 'starting_point', 'destination', 'night_stay', 'meals', 'view_tour_link')
    list_filter = ('tour', 'night_stay')
    search_fields = ('title', 'intro', 'starting_point', 'destination', 'night_stay', 'hotel_name')
    ordering = ('tour', 'day_number')

    @display(description="Day")
    def day_badge(self, obj):
        return f"Day {obj.day_number}"

    @display(description="Tour Link")
    def view_tour_link(self, obj):
        return format_html(
            '<a href="{}" target="_blank" class="text-xs text-amber-600 hover:underline">👁️ Preview Tour</a>',
            obj.tour.get_absolute_url()
        )

    fieldsets = (
        ('Day Overview', {
            'fields': ('tour', 'day_number', 'title', 'route_summary', 'intro')
        }),
        ('Route & Transit', {
            'fields': (('starting_point', 'destination'), 'altitude')
        }),
        ('Accommodation & Food', {
            'fields': (('night_stay', 'hotel_type'), 'hotel_name', 'meals')
        }),
        ('Daily Schedule (No Code / Simple Input)', {
            'fields': ('schedule_morning', 'schedule_afternoon', 'schedule_evening', 'schedule_notes')
        }),
        ('Darshan & Scenic Tips (One per line)', {
            'fields': ('darshan_tips', 'scenic_points')
        }),
        ('Advanced Objects (JSON)', {
            'classes': ('collapse',),
            'fields': ('places_covered', 'route_nodes')
        }),
    )


# Note: DhamDestination, PackageDetail, StayAndTravel, TravelGuide, and PolicyAndFaq
# are managed directly as inlines inside TourPackageAdmin to keep the interface simple and uncluttered.
