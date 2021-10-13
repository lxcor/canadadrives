from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view
from rest_framework.viewsets import GenericViewSet

from leaderboard.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'points', 'address', 'url']


# ViewSets define the view behavior.
class UserViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    Used to create, read, delete, and list users. Two extra actions are available under the user instance (i.e. /user/1/) to increment and decrement the user points.
    """
    queryset = User.objects.all().order_by('-points')
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def increment_points(self, request, pk=None):
        """
        Used to increment user points.
        """
        user = self.get_object()
        user.points += 1
        user.save()
        return Response({'status': 'points incremented to %s' % user.points})

    @action(detail=True, methods=['post'])
    def decrement_points(self, request, pk=None):
        """
        Used to decrement user points.
        """
        user = self.get_object()
        user.points -= 1
        user.save()
        return Response({'status': 'points decremented to %s' % user.points})


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('schema/', get_schema_view(
        title="Leaderboard Application",
        description="Canada Drives Leaderboard Application",
        version="1.0.0"
    ), name='schema'),
]
