from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from provider.models import Contact, Product, Provider


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "country",
        "city",
        "street",
        "house",
    )
    search_fields = (
        'email',
    )
    list_filter = (
        'country',
        'city',
    )


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "model",
        "release_date",
    )
    search_fields = (
        'name',
        'model',
    )


@admin.register(Provider)
class AdminProvider(admin.ModelAdmin):
    list_select_related = True
    list_display = (
        "id",
        "name",
        "type",
        "contact",
        "contact__city",
        "supplier_url",
        "debt",
        "create_time",
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'type', "contact__city",
    )
    actions = ['knock_the_debts']

    @admin.action(description="Обнулить задолженность перед поставщиком")
    def knock_the_debts(self, queryset):
        queryset.update(debt=0)

    @admin.display(description="Поставщик")
    def supplier_url(self, obj):
        if obj.supplier:
            url = reverse('admin:provider_provider_change', args=(obj.supplier.id,))
            return format_html('<a href="%s">%s</a>' % (url, obj.supplier.name), url)
        return None

    @admin.display(description="Город")
    def contact__city(self, obj):
        return obj.contact.city
