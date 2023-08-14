from rest_framework import generics
from .models import Party, Character
from .serializers import PartySerializer

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Party
from .serializers import PartySerializer

class Create(generics.CreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class Read(generics.RetrieveAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

    def retrieve(self, request, *args, **kwargs):
        party = self.get_object()

        # If seats are full, add 2 more seats
        occupied_seats = party.seats.filter(character__isnull=False).count()
        if occupied_seats == party.total_seats:
            party.additional_seats += 2
            party.save()

        return super().retrieve(request, *args, **kwargs)

class Update(generics.UpdateAPIView):
    queryset = Party.objects.all()

    def update(self, request, *args, **kwargs):
        party = self.get_object()

        # Find an empty seat
        empty_seat = party.seats.filter(character__isnull=True).first()

        if not empty_seat:
            return Response({"detail": "빈 좌석이 없습니다. 오류 발생(400)"}, status=status.HTTP_400_BAD_REQUEST)

        # Assign a random character to the seat (customize this logic based on your Character model setup)
        random_character = Character.objects.order_by('?').first()
        empty_seat.character = random_character
        empty_seat.save()

        return Response({"detail": "입장에 성공하였습니다.", "seat_id": empty_seat.id}, status=status.HTTP_200_OK)
