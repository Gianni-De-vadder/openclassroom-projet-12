from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .permissions import CanCreateClientPermission, CanUpdateOwnClientPermission, CanUpdateOwnContractPermission, CanViewAssignedEventsPermission, CanUpdateOwnEventPermission

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [CanCreateClientPermission, CanUpdateOwnClientPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'email']

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [CanUpdateOwnContractPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__first_name', 'client__last_name', 'client__email', 'date_created', 'amount']

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [CanViewAssignedEventsPermission, CanUpdateOwnEventPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__first_name', 'client__last_name', 'client__email', 'event_date']

    def perform_create(self, serializer):
        serializer.save(support_contact=self.request.user)
