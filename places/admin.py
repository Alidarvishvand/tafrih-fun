from django.contrib import admin
from .models import Place, PlaceMedia


class PlaceMediaInline(admin.TabularInline):
    model = PlaceMedia
    extra = 1
    fields = ['media_type', 'file']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'province', 'subcategory', 'is_active']
    list_filter = ['province', 'subcategory', 'is_active']
    search_fields = ['name', 'description']
    inlines = [PlaceMediaInline]  


@admin.register(PlaceMedia)
class PlaceMediaAdmin(admin.ModelAdmin):
    list_display = ['place', 'media_type', 'file', 'uploaded_at']
    list_filter = ['media_type', 'place']

