from django.contrib import admin

from provider.models import Contact, Product, Provider


@admin.register(Contact)
class AdminUser(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "country",
        "city",
        "street",
        "house",
    )


@admin.register(Product)
class AdminUser(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "model",
        "release_date",
    )


@admin.register(Provider)
class AdminUser(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "type",
        "contact",
        "supplier",
        "debt",
        "create_time",
    )
