from django.urls import path
from .views import doctor_list, doctor_dashboard, patient_detail, complete_appointment
from  .import views


urlpatterns = [
    path('list/', doctor_list, name='doctor_list'),               # For patients
    path('dashboard/', doctor_dashboard, name='doctor_dashboard'), # For logged-in doctors
    path('appointment/<int:pk>/', patient_detail, name='patient_detail'),
    path('appointment/complete/<int:pk>/', complete_appointment, name='complete_appointment'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    

]
