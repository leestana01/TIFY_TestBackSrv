from rest_framework import generics
from .models import Party
from .serializers import PartySerializer

class Create(generics.CreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer