from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from accounts.api_endpoints.Profile.PasswordReset.emailing import send_password_reset_email
from accounts.api_endpoints.Profile.PasswordReset.serializers import (
    RequestPasswordResetSerializer,
    ConfirmPasswordResetSerializer,
)
from accounts.api_endpoints.Profile.PasswordReset.tokens import verify_password_reset_token


class RequestPasswordResetView(APIView):
    @swagger_auto_schema(
        request_body=RequestPasswordResetSerializer,
    )
    def post(self, request):
        serializer = RequestPasswordResetSerializer(data=request.data, context={
            "send_email": send_password_reset_email
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password reset email sent."}, status=200)


class PasswordResetConfirmView(APIView):
    permission_classes = []
    @swagger_auto_schema(
        request_body=ConfirmPasswordResetSerializer,
    )
    def post(self, request):
        serializer = ConfirmPasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password has been reset successfully."}, status=200)


class CheckResetTokenValidView(APIView):
    permission_classes = []
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'token',
                openapi.IN_QUERY,
                description="Token to check",
                type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: openapi.Response(
                description="Token is valid",
                schema=openapi.Schema(
                    title="Token valid",
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'valid': openapi.Schema(
                            title="Valid",
                            type=openapi.TYPE_BOOLEAN
                        )
                    }
                )
            ),
            400: openapi.Response(
                description="Token is invalid",
                schema=openapi.Schema(
                    title="Token invalid",
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'valid': openapi.Schema(
                            title="Valid",
                            type=openapi.TYPE_BOOLEAN
                        )
                    }
                )
            )
        }
    )
    def get(self, request):
        token = request.query_params.get("token")
        user_id = verify_password_reset_token(token)
        if user_id:
            return Response({"valid": True})
        return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
