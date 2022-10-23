from django.contrib import admin
from .models import Product

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_name','item_brand', 'item_model_number', 'item_rating','item_price')
    search_fields = ('item_name', 'item_brand')
    list_filter = ('item_brand', 'item_operating_system', 'item_ram', 'item_disk_type', 'item_disk_size', 'item_screen_size', 'item_rating')
