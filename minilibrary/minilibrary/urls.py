"""
URL configuration for minilibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1.views import *


urlpatterns = [
    path('', index, name='index'),

    # Auth
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),

    # Admin
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('add-book/', add_book, name='add_book'),

    # User
    path('books/', books, name='books'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
    path('confirm-issue/', confirm_issue, name='confirm_issue'),

    path('admin/', admin.site.urls),
    # path('', include('app1.urls')), 
    path('books/', book_list, name='books'),

]


