from django.utils import timezone
from django.urls import reverse
from .models import Inquiry, TourCategory, Testimonial


def dashboard_callback(request, context):
    """
    Supplies real-time business metrics, visual Tour Package cards,
    and operational shortcuts to the Unfold Admin dashboard index.
    """
    try:
        now = timezone.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

        total_inquiries = Inquiry.objects.count()
        today_inquiries = Inquiry.objects.filter(created_at__gte=today_start).count()
        new_inquiries = Inquiry.objects.filter(status='new').count()
        follow_up_inquiries = Inquiry.objects.filter(status='follow_up').count()
        contacted_inquiries = Inquiry.objects.filter(status='contacted').count()
        converted_inquiries = Inquiry.objects.filter(status='converted').count()

        # Import TourPackage lazily to prevent circular imports
        from yatras.models import TourPackage
        tours_qs = TourPackage.objects.select_related('category').prefetch_related('itinerary_days', 'dhams').order_by('category__order', 'order')
        
        tours_list = []
        for tour in tours_qs:
            tours_list.append({
                "id": tour.id,
                "name": tour.name,
                "slug": tour.slug,
                "tagline": tour.tagline or tour.subtitle,
                "region": tour.region or (tour.category.name if tour.category else ""),
                "category_name": tour.category.name if tour.category else "General Circuit",
                "category_slug": tour.category.slug if tour.category else "general",
                "duration_display": tour.duration_display or f"{tour.duration_days} Days / {tour.duration_nights} Nights",
                "starting_price": tour.starting_price or "₹--",
                "price_note": tour.price_note,
                "status": tour.status,
                "status_display": tour.get_status_display(),
                "status_label": tour.status_label,
                "is_completed": tour.is_completed,
                "image_url": tour.image_url,
                "days_count": tour.itinerary_days.count(),
                "dhams_count": tour.dhams.count(),
                "is_active": tour.is_active,
                "tour_date": tour.tour_date,
                "toggle_active_url": reverse('admin:yatras_tourpackage_toggle_active', args=[tour.id]),
                "edit_url": reverse('admin:yatras_tourpackage_change', args=[tour.id]),
                "duplicate_url": reverse('admin:yatras_tourpackage_duplicate', args=[tour.id]),
                "view_url": tour.get_absolute_url(),
            })

        total_tours = len(tours_list)
        active_tours = sum(1 for t in tours_list if t['is_active'])
        not_active_tours = sum(1 for t in tours_list if not t['is_active'])
        upcoming_tours = sum(1 for t in tours_list if t['status'] == 'upcoming')
        draft_tours = sum(1 for t in tours_list if t['status'] == 'draft')

        recent_inquiries = Inquiry.objects.order_by('-created_at')[:6]
        categories = TourCategory.objects.filter(is_active=True).order_by('order')

        # Pilgrim Reviews Data & Shareable Review Link
        total_reviews = Testimonial.objects.count()
        five_star_reviews = Testimonial.objects.filter(rating=5).count()
        recent_reviews = Testimonial.objects.order_by('-created_at')[:5]

        review_url = request.build_absolute_uri(reverse('core:pilgrim_review'))
        import urllib.parse
        share_msg = f"Namaste! Hope you had a blessed yatra with Swarnav Tour & Travels. Please take a minute to share your sacred yatra experience and blessings with us here: {review_url}"
        review_whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(share_msg)}"

        context.update({
            "kpi": {
                "total_inquiries": total_inquiries,
                "today_inquiries": today_inquiries,
                "new_inquiries": new_inquiries,
                "action_needed": new_inquiries + follow_up_inquiries,
                "contacted_inquiries": contacted_inquiries,
                "converted_inquiries": converted_inquiries,
                "total_tours": total_tours,
                "active_tours": active_tours,
                "not_active_tours": not_active_tours,
                "upcoming_tours": upcoming_tours,
                "draft_tours": draft_tours,
                "conversion_rate": round((converted_inquiries / total_inquiries * 100), 1) if total_inquiries > 0 else 0,
            },
            "reviews_data": {
                "total_reviews": total_reviews,
                "five_star_reviews": five_star_reviews,
                "recent_reviews": recent_reviews,
                "review_submit_url": review_url,
                "review_whatsapp_url": review_whatsapp_url,
            },
            "tours": tours_list,
            "categories": categories,
            "recent_inquiries": recent_inquiries,
        })
    except Exception as exc:
        context["kpi"] = {
            "total_inquiries": 0,
            "today_inquiries": 0,
            "new_inquiries": 0,
            "action_needed": 0,
            "contacted_inquiries": 0,
            "converted_inquiries": 0,
            "total_tours": 0,
            "active_tours": 0,
            "not_active_tours": 0,
            "upcoming_tours": 0,
            "draft_tours": 0,
            "conversion_rate": 0,
        }
        context["tours"] = []
        context["categories"] = []
        context["recent_inquiries"] = []

    return context
