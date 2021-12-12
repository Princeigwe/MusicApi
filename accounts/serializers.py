from django.db.models import fields
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework import serializers

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        ref_name = "UserCreateSerializer"
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name',]