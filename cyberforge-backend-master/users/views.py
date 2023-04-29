import jwt
from braces.views import CsrfExemptMixin
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import verify_jwt_token

from main import settings
from users.serializers import UserSerializer

User = get_user_model()


class LoginPageAPIView(CsrfExemptMixin, APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            raise AuthenticationFailed('Password is incorrect!')

        payload = {'id': user.id}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        response = Response({'token': token}, status=200)
        response['Authorization'] = f'Bearer {token}'

        return response


class RegisterPageAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)

            return Response(serializer.data)
        else:
            raise AuthenticationFailed('Unauthenticated!')


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = Response()
        response['Authorization'] = ''
        response.data = {
            "message": "Successfully logged out."
        }
        return response

