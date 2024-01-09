from rest_framework import viewsets
from .models import Word
from .serializers import WordSerializer

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
