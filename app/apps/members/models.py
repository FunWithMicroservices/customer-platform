import uuid

from django.db import models
from django.conf import settings


class Car(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="cars",
        on_delete=models.CASCADE
    )
    brand = models.CharField(
        max_length=80
    )
    type = models.CharField(
        max_length=240
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"User {self.user.id} - {self.brand} {self.type}"
