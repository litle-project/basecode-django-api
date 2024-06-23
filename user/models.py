from django.db import models
from django_softdelete.models import SoftDeleteModel

# Create your models here.
class User(SoftDeleteModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    reset_password_token = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [name, email, password]

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return False

    class Meta:
        db_table = "users"