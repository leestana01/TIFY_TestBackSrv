from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from CharacterApp.models import Character

class User(AbstractUser):
    character = models.OneToOneField(Character, null=True, blank=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)


    def __str__(self):
        return self.username