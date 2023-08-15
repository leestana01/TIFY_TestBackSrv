from django.db import models
# from UserApp.models import User

class Character(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    hat = models.PositiveIntegerField()
    face = models.PositiveIntegerField()
    top = models.PositiveIntegerField()
    bottom = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
