from django.urls import path
from . import views

urlpatterns = [
    path('secure-admin-portal/login/', views.admin_login, name='admin_login'),
    path('secure-admin-portal/register/', views.admin_register, name='admin_register'),
    path('secure-admin-portal/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('secure-admin-portal/add-doctor/', views.add_doctor, name='add_doctor'),
    path('secure-admin-portal/logout/', views.admin_logout, name='admin_logout'),

    path('secure-admin-portal/testimonials/', views.manage_testimonials, name='manage_testimonials'),
    path('secure-admin-portal/testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('secure-admin-portal/testimonials/delete/<int:id>/', views.delete_testimonial, name='delete_testimonial'),
    path('secure-admin-portal/testimonials/toggle/<int:id>/', views.toggle_testimonial, name='toggle_testimonial'),

    
    path('secure-admin-portal/testimonials/', views.manage_testimonials, name='manage_testimonials'),
    path('secure-admin-portal/testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('secure-admin-portal/testimonials/delete/<int:id>/', views.delete_testimonial, name='delete_testimonial'),
    path('secure-admin-portal/testimonials/toggle/<int:id>/', views.toggle_testimonial, name='toggle_testimonial'),

    path('secure-admin-portal/services/', views.manage_services, name='manage_services'),
    path('secure-admin-portal/services/add/', views.add_service, name='add_service'),
    path('secure-admin-portal/services/toggle/<int:id>/', views.toggle_service, name='toggle_service'),
    path('secure-admin-portal/services/delete/<int:id>/', views.delete_service, name='delete_service'),
]

