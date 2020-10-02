from rest_framework.routers import DefaultRouter

from .api import UserExperienceViewSet

router = DefaultRouter()
router.register('api/experiences', UserExperienceViewSet, 'experiences')

urlpatterns = router.urls
