from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WordViewSet,
    VocabularyViewSet,
    RegistrationAPIView,
)

router = DefaultRouter()
router.register(r'words', WordViewSet, basename='words')
router.register(r'vocabulary', VocabularyViewSet, basename='vocabulary')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationAPIView.as_view(), name='register'),
]
