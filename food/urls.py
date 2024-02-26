from django.urls import path
from .views import CalculatePriceAPIView

urlpatterns = [
    path('calculate_price/', CalculatePriceAPIView.as_view(), name='calculate_price'),
]