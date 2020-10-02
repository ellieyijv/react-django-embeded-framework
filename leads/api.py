from leads.models import Lead, City, CityCategory
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, CitySerializer, CategorySerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer


class CityViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = City.objects.all()
            name = self.request.GET.get('q', None)
            if name is not None:
                queryset = queryset.filter(name__contains=name)
            return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CityCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer
