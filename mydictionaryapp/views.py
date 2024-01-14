from rest_framework import viewsets, generics, status, serializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Word, Vocabulary
from .serializers import (
    WordSerializer,
    VocabularySerializer,
    UserSerializer
)


class VocabularyViewSet(viewsets.ModelViewSet):
    queryset = Vocabulary.objects.none()
    serializer_class = VocabularySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
