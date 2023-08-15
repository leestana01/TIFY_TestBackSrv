from django.urls import path
from .views import Create, ReadUpdateDelete

urlpatterns = [
    path('', Create.as_view(), name='character-create'),
    path('', ReadUpdateDelete.as_view() , name='character-read')
]