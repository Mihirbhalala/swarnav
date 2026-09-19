from django.contrib import admin
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


class DhamDestinationInline(TabularInline):
    model = DhamDestination
    extra = 0
    fields = ('order', 'name', 'significance', 'highlight', 'image')
    ordering = ('order',)


class ItineraryDayInline(TabularInline):
    model = ItineraryDay
    extra = 0
    fields = ('day_number', 'title', 'starting_point', 'destination', 'night_stay', 'meals')
    ordering = ('day_number',)
    show_change_link = True


class PackageDetailInline(StackedInline):
    model = PackageDetail
    can_delete = False
    max_num = 1


class StayAndTravelInline(StackedInline):
    model = StayAndTravel
    can_delete = False
    max_num = 1


class TravelGuideInline(StackedInline):
    model = TravelGuide
    can_delete = False
    max_num = 1


class PolicyAndFaqInline(StackedInline):
    model = PolicyAndFaq
    can_delete = False
    max_num = 1


@admin.register(TourPackage)
class TourPackageAdmin(ModelAdmin):
    list_display = (
        'name',
        'category',
        'region',
        'duration_display',
        'starting_price',
        'status_badge',
        'is_completed_badge',
        'order'
    )
    list_filter = ('category', 'status', 'is_completed', 'region')
    search_fields = ('name', 'subtitle', 'tagline', 'region', 'starting_city', 'brief_guide')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order',)
    ordering = ('order', 'name')
    inlines = [
        DhamDestinationInline,
        ItineraryDayInline,
        PackageDetailInline,
        StayAndTravelInline,
        TravelGuideInline,
        PolicyAndFaqInline
    ]

    @display(
        description="Status",
        label={
            "active": "success",
            "upcoming": "warning",
            "seasonal": "info",
            "draft": "secondary",
        },
    )
    def status_badge(self, obj):
        return obj.status, obj.get_status_display()

    @display(description="Portal Live", boolean=True)
    def is_completed_badge(self, obj):
        return obj.is_completed

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'slug',
                'category',
                'subtitle',
                'tagline',
                'region',
                'image',
                'order'
            )
        }),
        ('Duration & Pricing', {
            'fields': (
                ('duration_days', 'duration_nights', 'duration_display'),
                ('starting_price', 'price_display', 'price_note')
            )
        }),
        ('Travel Logistics & Connectivity', {
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
            'fields': (
                'accommodation_summary',
                'meals_summary',
                'transport_summary',
                'confirmation_note',
                'brief_guide'
            )
        }),
        ('Structured Content Lists', {
            'classes': ('collapse',),
            'fields': ('introduction', 'route_highlights', 'highlights')
        }),
        ('Portal & Publication Status', {
            'fields': (
                'status',
                'status_label',
                'is_completed'
            )
        }),
    )

    actions = ['mark_as_active', 'mark_as_upcoming']

    @admin.action(description="✓ Mark selected tours as Active")
    def mark_as_active(self, request, queryset):
        queryset.update(status='active', is_completed=True)
        self.message_user(request, "Selected tours marked as Active.")

    @admin.action(description="⏰ Mark selected tours as Upcoming")
    def mark_as_upcoming(self, request, queryset):
        queryset.update(status='upcoming', is_completed=False)
        self.message_user(request, "Selected tours marked as Upcoming.")


@admin.register(ItineraryDay)
class ItineraryDayAdmin(ModelAdmin):
    list_display = ('tour', 'day_badge', 'title', 'starting_point', 'destination', 'night_stay', 'meals')
    list_filter = ('tour', 'night_stay')
    search_fields = ('title', 'intro', 'starting_point', 'destination', 'night_stay', 'hotel_name')
    ordering = ('tour', 'day_number')

    @display(description="Day")
    def day_badge(self, obj):
        return f"Day {obj.day_number}"

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
        ('Detailed Content', {
            'fields': ('schedule', 'darshan_tips', 'scenic_points', 'places_covered', 'route_nodes')
        }),
    )


@admin.register(DhamDestination)
class DhamDestinationAdmin(ModelAdmin):
    list_display = ('tour', 'order', 'name', 'significance', 'highlight')
    list_filter = ('tour',)
    search_fields = ('name', 'significance', 'description')
    ordering = ('tour', 'order')


@admin.register(PackageDetail)
class PackageDetailAdmin(ModelAdmin):
    list_display = ('tour',)
    search_fields = ('tour__name',)


@admin.register(StayAndTravel)
class StayAndTravelAdmin(ModelAdmin):
    list_display = ('tour',)
    search_fields = ('tour__name',)


@admin.register(TravelGuide)
class TravelGuideAdmin(ModelAdmin):
    list_display = ('tour',)
    search_fields = ('tour__name',)


@admin.register(PolicyAndFaq)
class PolicyAndFaqAdmin(ModelAdmin):
    list_display = ('tour',)
    search_fields = ('tour__name',)
