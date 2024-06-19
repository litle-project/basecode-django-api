import bcrypt
from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry 
from .models import User
from time import gmtime, strftime

@SeederRegistry.register
class UserSeeder(seeders.ModelSeeder):
    id = 'UserSeeder'
    priopity = 1
    model = User
    data = [
        {
            "name": "admin",
            "email": "admin@mail.com",
            "password": bcrypt.hashpw("123456".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            "reset_password_token": "",
            "description": "admin",
            "created_at": strftime("%Y-%m-%d %H:%M:%S", gmtime())
        },
    ]