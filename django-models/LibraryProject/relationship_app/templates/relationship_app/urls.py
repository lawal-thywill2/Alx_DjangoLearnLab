from django.contrib import admin
from django.urls import  path

from LibraryProject.relationship_app import views
from .views import list_books, LibraryDetailView

urlpatterns = [
     path('book/', list_books, name='list_books'),
     path('library_detail/', LibraryDetailView.as_view(), name='library_detail'),
]
