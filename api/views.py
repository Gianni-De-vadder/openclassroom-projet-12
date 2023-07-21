from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .permissions import CanCreateClientPermission, CanUpdateOwnClientPermission, CanUpdateOwnContractPermission, CanViewAssignedEventsPermission, CanUpdateOwnEventPermission

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [CanCreateClientPermission, CanUpdateOwnClientPermission]

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [CanUpdateOwnContractPermission]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [CanViewAssignedEventsPermission, CanUpdateOwnEventPermission]

    def perform_create(self, serializer):
        serializer.save(support_contact=self.request.user)