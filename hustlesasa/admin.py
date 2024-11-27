from django.contrib import admin
from hustlesasa.models import EventCategory, EventTicket, TicketPurchase
from import_export.admin import ImportExportModelAdmin


class EventCategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ['name',]
    list_per_page = 50


class EventTicketAdmin(ImportExportModelAdmin):
    list_display = ['name', 'venue', 'price', 'start_date', 'end_date' ]
    search_fields = ['name', 'venue']
    list_filter = ['event_type',]
    list_per_page = 50


class TicketPurchaseAdmin(ImportExportModelAdmin):
    list_display = ['user', 'ticket', 'quantity', 'created_at']
    list_per_page = 50


admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(EventTicket, EventTicketAdmin)
admin.site.register(TicketPurchase, TicketPurchaseAdmin)