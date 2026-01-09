from django.contrib import admin
from .models import Book, Borrower, Issue

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'book_id',
        'title',
        'author',
        'category',
        'total_stock',
        'available_stock',
    )


class BorrowerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'status',
    )


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'book',
        'borrower',
        'issue_date',
        'expected_return_date',
        'actual_return_date',
        'status',
        'overdue_flag',
    )
admin.site.register(Book,BookAdmin)
admin.site.register(Borrower,BorrowerAdmin)
admin.site.register(Issue,IssueAdmin)