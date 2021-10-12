from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    points = models.PositiveIntegerField(null=False, blank=True, default=0)
    age = models.PositiveSmallIntegerField(null=False, blank=False)
    address = models.TextField(null=False, blank=False)
