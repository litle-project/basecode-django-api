import jwt
from decouple import config
from jwt import ExpiredSignatureError, InvalidTokenError

def user_id(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', None)
    secret_key = config('SECRET_KEY', None)
    token = auth_header.split(' ')[1]

    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])

    return decoded_token.get('id', None)