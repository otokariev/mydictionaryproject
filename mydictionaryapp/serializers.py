from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['pk', 'word', 'translate']
        extra_kwargs = {
            'word': {'validators': []},
        }

    def validate(self, data):
        word = data['word']
        translate = data['translate']

        if not word.isalpha():
            raise serializers.ValidationError({'word': 'Enter a word without numbers or symbols.'})

        if not translate.isalpha():
            raise serializers.ValidationError({'translate': 'Enter a word without numbers or symbols.'})

        return data

    def create(self, validated_data):
        word = validated_data['word']

        if Word.objects.filter(word__iexact=word).exists():
            raise serializers.ValidationError({'word': 'This word is already exist.'})

        word_instance = Word.objects.create(word=word, translate=validated_data['translate'])
        return word_instance
