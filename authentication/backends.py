import bcrypt
from user.models import User
from django.contrib.auth.backends import BaseBackend

class Authentication(BaseBackend):
    def authenticate(self, request, **kwargs):
        try:
            user = User.objects.get(email=request.get('email', None))
            if user:
                password = request.get('password', None)
                if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    return user
                pass
        except User.DoesNotExist:
            pass
        
        return None    
