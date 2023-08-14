from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

User = get_user_model()

class ReadUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all() # User 전체 대상
    serializer_class = UserSerializer # 사용할 Serializer
    permission_classes = [IsAuthenticated] # 로그인 사용자만 이용 가능

    def get_object(self):
        return self.request.user # 현재 로그인 유저 반환
