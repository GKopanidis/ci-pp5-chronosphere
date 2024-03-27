from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        """
        Method for creating a like instance.

        Args:
            validated_data (dict): The validated data for creating the like.

        Returns:
            Like: The created like instance.

        Raises:
            serializers.ValidationError: If a duplicate like is detected.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'Duplicate'}
            )
