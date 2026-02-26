from django.urls import path
from . import views
from . import admin_view, librarian_view, member_view

urlpatterns = [
    path('', views.home, name='home'),  # your home page
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/', views.list_books, name='list_books'),
    path('admin-dashboard/', admin_view.admin_view, name='admin-view'),
    path('librarian-dashboard/', librarian_view.librarian_view, name='librarian-view'),
    path('member-dashboard/', member_view.member_view, name='member-view'),
]