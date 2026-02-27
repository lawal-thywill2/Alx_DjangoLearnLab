from django.contrib import admin

# Register your models here.
from .models import Book

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    search_fields = ('title', 'author')  # fields that can be searched
    list_filter = ('publication_year',)    # add filter sidebar

# Register model with custom admin
admin.site.register(Book, BookAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)