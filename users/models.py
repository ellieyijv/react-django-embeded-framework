from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Name")
    birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    gender = models.CharField(max_length=12, choices=(
        ("male", "male"), ("female", "female"), ("anonymous", "anonymous")), default="anonymous", verbose_name="Gender")
    mobile = models.CharField(max_length=11, verbose_name="Phone")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email", unique=True)
    userImg = models.ImageField(upload_to="user/profile", max_length=200, default="")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
