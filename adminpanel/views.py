from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def admin_register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not full_name or not username or not password:
            messages.error(request, "All fields are required")
            return redirect('admin_register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('admin_register')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        AdminProfile.objects.create(
            user=user,
            full_name=full_name
        )

        messages.success(request, "Admin created successfully")
        return redirect('admin_login')

    return render(request, 'adminpanel/register.html')


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and hasattr(user, 'adminprofile'):
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials or not authorized")
    return render(request, 'adminpanel/login.html')

@login_required(login_url='admin_login')
def admin_dashboard(request):
    if not request.user.is_authenticated or not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')
    return render(request, 'adminpanel/dashboard.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required
def add_doctor(request):
    if not hasattr(request.user, 'adminprofile'):
        return redirect('home')

    if request.method == "POST":
        name = request.POST['name']
        specialization = request.POST['specialization']
        experience = request.POST['experience']
        image = request.FILES['image']

        Doctor.objects.create(
            name=name,
            specialization=specialization,
            experience=experience,
            image=image
        )
        return redirect('admin_dashboard')

    return render(request, 'adminpanel/add_doctor.html')



def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not hasattr(request.user, 'adminprofile'):
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return wrapper


@admin_required
def manage_testimonials(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'adminpanel/testimonials.html', {'testimonials': testimonials})


@admin_required
def add_testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        Testimonial.objects.create(
            name=name,
            message=message
        )

        return redirect('manage_testimonials')

    return render(request, 'adminpanel/add_testimonial.html')



@admin_required
def delete_testimonial(request, id):
    Testimonial.objects.get(id=id).delete()
    return redirect('manage_testimonials')


@admin_required
def toggle_testimonial(request, id):
    t = Testimonial.objects.get(id=id)
    t.is_active = not t.is_active
    t.save()
    return redirect('manage_testimonials')



@admin_required
def manage_services(request):
    services = Service.objects.all().order_by('-created_at')
    return render(request, 'adminpanel/services.html', {'services': services})


@admin_required
def add_service(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        icon = request.FILES.get('icon')

        Service.objects.create(
            title=title,
            description=description,
            icon=icon
        )
        return redirect('manage_services')

    return render(request, 'adminpanel/add_service.html')


@admin_required
def toggle_service(request, id):
    service = Service.objects.get(id=id)
    service.is_active = not service.is_active
    service.save()
    return redirect('manage_services')


@admin_required
def delete_service(request, id):
    Service.objects.get(id=id).delete()
    return redirect('manage_services')
