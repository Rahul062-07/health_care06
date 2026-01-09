from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.utils.timezone import now
from datetime import timedelta

from .models import Book
from .models import  Borrower
from .models import Issue


# ================= AUTH =================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_dashboard' if user.is_staff else 'books')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        Borrower.objects.create(user=user, name=username)

        return redirect('login')

    return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    return redirect('login')





@staff_member_required(login_url='login')
def admin_dashboard(request):
    context = {
        'total_books': Book.objects.count(),
        'available_books': Book.objects.filter(available_stock__gt=0).count(),
        'borrowed_books': Issue.objects.filter(actual_return_date__isnull=True).count(),
        'overdue_books': Issue.objects.filter(
            actual_return_date__isnull=True,
            expected_return_date__lt=now().date()
        ).count(),
        'recent_activity': Issue.objects.select_related(
            'book_id', 'borrower_id'
        ).order_by('-issue_date')[:5],
        'total_borrowers': Borrower.objects.count()
    }
    return render(request, 'admin_dashboard.html', context)


def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            book_id=request.POST['book_id'],
            title=request.POST['title'],
            author=request.POST['author'],
            category=request.POST['category'],
            total_stock=request.POST['total_stock'],
            available_stock=request.POST['total_stock']
        )
        return redirect('books')

    return render(request, 'add_book.html')


# ================= USER =================

def index(request):
    return render(request, 'base.html')


@login_required(login_url='login')
def books(request):
    return render(request, 'books.html', {
        "data": Book.objects.all()
    })


@login_required(login_url='login')
def cart_view(request):
    cart = request.session.get('cart', [])
    cart_books = Book.objects.filter(book_id__in=cart)
    return render(request, 'cart.html', {'cart_books': cart_books})


@require_POST
@login_required(login_url='login')
def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    if book_id not in cart:
        cart.append(book_id)
    request.session['cart'] = cart
    return redirect('cart')


@require_POST
@login_required(login_url='login')
def remove_from_cart(request, book_id):
    cart = request.session.get('cart', [])
    if book_id in cart:
        cart.remove(book_id)
    request.session['cart'] = cart
    return redirect('cart')


@login_required(login_url='login')
def confirm_issue(request):
    cart = request.session.get('cart', [])
    borrower = get_object_or_404(Borrower, user=request.user)

    for book_id in cart:
        book = get_object_or_404(Book, book_id=book_id)
        if book.available_stock > 0:
            Issue.objects.create(
                book_id=book,
                borrower_id=borrower,
                expected_return_date=now().date() + timedelta(days=14)
            )
            book.available_stock -= 1
            book.save()

    request.session['cart'] = []
    return redirect('books')


@login_required(login_url='login')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'data': books})
