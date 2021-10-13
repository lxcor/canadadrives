from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

from leaderboard.routers import router

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
