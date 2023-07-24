from rest_framework import viewsets
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from django_filters.rest_framework import FilterSet, DateFilter, NumberFilter, CharFilter


class ClientFilterSet(FilterSet):
    first_name = CharFilter(lookup_expr='icontains')
    last_name = CharFilter(lookup_expr='icontains')
    email = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email']


class ContractFilterSet(FilterSet):
    client__first_name = CharFilter(lookup_expr='icontains')
    client__last_name = CharFilter(lookup_expr='icontains')
    client__email = CharFilter(lookup_expr='icontains')
    date_created = DateFilter()
    amount = NumberFilter()

    class Meta:
        model = Contract
        fields = ['client__first_name', 'client__last_name', 'client__email', 'date_created', 'amount']


class EventFilterSet(FilterSet):
    client__first_name = CharFilter(lookup_expr='icontains')
    client__last_name = CharFilter(lookup_expr='icontains')
    client__email = CharFilter(lookup_expr='icontains')
    event_date = DateFilter()

    class Meta:
        model = Event
        fields = ['client__first_name', 'client__last_name', 'client__email', 'event_date']


