from django.shortcuts import render
from rest_framework import viewsets
from .models import UserRegistration
from .serilier import UserSerilizer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=UserRegistration.objects.all()
    serializer_class=UserSerilizer