from rest_framework import routers
from .api import LeadViewSet, CityViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/cities', CityViewSet, 'cities')
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls
