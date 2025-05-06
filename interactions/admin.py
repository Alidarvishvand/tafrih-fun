from django.contrib import admin
from interactions import models as intmodel

@admin.register(intmodel.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'place', 'is_reply', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text', 'user__username', 'place__name']

    def is_reply(self, obj):
        return bool(obj.parent)
    is_reply.boolean = True
    is_reply.short_description = "پاسخ است؟"



@admin.register(intmodel.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'place', 'value', 'created_at']
    list_filter = ['value', 'created_at']
    search_fields = ['user__username', 'place__name']
    ordering = ['-created_at']

@admin.register(intmodel.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'place', 'created_at']
