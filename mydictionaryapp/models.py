import hashlib
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# class HashKey(models.Model):
#     word = models.OneToOneField('Word', on_delete=models.CASCADE)
#     hash_key = models.CharField(max_length=64)
#
#     def generate_hash_key(self):
#         data = f"{self.word.word}{self.word.translate}"
#         hashed_data = hashlib.sha256(data.encode()).hexdigest()
#         return hashed_data


class Word(models.Model):
    word = models.CharField(max_length=50)  # unique=True ?
    translate = models.CharField(max_length=50)


# @receiver(post_save, sender=Word)
# def create_or_update_hash_key(sender, instance, created, **kwargs):
#     if created or not hasattr(instance, 'hashkey'):
#         HashKey.objects.create(word=instance, hash_key=instance.generate_hash_key())
#     else:
#         instance.hashkey.hash_key = instance.generate_hash_key()
#         instance.hashkey.save()
