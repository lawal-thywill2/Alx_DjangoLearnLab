from django.shortcuts import render
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
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)  # automatically log them in after registering
        return redirect('home')  # change 'home' to your homepage url name

    return render(request, 'relationship_app/register.html')

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'relationship_app/login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')