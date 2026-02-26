from django.test import TestCase
from LibraryProject.relationship_app.admin_view import is_admin


# Create your tests here.
@user_passes_test(is_admin)