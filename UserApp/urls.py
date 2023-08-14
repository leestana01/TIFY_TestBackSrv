from django.urls import path
from .views import Login, ReadUpdate, Register

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('profile/', ReadUpdate.as_view(), name='profile')
]