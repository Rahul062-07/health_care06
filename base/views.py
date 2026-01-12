from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,'home.html')



def about(request):
    return render(request, 'about.html')



def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
    return render(request, 'contact.html')