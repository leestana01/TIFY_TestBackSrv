from django.urls import path
from .views import Create, RetrieveDestroy, CreateContent

urlpatterns = [
    path('invite/', Create.as_view(), name='invite-create'),
    path('invite/<int:pk>/', RetrieveDestroy.as_view(), name='invite-detail'),
    path('invite/<int:pk>/write/', CreateContent.as_view(), name='content-create'),
]
