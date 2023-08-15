import uuid
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Invite, Response
from .serializers import InviteSerializer, ResponseSerializer

# 초대장 영역
class Create(generics.CreateAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [IsAuthenticated] # 로그인 사용자만 이용 가능

    def perform_create(self, serializer):
        random_url = str(uuid.uuid4())  # 랜덤한 URL 부여
        party_url = get_object_or_404(Invite, url=self.kwargs['party_url'])
        serializer.save(url=random_url, party_url = party_url, inviter=self.request.user)

class GetInviteByURL(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    lookup_field = 'url'
    lookup_url_kwarg = 'invite_url'

    def get_queryset(self):
        # URL에 기반하여 초대장 검색
        # url = self.kwargs.get('invite_url')
        # return Invite.objects.filter(url=url)
        return get_object_or_404(Invite, url=self.kwargs['invite_url'])
    

# 답변 영역
class CreateResponse(generics.CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def perform_create(self, serializer):
        # request에서 invite의 ID나 URL을 가져와서 해당 Invite를 찾아 연결
        # invite = get_object_or_404(Invite, id=self.request.data.get('invite_id'))
        # invite = get_object_or_404(Invite, id=self.kwargs['pk'])
        invite = get_object_or_404(Invite, url=self.kwargs['invite_url'])
        serializer.save(invite=invite, user=self.request.user)
