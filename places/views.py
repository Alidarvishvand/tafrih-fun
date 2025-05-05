from rest_framework import viewsets
from places import models as modpl
from places import serializers as serpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi






class PlaceViewSet(viewsets.ModelViewSet):


    queryset = modpl.Place.objects.all()
    serializer_class = serpl.PlaceSerializer

    @swagger_auto_schema(operation_description="لیست همه مکان‌های ثبت‌شده")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="ساخت مکان جدید")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="دریافت جزئیات مکان")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="ویرایش مکان")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="حذف مکان")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




class PlaceMediaViewSet(viewsets.ModelViewSet):

    queryset = modpl.PlaceMedia.objects.all()
    serializer_class = serpl.PlaceMediaSerializer

    @swagger_auto_schema(operation_description="دریافت لیست فایل‌های مدیا برای مکان‌ها")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="آپلود مدیا برای یک مکان خاص")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="دریافت یک فایل مدیای خاص")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="ویرایش اطلاعات فایل مدیا")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="حذف فایل مدیا")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
