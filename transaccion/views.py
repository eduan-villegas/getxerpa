from rest_framework import viewsets
from rest_framework.response import Response
from .models import Transaccion
from .serializers import TransaccionSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Calcular métricas
        total_transacciones = queryset.count()
        tasa_categorizacion = self.calcular_tasa_categorizacion(queryset)
        tasa_identificacion_comercio = self.calcular_tasa_identificacion_comercio(queryset)

        # Crear la respuesta
        return Response({
            'total_transacciones': total_transacciones,
            'tasa_categorizacion': tasa_categorizacion,
            'tasa_identificacion_comercio': tasa_identificacion_comercio,
            'transacciones': serializer.data
        })

    def calcular_tasa_categorizacion(self, queryset):
        # Calcular la tasa de categorización (ejemplo simple)
        categorizadas = queryset.filter(categoria__isnull=False).count()
        if queryset.count() > 0:
            return categorizadas / queryset.count() * 100
        return 0

    def calcular_tasa_identificacion_comercio(self, queryset):
        # Calcular la tasa de identificación de comercio (ejemplo simple)
        identificadas = queryset.filter(comercio__isnull=False).count()
        if queryset.count() > 0:
            return identificadas / queryset.count() * 100
        return 0
    
    
    
    