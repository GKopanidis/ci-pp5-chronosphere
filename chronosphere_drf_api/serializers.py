from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer class for the current user, extending UserDetailsSerializer.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    is_superuser = serializers.ReadOnlyField()

    class Meta(UserDetailsSerializer.Meta):
        """
        Meta class for CurrentUserSerializer.
        """
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'is_superuser',
        )
