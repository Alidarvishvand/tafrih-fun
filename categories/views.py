from rest_framework import viewsets
from yaml import serialize
from .models import Province, Category, SubCategory,Media
from categories import serializers as sercat


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = sercat.ProvinceSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = sercat.CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = sercat.SubCategorySerializer






# from .models import Media

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()  # ✅ اضافه بشه
    serializer_class = sercat.MediaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        province_id = self.request.query_params.get('province')
        subcat_id = self.request.query_params.get('subcategory')
        if province_id:
            queryset = queryset.filter(province_id=province_id)
        if subcat_id:
            queryset = queryset.filter(subcategory_id=subcat_id)
        return queryset
