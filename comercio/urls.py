from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComercioViewSet

router = DefaultRouter()
router.register(r'comercios', ComercioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]