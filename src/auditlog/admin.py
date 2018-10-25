from django.contrib import admin
from .models import LogEntry
from .mixins import LogEntryAdminMixin
from .filters import ResourceTypeFilter


class LogEntryAdmin(admin.ModelAdmin, LogEntryAdminMixin):
    list_display = ('created', 'resource_url', 'action', 'msg_short', 'user_url')
    search_fields = ('timestamp', 'object_repr', 'changes', 'actor__first_name', 'actor__last_name')
    list_filter = ('action', ResourceTypeFilter)
    readonly_fields = ('created', 'resource_url', 'action', 'user_url', 'msg', 'timestamp', 'remote_addr')
    fieldsets = (
        (None, {'fields': ('created', 'user_url', 'remote_addr', 'resource_url')}),
        ('Changes', {'fields': ('action', 'msg', )}),
    )

    def get_queryset(self, request, **kwargs):
        queryset = super().get_queryset(request, **kwargs)
        return queryset.select_related('actor', 'content_type')


admin.site.register(LogEntry, LogEntryAdmin)
