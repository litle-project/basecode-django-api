from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reset_password_token = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

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