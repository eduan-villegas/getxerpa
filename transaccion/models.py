from django.db import models
import uuid

class Transaccion(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Permite NULL
    date = models.DateTimeField(null=True, blank=True)  # Permite NULL
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
