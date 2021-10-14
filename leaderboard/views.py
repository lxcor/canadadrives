from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from leaderboard.models import User
from leaderboard.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """
    Used to create, retrieve, delete, and list users and also to increment and decrement user points.
    """
    queryset = User.objects.all().order_by('-points')
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def increment_points(self, request, pk=None):
        """
        Used to increment user points by one.
        """
        user = self.get_object()
        user.points += 1
        user.save()

        return Response(user.json())

    @action(detail=True, methods=['post'])
    def decrement_points(self, request, pk=None):
        """
        Used to decrement user points by one.
        """
        user = self.get_object()
        user.points -= 1
        user.save()

        return Response(user.json())
