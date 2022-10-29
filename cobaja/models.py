# from datetime import date
from djongo import models
from django import forms

class AllProduct(models.Model):
    id = models.ObjectIdField()
    item_model_number = models.CharField(max_length=100)
    item_site_name = models.CharField(max_length=100)
    item_price = models.FloatField()
    item_rating = models.FloatField()
    item_link = models.TextField()
    item_image_link = models.TextField(blank=True, null=True)
    # class Meta:
    #     abstract = True

class AllProductForm(forms.ModelForm):
    
    class Meta:
        model = AllProduct
        fields = '__all__'

class Product(models.Model):
    _id = models.ObjectIdField()
    all_product = models.ArrayField(
        model_container = AllProduct,
        model_form_class = AllProductForm,
        blank=True, null=True
    )
    item_name = models.CharField(max_length=255, unique=True)
    item_brand = models.CharField(max_length=50)
    item_model_number = models.CharField(max_length=100)
    item_operating_system = models.CharField(max_length=50)
    item_processor_type = models.CharField(max_length=50)
    item_processor_gen = models.CharField(max_length=50, blank=True) 
    item_ram = models.CharField(max_length=50)
    item_disk_type = models.CharField(max_length=50)
    item_disk_size = models.CharField(max_length=50)
    item_screen_size = models.CharField(max_length=50)
    item_rating = models.FloatField()
    item_price = models.FloatField()
    item_site_name = models.CharField(max_length=50)
    item_image_link = models.TextField()
    item_link = models.TextField()
