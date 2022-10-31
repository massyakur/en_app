import django_filters
from django import forms
from .models import Product

class ProductFilter(django_filters.FilterSet):

    item_brand = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    item_operating_system = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    item_processor_type = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    item_ram = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    item_disk_type = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    item_disk_size = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    item_screen_size = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    item_rating = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    item_site_name = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple)
    # laptops = django_filters.AllValuesMultipleFilter(field_name = 'laptops__item_site_name')
    # price = django_filters.NumberFilter(field_name='item_price') 
    # category = filters.CharFilter(lookup_expr='icontains')

    o = django_filters.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('item_price', 'Price'),
            ('item_rating', 'Rating'),
        ),

        # labels do not need to retain order
        # field_labels={
        #     'username': 'User account',
        # }
    )

    class Meta:
        model = Product
        fields = {
           # 'item_site_name': ['icontains'],
        }