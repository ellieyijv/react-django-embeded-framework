from rest_framework import viewsets, permissions

from .serializers import UserExperienceSerializer
from user_operation.models import UserExperience


class UserExperienceViewSet(viewsets.ModelViewSet):
    queryset = UserExperience.objects.all()
    permission_classes = [
        permissions.AllowAny,
        # permissions.IsAuthenticatedOrReadOnly,
    ]
    serializer_class = UserExperienceSerializer

    def get_queryset(self):
        return UserExperience.objects.filter(user=self.request.user)
