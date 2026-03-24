from rest_framework import generics
from users.models import User
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer