from rest_framework import serializers

from leaderboard.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'points', 'address', 'url']


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'address', 'url']
