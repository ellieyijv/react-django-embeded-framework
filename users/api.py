from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework import authentication
from rest_framework import mixins, viewsets

from .serializers import UserDetailSerializer
# Create your views here.
User = get_user_model()


class UserViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    authentication_classes = (authentication.SessionAuthentication, )

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []
        return []
