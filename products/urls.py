from django.urls import path

from products.api_endpoints import *


urlpatterns = [
    path('', ProductListAPIView.as_view(), name="product-list"),
    path('create/', ProductCreateAPIView.as_view(), name="product-create"),
    path('<str:slug>/', ProductRetrieveAPIView.as_view(), name="product-retrieve"),
    path('<str:slug>/update/', ProductUpdateAPIView.as_view(), name="product-update"),
    path('<str:slug>/delete/', ProductDeleteAPIView.as_view(), name="product-delete"),

    path('categories/', CategoryListAPIView.as_view(), name="category-list"),
    path('categories/create/', CategoryCreateAPIView.as_view(), name="category-create"),
    path('categories/<str:slug>/', CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
    path('categories/<str:slug>/update/', CategoryUpdateAPIView.as_view(), name="category-update"),
    path('categories/<str:slug>/delete/', CategoryDeleteAPIView.as_view(), name="category-delete"),
]
