from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "reset_password_token",
            "deleted_at",
            "restored_at",
        )
    pass

class UserSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "reset_password_token",
            "deleted_at",
            "restored_at",
        )

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6.")
        return value
