import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user = User.objects.get(pk=payload['id'])
                request.user = user
            except (jwt.ExpiredSignatureError, ObjectDoesNotExist):
                pass

        response = self.get_response(request)

        return response
