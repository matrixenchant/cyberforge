from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import RegisterPageAPIView, UserAPIView

app_name = 'users'

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', RegisterPageAPIView.as_view(), name='register'),
    path('user/', UserAPIView.as_view(), name='user_view'),
    # path('logout/', LogoutAPIView.as_view(), name='logout'),
]
