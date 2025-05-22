from django.urls import path

from accounts.api_endpoints import (
    SessionLoginAPIView,
    SessionLogoutAPIView,
    CartItemsListAPIView,
    CartItemsCreateAPIView
)

urlpatterns = [
    path('login/', SessionLoginAPIView.as_view(), name="login-session"),
    path('logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    path('cart/', CartItemsListAPIView.as_view(), name="cart-items"),
    path('cart/cartitems/create/', CartItemsCreateAPIView.as_view(), name="cart-items-create"),
]
