from rest_framework import generics
from .models import Invite
from .serializers import InviteSerializer

class Create(generics.CreateAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

class RetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

class CreateContent(generics.UpdateAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer