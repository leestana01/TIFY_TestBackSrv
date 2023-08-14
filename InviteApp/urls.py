from django.urls import path
from .views import Create, ReadUpdateDelete, CreateResponse

urlpatterns = [
    path('', Create.as_view(), name='invite-create'),
    path('<int:pk>/', ReadUpdateDelete.as_view(), name='invite-read'),
    path('<int:pk>/respond/', CreateResponse.as_view(), name='invide-respond'),
]
