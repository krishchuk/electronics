from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from provider.filters import ProviderFilter
from provider.models import Product, Provider
from provider.paginators import CustomPagination
from provider.serializers import ProductSerializer, ProviderSerializer, ProviderUpdateSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class ProviderCreateAPIView(generics.CreateAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    permission_classes = [IsAuthenticated]


class ProviderListAPIView(generics.ListAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_class = ProviderFilter
    filter_backends = (DjangoFilterBackend,)


class ProviderDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    permission_classes = [IsAuthenticated]


class ProviderUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProviderUpdateSerializer
    queryset = Provider.objects.all()
    permission_classes = [IsAuthenticated]


class ProviderDeleteAPIView(generics.DestroyAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    permission_classes = [IsAuthenticated]
