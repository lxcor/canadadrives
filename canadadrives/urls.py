from django.urls import path, include
from rest_framework.schemas import get_schema_view

from leaderboard.routers import router

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', get_schema_view(
        title="Leaderboard Application",
        description="Canada Drives Leaderboard Application",
        version="1.0.0"
    ), name='schema'),
]
