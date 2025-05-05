from django.urls import path, include
from rest_framework.routers import DefaultRouter
from places import views as viewpl


app_name = "places"


router = DefaultRouter()
router.register(r'amaken', viewpl.PlaceViewSet)
router.register(r'media', viewpl.PlaceMediaViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
