from django.test import TestCase
# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse


class RoleBasedViewTests(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='pass123')

        # Set role to admin (default test role)
        self.user.userprofile.role = 'admin'
        self.user.userprofile.save()

    def test_admin_view_access(self):
        # Log in the user
        self.client.login(username='testuser', password='pass123')

        # Try to access admin view
        response = self.client.get(reverse('admin-view'))

        # Check that access is allowed
        self.assertEqual(response.status_code, 200)