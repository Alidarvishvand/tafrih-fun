from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, RatingViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
