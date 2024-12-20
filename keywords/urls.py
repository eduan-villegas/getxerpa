from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeywordViewSet

router = DefaultRouter()
router.register(r'keywords', KeywordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]