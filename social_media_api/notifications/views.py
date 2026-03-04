from django.shortcuts import render

# Create your views here.
# notifications/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user)
        serializer = self.serializer_class(notifications, many=True)
        return Response(serializer.data)