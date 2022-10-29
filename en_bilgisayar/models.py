from enum import unique
from djongo import models


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
    item_price = models.FloatField() # models.DecimalField(max_digits=6, decimal_places=2)
    item_site_name = models.CharField(max_length=50)
    item_image_link = models.TextField()
    item_link = models.TextField()

    # def __str__(self):
    #     return self.item_model_number
    #item_disk_size_hdd = models.CharField(max_length=50)
    #date_created = 
    #date_updated = 
class All(models.Model):
    _id = models.ObjectIdField()
    item_name = models.CharField(max_length=255)
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
    item_price = models.FloatField() # models.DecimalField(max_digits=6, decimal_places=2)
    item_site_name = models.CharField(max_length=50)
    item_image_link = models.TextField()
    item_link = models.TextField()
    # item_model_number = models.ArrayReferenceField(
    #     to = Product,
    #     # db_column = 'item_model_number',
    #     # default = True,
    #     on_delete=models.CASCADE,
    # )
    def __str__(self):
        return self.item_name