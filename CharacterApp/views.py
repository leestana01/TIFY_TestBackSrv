from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Character
from .serializers import CharacterSerializer
from UserApp.models import User
class Create(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated] # 로그인 사용자만 이용 가능

    def perform_create(self, serializer):
        character = serializer.save()  # Character 인스턴스 생성

        # Character 인스턴스를 현재 로그인한 사용자의 character 필드와 연결
        user = self.request.user
        user.character = character
        user.save()

class ReadUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 본인의 Character만 조회/수정/삭제 가능
        return Character.objects.filter(owner=self.request.user)
