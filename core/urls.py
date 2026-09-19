from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-inquiry/', views.submit_inquiry, name='submit_inquiry'),
    path('inquiry-success/<int:inquiry_id>/', views.inquiry_success, name='inquiry_success'),
    path('inquiry/<int:inquiry_id>/pdf/', views.inquiry_download_pdf, name='inquiry_pdf'),
    path('export-inquiries-excel/', views.inquiry_export_excel, name='inquiry_export_excel'),
    path('admin-inquiries-report-pdf/', views.inquiry_master_pdf, name='inquiry_master_pdf'),
    # AI Assistant Endpoints
    path('api/ai/chat/', views.ai_chat_api, name='ai_chat_api'),
    path('api/ai/reset/', views.ai_reset_api, name='ai_reset_api'),
]



