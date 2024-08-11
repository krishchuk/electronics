from django.urls import path

from provider.views import ProductListAPIView

app_name = "provider"

urlpatterns = [
    path("habits/", ProductListAPIView.as_view(), name="product_list"),
]
