from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class UserExperience(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    description = models.TextField(default="", verbose_name="Description", help_text="Description")
    company = models.CharField(max_length=100, verbose_name="Company")
    start_date = models.DateField()
    end_date = models.DateField()
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experience"
        unique_together = ("user", "company")

    def __str__(self):
        return self.user.username
