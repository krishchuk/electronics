from django.contrib import admin

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
    list_display = (
        "id",
        "name",
        "type",
        "contact",
        "supplier",
        "debt",
        "create_time",
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'type',
    )
    actions = ['knock_the_debts']

    @admin.action(description="Обнулить задолженность перед поставщиком")
    def knock_the_debts(self, request, queryset):
        queryset.update(debt=0)
