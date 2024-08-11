from django.urls import path

from provider.views import ProductListAPIView, ProviderCreateAPIView, ProviderListAPIView, ProviderDetailAPIView, \
    ProviderUpdateAPIView, ProviderDeleteAPIView

app_name = "provider"

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="product_list"),
    path("providers/create/", ProviderCreateAPIView.as_view(), name="provider_create"),
    path("providers/", ProviderListAPIView.as_view(), name="provider_list"),
    path("providers/<int:pk>/", ProviderDetailAPIView.as_view(), name="provider_detail"),
    path("providers/<int:pk>/update/", ProviderUpdateAPIView.as_view(), name="provider_update"),
    path("providers/<int:pk>/delete/", ProviderDeleteAPIView.as_view(), name="provider_delete"),
]
