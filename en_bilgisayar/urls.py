from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('laptop/', views.show_all, name='laptop'),
    path('laptop/<path:name>', views.product_detail, name='product_detail'),
]