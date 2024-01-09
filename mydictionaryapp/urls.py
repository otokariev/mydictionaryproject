from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WordViewSet, RegistrationAPIView

router = DefaultRouter()
router.register(r'words', WordViewSet, basename='words')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationAPIView.as_view(), name='register'),
]
