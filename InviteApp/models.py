from django.db import models
from UserApp.models import User

class Invite(models.Model):
    inviter = models.ForeignKey(User, related_name='invites_sent', on_delete=models.CASCADE)
    invitee = models.ForeignKey(User, related_name='invites_received', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.TextField(unique=True, default="")
    party_url = models.TextField(null=True, default="")

    def __str__(self):
        return f"발신: {self.inviter.username} | 수신: {self.invitee.username if self.invitee else '없음'}"
    
class Response(models.Model):
    invite = models.ForeignKey(Invite, related_name='responses', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    responded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}의 답변: {self.message}"
