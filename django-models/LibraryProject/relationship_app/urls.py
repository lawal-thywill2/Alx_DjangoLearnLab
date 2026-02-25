from django.contrib import admin
from django.urls import  path

from LibraryProject.relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('book/', views.book_list, name='book_list'),
     path('book_detail/', views.BookDetailView.as_view(), name='book_detail'),
]
