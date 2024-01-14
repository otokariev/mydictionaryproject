from django.contrib.auth.models import User
from django.db import models


class Vocabulary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.table_name


class Word(models.Model):
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    word = models.CharField(max_length=64, unique=True)
    translate = models.CharField(max_length=64)

    def __str__(self):
        return self.word
