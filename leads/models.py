from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CityCategory(models.Model):
    title = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    title = models.ForeignKey(CityCategory, on_delete=models.CASCADE, related_name='cities')
