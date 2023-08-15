from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User

class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({"detail": "로그인 완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "계정이 존재하지 않음"}, status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "로그아웃 완료"}, status=status.HTTP_200_OK)


class UserControll(APIView):

    # 회원 가입 -------------------------------------
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
    
    # 회원 조회(본인 계정) -------------------------------------
    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied("로그인이 필요합니다.")
        
        user = request.user
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    # 회원 수정(본인 계정) -------------------------------------
    def put(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied("로그인이 필요합니다.")
        
        user = request.user
        user_serializer = UserSerializer(User, data=request.data)
        if not user_serializer.is_valid():
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    # 회원 삭제(본인 계정) -------------------------------------
    def delete(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied("로그인이 필요합니다.")
        
        user = request.user
        user.delete()
        return Response({"detail": "회원탈퇴가 완료되었습니다."}, status=status.HTTP_200_OK)