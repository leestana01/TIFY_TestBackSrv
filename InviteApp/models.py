from django.db import models
from UserApp.models import User

class Invite(models.Model):
    url = models.URLField(unique=True)
    inviter = models.ForeignKey(User, related_name='invites_sent', on_delete=models.CASCADE)
    invitee = models.ForeignKey(User, related_name='invites_received', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return f"발신: {self.inviter.username} | 수신: {self.invitee.username if self.invitee else '없음'}"