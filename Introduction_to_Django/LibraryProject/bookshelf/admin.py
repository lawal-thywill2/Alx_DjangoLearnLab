from django.contrib import admin

# Register your models here.
from .models import Book

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')  # columns to show
    search_fields = ('title', 'author')  # fields that can be searched
    list_filter = ('published_year',)    # add filter sidebar

# Register model with custom admin
admin.site.register(Book, BookAdmin)