from rest_framework import serializers
from .models import Invite

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['id', 'url', 'inviter', 'invitee', 'content']

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['content']