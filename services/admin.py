from django.contrib import admin
from .models import Service, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'device_type', 'price', 'is_published', 'created_at')
    list_filter = ('device_type', 'is_published')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
