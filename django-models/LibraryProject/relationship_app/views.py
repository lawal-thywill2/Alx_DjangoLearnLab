from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import Book

def home(request):
    return render(request, "relationship_app/home.html")

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

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

def register_view(request):
    return render(request, 'relationship_app/register.html')

def LoginView(request):
    return render(request, 'relationship_app/login.html')

def LogoutView(request):
    return render(request, 'relationship_app/logout.html')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


# role check functions
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'admin'


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'librarian'


def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'member'


# views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')