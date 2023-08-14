from rest_framework import serializers
from .models import Party

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['id', 'host', 'participants']
