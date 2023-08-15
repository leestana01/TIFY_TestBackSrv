from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'character']
        # fields = '__all__'
