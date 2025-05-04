from django.contrib import admin
from .models import Province, Category, SubCategory,Media

class ProvinceMediaInline(admin.TabularInline):
    model = Media
    extra = 0
    fields = ['subcategory', 'media_type', 'file']  # 👈 اضافه شد



@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [ProvinceMediaInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']  # ✅ حذف province
    list_filter = ['category']
    search_fields = ['name']



@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['media_type', 'file', 'province', 'subcategory']
    list_filter = ['media_type', 'province', 'subcategory']