import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "gender", "birthday", "email", "mobile")
