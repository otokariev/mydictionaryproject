from rest_framework import serializers
from .models import Word, Vocabulary
from django.contrib.auth.models import User


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ['pk', 'word', 'translate', 'vocabulary']

    def validate_word(self, value):
        if Word.objects.filter(word__iexact=value).exists():
            raise serializers.ValidationError("This word already exists.")
        return value


class VocabularySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vocabulary
        fields = ['pk', 'table_name']


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'confirm_password']

    extra_kwargs = {
        'password': {'write_only': True},
    }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user = User.objects.create_user(**validated_data)
        return {'id': user.id, 'username': user.username, 'password': None}
