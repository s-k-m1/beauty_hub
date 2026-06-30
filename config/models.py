import uuid
from django.db import models
from django.conf import settings
# Create your models here.
class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL
    ),
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        related_name="%(class)s_deleted",
        on_delete=models.SET_NULL
    )
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        abstract = True