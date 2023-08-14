from django.db import models
from UserApp.models import User
from CharacterApp.models import Character

class Party(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parties_hosted')
    participants = models.ManyToManyField(Character, related_name='parties')

    def __str__(self):
        return f"{self.host.username}에 의해 생성된 모임"