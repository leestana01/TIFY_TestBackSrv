from django.db import models
from UserApp.models import User
from CharacterApp.models import Character

class Party(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parties_hosted')
    participants = models.ManyToManyField(Character, through='Seat', related_name='parties')
    seats_count = models.PositiveIntegerField(default=10)
    url = models.TextField(unique=True, default="")

    @property
    def total_seats(self):
        return self.seats.count()

class Seat(models.Model):
    party = models.ForeignKey(Party, related_name="seats", on_delete=models.CASCADE)
    character = models.ForeignKey(Character, null=True, blank=True, on_delete=models.CASCADE)


# Party -> Seat -> Character 의 구조임
# 이 때, Party의 participants는 Seat을 통하여 얻은 Character를 모아서 얻음.