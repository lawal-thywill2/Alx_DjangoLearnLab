from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # your home page
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/', views.list_books, name='list_books'),
]