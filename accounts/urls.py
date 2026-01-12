from django.urls import path
from . import views

urlpatterns=[
    path('login_',views.login_,name='login_'),
    path('register',views.register,name='register'),
    path('logout_',views.logout_,name='logout_'),
    path('profile',views.profile,name='profile'),
    path('change_password',views.change_password,name='change_password'),
    path('update_profile',views.update_profile,name='update_profile')
]