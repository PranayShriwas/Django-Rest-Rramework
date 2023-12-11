from .models import UserRegistration
from rest_framework import serializers

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=UserRegistration
        fields='__all__'