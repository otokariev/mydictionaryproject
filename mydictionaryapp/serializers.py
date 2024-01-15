from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['pk', 'word', 'translate']
        extra_kwargs = {
            'word': {'validators': []},
        }

    def create(self, validated_data):
        word = validated_data['word']

        if Word.objects.filter(word=word).exists():
            raise serializers.ValidationError({'word': 'This word is already exist.'})
