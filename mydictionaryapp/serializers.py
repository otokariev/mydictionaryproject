from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ['pk', 'word', 'translate']

    def validate_word(self, value):
        if Word.objects.filter(word__iexact=value).exists():
            raise serializers.ValidationError("This word already exists.")
        return value
