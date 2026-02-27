from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book


@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/view_books.html', {'books': books})


@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    return render(request, 'relationship_app/create_book.html')


@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request):
    return render(request, 'relationship_app/edit_book.html')


@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html')