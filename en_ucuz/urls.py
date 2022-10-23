from django.urls import path
from . import views

urlpatterns = [
    path('en_ucuz/', views.en_ucuz, name='en-ucuz-home'),
]