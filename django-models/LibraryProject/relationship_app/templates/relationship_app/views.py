from dbm.ndbm import library

from django.shortcuts import render

# Create your views here.
from .models import Book

def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'list_books': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
  """A class-based view for displaying details of a specific library."""
  model = Library
  template_name = 'relationship_app/library_detail.html'