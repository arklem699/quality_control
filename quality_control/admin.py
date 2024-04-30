from django.contrib import admin
from .models import BugReport, FeatureRequest


def mark_as_new(modeladmin, request, queryset):
    queryset.update(status='New')

mark_as_new.short_description = "Mark selected Bug Reports as New"


def mark_as_in_progress(modeladmin, request, queryset):
    queryset.update(status='In_progress')

mark_as_in_progress.short_description = "Mark selected Bug Reports as In Progress"


def mark_as_completed(modeladmin, request, queryset):
    queryset.update(status='Completed')

mark_as_completed.short_description = "Mark selected Bug Reports as Completed"


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    actions = [mark_as_new, mark_as_in_progress, mark_as_completed]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
        }),
        ('ReadOnly', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
        }),
        ('ReadOnly', {
            'fields': ('created_at', 'updated_at')
        }),
    )