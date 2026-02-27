from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book


@permission_required('bookstore.can_list', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})


@permission_required('bookstore.can_create', raise_exception=True)
def create_book(request):
    return render(request, 'bookstore/create_book.html')


@permission_required('bookstore.can_edit', raise_exception=True)
def edit_book(request):
    return render(request, 'bookstore/edit_book.html')


@permission_required('bookstore.can_delete', raise_exception=True)
def delete_book(request):
    return render(request, 'bookstore/delete_book.html')