"""
Views for the user API.
"""
from rest_framework import generics  # type: ignore

from user.serializers import UserSerializer  # type: ignore


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
