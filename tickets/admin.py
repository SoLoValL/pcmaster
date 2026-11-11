from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'device_type', 'status', 'created_at')
    list_filter = ('status', 'device_type')
    search_fields = ('client__email', 'problem')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
