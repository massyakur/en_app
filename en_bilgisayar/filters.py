from secrets import choice
import django_filters
from django import forms
from .models import Product

class ProductFilter(django_filters.FilterSet):
    item_brand = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)

    item_operating_system = django_filters.AllValuesFilter()
    item_processor_type = django_filters.AllValuesFilter()
    item_ram = django_filters.AllValuesFilter()
    item_disk_type = django_filters.AllValuesFilter()
    item_disk_size = django_filters.AllValuesFilter()
    item_screen_size = django_filters.AllValuesFilter()
    item_rating = django_filters.AllValuesFilter()
    item_site_name = django_filters.AllValuesFilter()

    class Meta:
        model = Product
        fields = {
           # 'item_site_name': ['icontains'],
        }