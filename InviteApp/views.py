from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Invite, Response
from .serializers import InviteSerializer, ResponseSerializer

# 초대장 영역
class Create(generics.CreateAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

class ReadUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

# 답변 영역
class CreateResponse(generics.CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def create(self, serializer):
        # request에서 invite의 ID나 URL을 가져와서 해당 Invite를 찾아 연결
        # invite = get_object_or_404(Invite, id=self.request.data.get('invite_id'))
        invite = get_object_or_404(Invite, id=self.kwargs['pk'])
        serializer.save(invite=invite, user=self.request.user)
