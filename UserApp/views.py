from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User

class ReadUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all() # User 전체 대상
    serializer_class = UserSerializer # 사용할 Serializer
    permission_classes = [IsAuthenticated] # 로그인 사용자만 이용 가능

    def get_object(self):
        return self.request.user # 현재 로그인 유저 반환

class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({"detail": "로그인 완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class Register(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            print(username)
            print(password)
            return Response({"detail": "누락된 값이 존재합니다"}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({"detail": "Username 이 이미 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        User.objects.create_user(username=username, password=password)
        
        return Response({"detail": "회원가입이 성공적으로 완료되었습니다!"}, status=status.HTTP_201_CREATED)

class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "로그아웃 완료"}, status=status.HTTP_200_OK)

class DeleteAccount(APIView):
    permission_classes = [IsAuthenticated] # 로그인 사용자만 이용 가능

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"detail": "회원탈퇴가 완료되었습니다."}, status=status.HTTP_200_OK)
