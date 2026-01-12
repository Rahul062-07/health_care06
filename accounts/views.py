from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def login_(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        u=authenticate(username=username,password=password)
        if u:
            login(request,u)
            return redirect('home')

    return render(request,'login_.html',{'login_nav':True})


def register(request):

    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        print(firstname,lastname,email,username,password)
        u=User.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            username=username
        )
        u.set_password(password)
        u.save()
        return redirect('login_')


    return render(request,'register.html',{'login_nav':True})

@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html',{'profile_nav':True})

@login_required(login_url='login_')
    
def change_password(request):
    if request.method == 'POST':
        try:
            u=User.objects.get(username=request.user.username)
            old_pass_data=request.POST['oldpassword']
            old_pass_verified=authenticate(username=u.username,password=old_pass_data)
            if old_pass_verified:
                print('Old password is matching')
                return render(request,'change_password.html',{'oldpassword_match':True})
            else:
                return render(request,'change_password.html',{'oldpassword_notmatch':True})
        except:
                new_pass_data=request.POST['newpassword']
                u.set_password(new_pass_data)
                u.save()
                return redirect('login_')
    return render(request,'change_password.html')

def update_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.save()
        messages.success(request, "Profile updated successfully!")

        return redirect("profile")

    return render(request, "update_profile.html") 

