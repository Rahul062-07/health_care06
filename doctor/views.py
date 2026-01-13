from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment
from django.contrib.auth.models import User

# List all doctors for patients
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})


# Doctor dashboard
@login_required
def doctor_dashboard(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    total_patients = Appointment.objects.filter(doctor=doctor).values('patient').distinct().count()
    appointments = Appointment.objects.filter(doctor=doctor).order_by('-date')

    context = {
        'doctor': doctor,
        'total_patients': total_patients,
        'appointments': appointments
    }
    return render(request, 'doctor/dashboard.html', context)


# Patient detail for a specific appointment
@login_required
def patient_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'doctor/patient_detail.html', {'appointment': appointment})


# Mark appointment completed
@login_required
def complete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'Completed'
    appointment.save()
    return redirect('doctor_dashboard')
