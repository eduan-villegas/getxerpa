from rest_framework import viewsets
from .models import Keyword
from .serializers import KeywordSerializer

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer