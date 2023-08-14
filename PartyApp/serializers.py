from rest_framework import serializers
from .models import Party, Seat
from CharacterApp.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    character = CharacterSerializer()  # 캐릭터 정보도 함께 직렬화

    class Meta:
        model = Seat
        fields = ('id', 'character')

class PartySerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)  # Party와 관련된 좌석 정보를 직렬화

    class Meta:
        model = Party
        fields = ('id', 'host', 'seats')
