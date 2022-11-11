from django.urls import path
from . import views

urlpatterns = [
    path('en_ucuz/', views.en_ucuz, name='en-ucuz-home'),
    path('en_ucuz/<path:name>', views.product_detail, name='product-detail'),
    path('refresh/', views.refresh, name='refresh'),
]