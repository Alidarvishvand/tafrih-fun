from django.urls import path
from .views import SendOTPView, VerifyOTPView,SwaggerLoginView,CustomLogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = "accounts"


urlpatterns = [
    path('swagger-login/', SwaggerLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp')
]