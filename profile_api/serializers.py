from rest_framework import serializers
from . import models

class HelloSerializer(serializers.ModelSerializer):
    """Serializers for name field to test our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for our user profile object."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'bio', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],
            bio = validated_data['bio']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A Serializer for Profile Feed Item"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}

