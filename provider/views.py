from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from provider.models import Product
from provider.paginators import CustomPagination
from provider.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
