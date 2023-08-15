from django.urls import path
from .views import Create, CreateResponse, GetInviteByURL

urlpatterns = [
    path('<str:invite_url>/', GetInviteByURL.as_view(), name='invite-RUD'),
    path('<str:invite_url>/response/', CreateResponse.as_view(), name='invite-response'),
    path('party/<str:party_url>/', Create.as_view(), name='invite-create'),
]
