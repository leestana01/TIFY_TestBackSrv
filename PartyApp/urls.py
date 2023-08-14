from django.urls import path
from .views import Create, Read, Update

urlpatterns = [
    path('', Create.as_view(), name='party-create'),
    path('<int:pk>/', Read.as_view(), name='party-read'),
    path('<int:pk>/join/', Update.as_view(), name='party-join'),
]
