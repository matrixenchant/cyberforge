from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import RegisterPageAPIView, LoginPageAPIView, UserAPIView, LogoutAPIView

app_name = 'users'

urlpatterns = [
    path('login/', LoginPageAPIView.as_view(), name='login'),
    path('register/', RegisterPageAPIView.as_view(), name='register'),
    path('user/', UserAPIView.as_view(), name='user_view'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
