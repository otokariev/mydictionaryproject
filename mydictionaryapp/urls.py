# mydictionaryapp/urls.py
from django.urls import path
from .views import words_list, add_word, delete_word

urlpatterns = [
    path('words/', words_list, name='words_list'),
    path('add_word/', add_word, name='add_word'),
    path('delete_word/<int:pk>/', delete_word, name='delete_word'),
]
