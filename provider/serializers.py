from rest_framework import serializers
from rest_framework.fields import CharField

from provider.models import Contact, Product, Provider


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    product_queryset = Product.objects.all()
    product = ProductSerializer(product_queryset, many=True)
    contact_data = Contact.objects.all()
    contact = ContactSerializer(contact_data)

    class Meta:
        model = Provider
        fields = "__all__"


class ProviderUpdateSerializer(serializers.ModelSerializer):
    debt = CharField(read_only=True)

    class Meta:
        model = Provider
        fields = "__all__"
