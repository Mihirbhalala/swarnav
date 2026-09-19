from django.utils import timezone
from .models import Inquiry, TourCategory, Testimonial


def dashboard_callback(request, context):
    """
    Supplies real-time business metrics, KPI summary cards,
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
        total_tours = TourPackage.objects.count()
        active_tours = TourPackage.objects.filter(status='active').count()

        recent_inquiries = Inquiry.objects.order_by('-created_at')[:6]

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
                "conversion_rate": round((converted_inquiries / total_inquiries * 100), 1) if total_inquiries > 0 else 0,
            },
            "recent_inquiries": recent_inquiries,
        })
    except Exception:
        # Fail gracefully if tables or models are not yet migrated
        context["kpi"] = {
            "total_inquiries": 0,
            "today_inquiries": 0,
            "new_inquiries": 0,
            "action_needed": 0,
            "contacted_inquiries": 0,
            "converted_inquiries": 0,
            "total_tours": 0,
            "active_tours": 0,
            "conversion_rate": 0,
        }
        context["recent_inquiries"] = []

    return context
