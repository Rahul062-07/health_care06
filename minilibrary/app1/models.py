from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    total_stock = models.IntegerField()
    available_stock = models.IntegerField()

    def __str__(self):
        return self.title


class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=40, default='Issued')
    overdue_flag = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} - {self.borrower.name}"
