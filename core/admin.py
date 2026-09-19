import re
import urllib.parse
from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display, action
from unfold.enums import ActionVariant

from .models import TourCategory, WhyChooseUs, Inquiry, Testimonial

# -----------------------------------------------------------------------------
# Django Admin Site Branding
# -----------------------------------------------------------------------------
admin.site.site_header = "Swarnav Administration"
admin.site.site_title = "Swarnav Admin"
admin.site.index_title = "Inquiry Management"


@admin.register(TourCategory)
class TourCategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'badge_pill', 'order', 'is_active_badge', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'tagline', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order',)
    ordering = ('order', 'name')

    @display(description="Active", boolean=True)
    def is_active_badge(self, obj):
        return obj.is_active

    @display(description="Regional Badge")
    def badge_pill(self, obj):
        if not obj.badge:
            return "—"
        return format_html(
            '<span class="text-xs font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">{}</span>',
            obj.badge
        )


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(ModelAdmin):
    list_display = ('icon_display', 'title', 'order', 'is_active_badge')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)

    @display(description="Icon")
    def icon_display(self, obj):
        return format_html('<span class="text-xl">{}</span>', obj.icon)

    @display(description="Active", boolean=True)
    def is_active_badge(self, obj):
        return obj.is_active


@admin.register(Inquiry)
class InquiryAdmin(ModelAdmin):
    """
    Modern Unfold administration interface for managing customer pilgrimage inquiries.
    """
    list_display = (
        'id_badge',
        'created_at',
        'name',
        'phone',
        'tour_badge',
        'departure_city',
        'total_pilgrims',
        'status_badge',
        'quick_actions',
    )
    list_filter = (
        'status',
        'tour',
        'created_at',
    )
    search_fields = (
        'name',
        'phone',
        'departure_city',
        'message',
    )
    readonly_fields = ('created_at', 'updated_at', 'admin_whatsapp_link', 'admin_pdf_link')
    ordering = ['-created_at']
    date_hierarchy = 'created_at'

    @display(description="Ref #")
    def id_badge(self, obj):
        return f"#SW-{obj.id:04d}"

    @display(description="Pilgrimage Tour")
    def tour_badge(self, obj):
        return obj.get_tour_display()

    @display(
        description="Status",
        label={
            "new": "warning",
            "contacted": "info",
            "follow_up": "primary",
            "converted": "success",
            "closed": "secondary",
            "spam": "danger",
        },
    )
    def status_badge(self, obj):
        return obj.status, obj.get_status_display()

    @display(description="Quick Actions")
    def quick_actions(self, obj):
        from django.urls import reverse
        pdf_url = reverse('core:inquiry_pdf', args=[obj.id])
        digits = re.sub(r'\D', '', str(obj.phone))
        if len(digits) == 10:
            digits = f"91{digits}"
        greeting = f"Namaste {obj.name}, this is Swarnav Tour & Travels regarding your {obj.get_tour_display()} inquiry (#SW-INQ-{obj.id:04d})."
        wa_url = f"https://wa.me/{digits}?text={urllib.parse.quote(greeting)}"

        return format_html(
            '<div class="flex items-center gap-1.5">'
            '<a href="{}" target="_blank" title="Download / Print PDF Slip" class="inline-flex items-center gap-1 bg-amber-500/15 hover:bg-amber-500/25 text-amber-600 dark:text-amber-400 border border-amber-500/30 px-2 py-1 rounded text-xs font-bold transition">'
            '<span class="material-symbols-outlined text-xs">picture_as_pdf</span> PDF</a>'
            '<a href="{}" target="_blank" title="WhatsApp Chat" class="inline-flex items-center gap-1 bg-emerald-500/15 hover:bg-emerald-500/25 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30 px-2 py-1 rounded text-xs font-bold transition">'
            '<span class="material-symbols-outlined text-xs">chat</span> WA</a>'
            '</div>',
            pdf_url,
            wa_url
        )

    fieldsets = (
        ('Customer Identification', {
            'fields': (
                'name',
                'phone',
                'admin_whatsapp_link',
                'admin_pdf_link',
                'departure_city',
                'consent_given',
            ),
            'description': 'Customer contact details, direct WhatsApp initiation, and official PDF voucher.'
        }),
        ('Pilgrimage & Group Details', {
            'fields': (
                'tour',
                'total_pilgrims',
                'message',
            ),
            'description': 'Selected circuit package, requested headcount, and custom preferences.'
        }),
        ('Lead Status & Internal Notes', {
            'fields': (
                'status',
                'admin_notes',
                'created_at',
                'updated_at',
            ),
            'description': 'Operational workflow stage and internal coordinator remarks.'
        }),
    )

    actions = [
        'export_selected_to_excel',
        'mark_as_contacted',
        'mark_for_follow_up',
        'mark_as_converted',
        'mark_as_closed',
        'mark_as_spam',
    ]

    @admin.action(description="📥 Export selected inquiries to Excel (.csv)")
    def export_selected_to_excel(self, request, queryset):
        from .export_utils import export_inquiries_to_excel_response
        return export_inquiries_to_excel_response(queryset, filename_prefix="swarnav_selected_inquiries")

    @admin.action(description="✓ Mark selected inquiries as Contacted")
    def mark_as_contacted(self, request, queryset):
        count = queryset.update(status='contacted')
        self.message_user(request, f"{count} inquiry/inquiries marked as Contacted.")

    @admin.action(description="⏰ Mark selected inquiries for Follow-up")
    def mark_for_follow_up(self, request, queryset):
        count = queryset.update(status='follow_up')
        self.message_user(request, f"{count} inquiry/inquiries marked for Follow-up.")

    @admin.action(description="★ Mark selected inquiries as Converted")
    def mark_as_converted(self, request, queryset):
        count = queryset.update(status='converted')
        self.message_user(request, f"{count} inquiry/inquiries marked as Converted.")

    @admin.action(description="✕ Mark selected inquiries as Closed")
    def mark_as_closed(self, request, queryset):
        count = queryset.update(status='closed')
        self.message_user(request, f"{count} inquiry/inquiries marked as Closed.")

    @admin.action(description="🚫 Mark selected inquiries as Spam")
    def mark_as_spam(self, request, queryset):
        count = queryset.update(status='spam')
        self.message_user(request, f"{count} inquiry/inquiries marked as Spam.")

    @display(description="Printable PDF Slip")
    def admin_pdf_link(self, obj):
        """Link to open/print the official PDF summary voucher."""
        if not obj or not obj.id:
            return "—"
        from django.urls import reverse
        pdf_url = reverse('core:inquiry_pdf', args=[obj.id])
        return format_html(
            '<a href="{}" target="_blank" class="inline-flex items-center gap-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-4 py-2 rounded-xl text-xs shadow transition">'
            '<span class="material-symbols-outlined text-sm">picture_as_pdf</span> View / Print Official PDF Slip'
            '</a>',
            pdf_url
        )

    @display(description="Direct WhatsApp Contact")
    def admin_whatsapp_link(self, obj):
        """Safe WhatsApp contact link for administrators to quickly open a chat with the customer."""
        if not obj or not obj.phone:
            return "—"
        digits = re.sub(r'\D', '', str(obj.phone))
        if len(digits) == 10:
            digits = f"91{digits}"
        greeting = f"Namaste {obj.name}, this is Swarnav Tour & Travels regarding your {obj.get_tour_display()} inquiry (Ref #{obj.id:04d})."
        encoded = urllib.parse.quote(greeting)
        url = f"https://wa.me/{digits}?text={encoded}"
        return format_html(
            '<a href="{}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-4 py-2 rounded-xl text-xs shadow transition">'
            '<span class="material-symbols-outlined text-sm">chat</span> Open WhatsApp with Customer ({})'
            '</a>',
            url,
            obj.phone
        )


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('pilgrim_name', 'city', 'yatra_name', 'rating_stars', 'featured_badge', 'created_at')
    list_filter = ('rating', 'is_featured', 'yatra_name')
    search_fields = ('pilgrim_name', 'city', 'review_text')
    ordering = ('-created_at',)

    @display(description="Rating")
    def rating_stars(self, obj):
        stars = "★" * obj.rating + "☆" * (5 - obj.rating)
        return format_html('<span class="text-amber-500 font-bold text-sm tracking-wider">{}</span>', stars)

    @display(description="Featured", boolean=True)
    def featured_badge(self, obj):
        return obj.is_featured
