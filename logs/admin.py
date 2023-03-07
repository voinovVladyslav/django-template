from django.contrib import admin
from django.utils.safestring import mark_safe

from admin_auto_filters.filters import AutocompleteFilter

from .models import LogRecord


@admin.register(LogRecord)
class LogRecordAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'level',
        'type',
        'msg',
    )
    readonly_fields = (
        'created_at',
        'level',
        'type',
        'message',
        'trace',
    )
    list_filter = (
        'type', 'level__name',
    )
    search_fields = (
        'message',
    )
    ordering = (
        '-created_at',
    )
    date_hierarchy = "created_at"

    def msg(self, obj) -> str:
        return mark_safe(
            obj.message.replace("\n", "<br>\n")
        )
