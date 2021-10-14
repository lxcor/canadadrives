from rest_framework import routers

from leaderboard.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)\
