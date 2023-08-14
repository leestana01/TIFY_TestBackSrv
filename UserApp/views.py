from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

User = get_user_model()

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
            return Response({"detail": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class Register(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        
        if not username or not password or not email:
            return Response({"detail": "Required fields missing."}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({"detail": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        User.objects.create_user(username=username, password=password, email=email)
        
        return Response({"detail": "Registration successful!"}, status=status.HTTP_201_CREATED)