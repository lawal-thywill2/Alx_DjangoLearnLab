from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # your home page
    path('login/', views.login_view.as_view(), name='login'),
    path('logout/', views.logout_view.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/', views.list_books, name='list_books'),
]