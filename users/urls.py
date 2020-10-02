from rest_framework.routers import DefaultRouter

from .api import UserViewset

router = DefaultRouter()
router.register('api/users', UserViewset, basename="users")

urlpatterns = router.urls
