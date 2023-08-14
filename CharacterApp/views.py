from rest_framework import generics
from .models import Character
from .serializers import CharacterSerializer

class Create(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class ReadUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
