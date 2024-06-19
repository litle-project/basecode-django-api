import jwt
from decouple import config
from rest_framework import status
from django.utils.deprecation import MiddlewareMixin
from jwt import ExpiredSignatureError, InvalidTokenError
from django.http import JsonResponse

class Authenticate(MiddlewareMixin):
    def process_request(self, request):
        try:
            auth_header = request.META.get('HTTP_AUTHORIZATION', None)

            excludes = [
                '/api/v1/authentication/login'
            ]

            if (request.get_full_path() in excludes):
                return None

            if auth_header is None or not auth_header.startswith('Bearer '):
                return JsonResponse({
                    'code': 401,
                    'message': 'Bearer token is required',
                    'data': None
                }, status=status.HTTP_401_UNAUTHORIZED)
        
            secret_key = config('SECRET_KEY', None)
            token = auth_header.split(' ')[1]
            jwt.decode(token, secret_key, algorithms=["HS256"])
        
            return None
        except ExpiredSignatureError:
            return JsonResponse({'code': 401, 'message': "Token has expired", 'data': None}, status=status.HTTP_401_UNAUTHORIZED)
        except InvalidTokenError:
            return JsonResponse({'code': 400, 'message': "Invalid Token", 'data': None}, status=status.HTTP_400_BAD_REQUEST)