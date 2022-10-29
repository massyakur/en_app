from djongo import models
from django import forms

class Laptop(models.Model):
    _id = models.ObjectIdField()
    item_rating = models.FloatField()
    item_price = models.FloatField()
    item_site_name = models.CharField(max_length=50)
    item_image_link = models.TextField()
    item_link = models.TextField()
    # class Meta:
    #     abstract = False
    # def __str__(self):
    #     return self.name

class LaptopForm(forms.ModelForm):
    
    class Meta:
        model = Laptop
        fields = '__all__'

class Product(models.Model):
    _id = models.ObjectIdField()
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
    laptops = models.ArrayField(
        model_container = Laptop,
        model_form_class = LaptopForm,
        blank=True, null=True
    )
    objects = models.DjongoManager()
