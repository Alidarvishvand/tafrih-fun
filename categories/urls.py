from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProvinceViewSet, CategoryViewSet, SubCategoryViewSet,MediaViewSet
)

router = DefaultRouter()
router.register(r'provinces', ProvinceViewSet, basename='province')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')
router.register(r'media', MediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
