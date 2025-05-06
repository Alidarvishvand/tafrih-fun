from rest_framework import viewsets, permissions
from interactions import models as intmodel
from interactions import serializers as intser
from drf_yasg.utils import swagger_auto_schema


class CommentViewSet(viewsets.ModelViewSet):
    queryset = intmodel.Comment.objects.all()
    serializer_class = intser.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        parent = serializer.validated_data.get('parent')

        # فقط ادمین اجازه پاسخ دارد
        if parent:
            if not user.is_staff:
                raise intser.ValidationError("فقط ادمین می‌تواند پاسخ دهد.")

            # فقط یک پاسخ برای هر parent مجاز است
            if parent.replies.exists():
                raise intser.ValidationError("برای این کامنت قبلاً پاسخ داده شده است.")

        serializer.save(user=user)



    @swagger_auto_schema(operation_description="لیست و ساخت کامنت برای مکان‌ها")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = intmodel.Rating.objects.all()
    serializer_class = intser.RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_description="ثبت یا مشاهده امتیاز کاربران برای مکان‌ها")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = intmodel.Favorite.objects.all()
    serializer_class = intser.FavoriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_description="افزودن یا حذف علاقه‌مندی مکان‌ها توسط کاربر")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
