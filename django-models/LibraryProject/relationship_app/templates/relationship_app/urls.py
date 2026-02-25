from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # your home page
    path('login/', views.loginview.as_view(), name='login'),
    path('logout/', views.logoutview.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/', views.list_books, name='list_books'),
]