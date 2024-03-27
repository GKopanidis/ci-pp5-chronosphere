from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class ReplySerializer(serializers.ModelSerializer):
    """
    Serializer for the Reply model.
    """
    class Meta:
        model = Comment
        fields = ['id', 'content', 'owner', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    replies = ReplySerializer(many=True, read_only=True)
    replies_count = serializers.IntegerField(
        source='replies.count', read_only=True)
    is_main_comment = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Determine if the request user is the owner of the comment.

        Args:
            obj: The comment instance.

        Returns:
            bool: True if the request user is the owner, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Convert the comment creation time to a human-readable format.

        Args:
            obj: The comment instance.

        Returns:
            str: Human-readable creation time of the comment.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Convert the comment update time to a human-readable format.

        Args:
            obj: The comment instance.

        Returns:
            str: Human-readable update time of the comment.
        """
        return naturaltime(obj.updated_at)

    def get_is_main_comment(self, obj):
        """
        Determine if the comment is a main comment (not a reply).

        Args:
            obj: The comment instance.

        Returns:
            bool: True if the comment is a main comment, False otherwise.
        """
        return obj.parent is None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content', 'replies_count',
            'replies', 'is_main_comment',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for detailed information about a comment.
    """
    post = serializers.ReadOnlyField(source='post.id')
