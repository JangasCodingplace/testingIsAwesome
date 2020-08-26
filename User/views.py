from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer


class UserRegistrationAPI(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = get_user_model()
