from django.db import models
from comercio.models import Comercio
import uuid
# Create your models here.
class Keyword(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    keyword = models.CharField(max_length=255)
    merchant = models.ForeignKey(Comercio, on_delete=models.CASCADE, null=True, blank=True)  # Permite NULL
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword