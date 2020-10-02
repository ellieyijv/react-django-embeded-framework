from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from user_operation.models import UserExperience


class UserExperienceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserExperience
        validators = [
            UniqueTogetherValidator(
                queryset=UserExperience.objects.all(),
                fields=("user", "company"),
                message="Duplicate company information"
            )
        ]
        fields = ('user', 'company', 'start_date', 'end_date', 'description', 'id')
