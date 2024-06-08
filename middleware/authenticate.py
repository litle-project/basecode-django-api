from rest_framework import status
from rest_framework.response import Response
from django.utils.deprecation import MiddlewareMixin
from jwt import ExpiredSignatureError, InvalidTokenError

class Authenticate(MiddlewareMixin):
    def process_request(self, request):
        try:
            auth_header = request.META.get('HTTP_AUTHORIZATION', None)
            
            if auth_header is None or not auth_header.startswith('Bearer '):
                return Response({
                    'code': 401,
                    'message': 'Bearer token is required',
                    'data': None
                }, status=status.HTTP_401_UNAUTHORIZED)
        
        
            return request
        except ExpiredSignatureError:
            return Response({'code': 500, 'message': "Token has expired", 'data': None}, status=status.HTTP_200_OK)
        except InvalidTokenError:
            return Response({'code': 500, 'message': "Invalid Token", 'data': None}, status=status.HTTP_200_OK)

    def process_response(self, request, response):
        # Add custom headers to the response
        response['Custom-Header'] = 'value'

        return response