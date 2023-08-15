from django.urls import path
from .views import Login, Logout, UserControll

urlpatterns = [
    path('login/', Login.as_view(), name='user-login'),
    path('logout/', Logout.as_view(), name='user-logout'),
    path('', UserControll.as_view(), name='user-controll')
]