"""
URL configuration for mydictionaryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mydictionaryapp.views import home, words_list, add_word

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('words_list/', words_list, name='words_list'),
    path('add_word/', add_word, name='add_word'),
]
