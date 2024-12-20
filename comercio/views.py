from rest_framework import viewsets
from .models import Comercio
from .serializers import ComercioSerializer

class ComercioViewSet(viewsets.ModelViewSet):
    queryset = Comercio.objects.all()
    serializer_class = ComercioSerializer