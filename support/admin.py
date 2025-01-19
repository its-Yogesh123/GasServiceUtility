from django.contrib import admin
from service.models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('reference_id', 'user', 'service_type', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'service_type', 'created_at')
    search_fields = ('reference_id', 'user__username', 'description')
    ordering = ('-created_at',)
