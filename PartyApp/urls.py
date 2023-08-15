from django.urls import path
from .views import Create, Read, Update

urlpatterns = [
    path('', Create.as_view(), name='party-create'),
    path('<str:invite_url>/', Read.as_view(), name='party-read'),
    path('<str:invite_url>/join/', Update.as_view(), name='party-join'),
]
