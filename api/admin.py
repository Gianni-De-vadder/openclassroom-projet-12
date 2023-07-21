from django.contrib import admin

from .models import Client, Contract, EventStatus, Event


class ClientAdmin(admin.ModelAdmin):
    """Admin for the ticket"""

    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "mobile",
        "company_name",
        "date_created",
        "date_updated",
        "sales_contact",
    )


class ContractAdmin(admin.ModelAdmin):
    """Admin for the Review"""

    list_display = (
        "id",
        "sales_contact",
        "client",
        "date_created",
        "date_updated",
        "status",
        "amount",
        "payment_due",
    )


class EventAdmin(admin.ModelAdmin):
    """Admin for the Review"""

    list_display = (
        "id",
        "client",
        "date_created",
        "date_updated",
        "support_contact",
        "event_status",
        "attendees",
        "event_date",
        "notes",
    )


class EventStatusAdmin(admin.ModelAdmin):
    """Admin for the Review"""

    list_display = ("id", "name")


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventStatus, EventStatusAdmin)
