from rest_framework import routers

from leaderboard.views import UserViewSet, CreateUserView

router = routers.DefaultRouter()
router.register(r'user', CreateUserView)
router.register(r'user', UserViewSet)
