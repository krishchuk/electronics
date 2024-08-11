from rest_framework import serializers

from provider.models import Product, Provider
from provider.validators import validate_provider


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
