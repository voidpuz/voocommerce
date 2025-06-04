from django.urls import path

from accounts.api_endpoints import *
from accounts.template_views import *

apis = [
    path('register/', RegisterUserAPIView.as_view(), name="register"),
    path('register/confirm/', RegisterConfirmAPIView.as_view(), name="register-confirm"),
    path('login/', SessionLoginAPIView.as_view(), name="login-session"),
    path('logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    path('cart/', CartItemsListAPIView.as_view(), name="cart-items"),
    path('cart/cartitems/create/', CartItemsCreateAPIView.as_view(), name="cart-items-create"),
    path('cart/cartitems/<int:pk>/update/', CartItemsUpdateAPIView.as_view(), name="cart-items-update"),
    path('cart/cartitems/<int:pk>/delete/', CartItemsDeleteAPIView.as_view(), name="cart-items-delete"),

    # profile 
    path('profile/update/', ProfileUpdateAPIView.as_view(), name="profile-update"),
    path('profile/delete/', ProfileDeleteAPIView.as_view(), name="profile-delete"),

    path('password-reset/request/', PasswordResetRequestAPIView.as_view(), name="password-reset"),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
]

template_urls = [
    path("template/register/", RegisterView.as_view(), name="register-template"),
    path("template/login/", LoginView.as_view(), name="login-template"),
    # path("template/reset-password/", PasswordResetView.as_view(), name="reset-password-template"),
]

urlpatterns = apis + template_urls