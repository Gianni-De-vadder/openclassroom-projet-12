from django.urls import include, path
from rest_framework import routers
from .views import ClientViewSet, ContractViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"contracts", ContractViewSet)
router.register(r"events", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
