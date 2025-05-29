from django.urls import path

from accounts.api_endpoints import (
    SessionLoginAPIView,
    SessionLogoutAPIView,
    CartItemsListAPIView,
    CartItemsCreateAPIView,
    CartItemsUpdateAPIView,
    CartItemsDeleteAPIView,
    RequestPasswordResetView, 
    PasswordResetConfirmView,
    CheckResetTokenValidView
)

urlpatterns = [
    path('login/', SessionLoginAPIView.as_view(), name="login-session"),
    path('logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    path('cart/', CartItemsListAPIView.as_view(), name="cart-items"),
    path('cart/cartitems/create/', CartItemsCreateAPIView.as_view(), name="cart-items-create"),
    path('cart/cartitems/<int:pk>/update/', CartItemsUpdateAPIView.as_view(), name="cart-items-update"),
    path('cart/cartitems/<int:pk>/delete/', CartItemsDeleteAPIView.as_view(), name="cart-items-delete"),

    # Password Reset
    path("request-reset/", RequestPasswordResetView.as_view(), name="request-password-reset"),
    path("reset-confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path("validate-token/", CheckResetTokenValidView.as_view(), name="validate-reset-token"),
]
