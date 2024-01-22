from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=32, unique=True)
    translate = models.CharField(max_length=32)
