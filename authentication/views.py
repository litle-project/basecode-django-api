import jwt
from decouple import config
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timedelta
from helpers.redis_helper import store_redis, delete_redis
from helpers.user_helper import user_id
from user.models import User

class Login(APIView):
    def post(self, request):
        try:
            # validation
            serializer = LoginSerializer(data = request.data)
            if not serializer.is_valid():
                return Response({'code': 422, 'message': serializer.errors, 'data': None}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
            # logic to find user
            user = authenticate(serializer.data)
            if not user:
                return Response({'code': 400, 'message': 'Invalid email or password', 'data': None}, status=status.HTTP_400_BAD_REQUEST)

            # return token and user data
            expiration_time = datetime.utcnow() + timedelta(hours=24)
            client_ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR', '')
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            payload = {
                'id': user.id,
                'ip': client_ip,
                'source': user_agent,
                'exp': expiration_time,
            }

            token = jwt.encode(payload, config('SECRET_KEY', 'verysecret'), algorithm='HS256')

            # save token to redis
            store_redis(f"token-{user.email}", token, 0, 86400)

            return Response({
                'code': 200,
                'message': 'OK',
                'data': {
                    'email': user.email,
                    'name': user.name,
                    'token': token,
                }
            }, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'code': 500, 'message': str(error), 'data': None}, status=status.HTTP_200_OK)

class Logout(APIView):
    def get(self, request):
        try:
            user = User.objects.get(id=user_id(request))
            delete_redis(f"token-{user.email}")

            return Response({'code': 200, 'message': 'OK', 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as error:
            return Response({'code': 500, 'message': str(error), 'data': None}, status=status.HTTP_200_OK)