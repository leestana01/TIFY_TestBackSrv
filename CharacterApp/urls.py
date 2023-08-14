from django.urls import path
from .views import Create, RetrieveUpdateDestroy

urlpatterns = [
    path('character/', Create.as_view(), name='character-create'),
    path('character/<int:pk>/', RetrieveUpdateDestroy.as_view() , name='character-detail')
]