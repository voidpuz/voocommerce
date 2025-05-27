from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from products.models import Brand
from products.api_endpoints.Brand.BrandCreate.serializers import BrandCreateSerializer


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer
    permission_classes = [permissions.IsAuthenticated]