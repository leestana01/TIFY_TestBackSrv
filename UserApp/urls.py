from django.urls import path
from .views import Login, Logout, Register, DeleteAccount, ReadUpdate

urlpatterns = [
    path('login/', Login.as_view(), name='user-login'),
    path('logout/', Logout.as_view(), name='user-logout'),
    path('register/', Register.as_view(), name='user-register'),
    path('delete/', DeleteAccount.as_view(), name='user-delete'),
    path('profile/', ReadUpdate.as_view(), name='profile')
]