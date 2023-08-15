from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from CharacterApp.models import Character

class User(AbstractUser):
    character = models.OneToOneField(Character, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username