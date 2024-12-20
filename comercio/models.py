from django.db import models
from categoria.models import Categoria
import uuid

# Create your models here.
class Comercio(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    merchant_name = models.CharField(max_length=255)
    merchant_logo = models.URLField(null=True, blank=True)  # Permite NULL
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)  # Permite NULL
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.merchant_name
