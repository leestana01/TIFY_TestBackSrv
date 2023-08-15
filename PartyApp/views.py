import uuid
from rest_framework import generics
from .models import Party, Seat,Character
from .serializers import PartySerializer

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Party
from .serializers import PartySerializer

class Create(generics.CreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated] # 로그인 사용자만 이용 가능

    def perform_create(self, serializer):
        host = self.request.user
        random_url = str(uuid.uuid4())  # 랜덤한 URL 부여
        party = serializer.save(host=host, url=random_url)
        Seat.objects.create(party = party, character = host.character, url=random_url)

class Read(generics.RetrieveAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

    def get_object(self):
        invite_url = self.kwargs['invite_url']
        return Party.objects.get(url=invite_url)

# 유저 참가
class Update(generics.UpdateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

    def get_object(self):
        invite_url = self.kwargs['invite_url']
        return Party.objects.get(url=invite_url)
    
    def perform_update(self, serializer):
        party = self.get_object()
        if party.total_seats >= party.seats_count:
            party.seats_count += 1
            party.save()

        # Find an empty seat
        empty_seat = party.seats.filter(character__isnull=True).first()
        if not empty_seat:
            empty_seat = Seat.objects.create(party=party, character = None)

        # Assign a random character to the seat (customize this logic based on your Character model setup)
        random_character = Character.objects.order_by('?').first()
        empty_seat.character = random_character
        empty_seat.save()

        return Response({"detail": "입장에 성공하였습니다.", "seat_id": empty_seat.id}, status=status.HTTP_200_OK)
