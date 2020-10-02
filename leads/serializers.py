from rest_framework import serializers
from leads.models import Lead, City, CityCategory


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = CityCategory
        fields = ['title', 'cities']

