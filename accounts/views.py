from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import VerifyOTPSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SendOTPSerializer
from .models import OTP
from .utils import send_otp
import random
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SwaggerLoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class SendOTPView(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=SendOTPSerializer)
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            phone = serializer.validated_data['phone_number']
            User = get_user_model()
            user = User.objects.filter(phone_number=phone).first()
            if user and user.username != username:
                return Response({'error': 'Username does not match for this phone number.'}, status=400)

            code = str(random.randint(100000, 999999))
            OTP.objects.create(phone_number=phone, code=code)
            send_otp(phone, code)

            return Response({'message': 'OTP sent successfully'})
        return Response(serializer.errors, status=400)



class VerifyOTPView(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=VerifyOTPSerializer)
    def post(self, request):
        phone = request.session.get('otp_phone')  

        if not phone:
            return Response({'error': 'Phone number not found in session. Please request OTP again.'}, status=400)

        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            otp = OTP.objects.filter(phone_number=phone, code=code).last()

            if not otp:
                return Response({'error': 'Invalid or expired code'}, status=400)

            User = get_user_model()
            user, created = User.objects.get_or_create(phone_number=phone, defaults={'username': phone})
            refresh = RefreshToken.for_user(user)

            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'new_user': created
            })
        return Response(serializer.errors, status=400)







class SwaggerLoginView(APIView):

    @swagger_auto_schema(
        request_body=SwaggerLoginSerializer,
        operation_description="ورود با نام کاربری و رمز عبور - دریافت توکن JWT",
        responses={200: openapi.Response("توکن‌ها", SwaggerLoginSerializer)},
    )
    def post(self, request):
        serializer = SwaggerLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class CustomLogoutView(APIView):
    """
    خروج کاربر و ریدایرکت به Swagger
    """

    def get(self, request):
        logout(request)
        return redirect('/swagger/')