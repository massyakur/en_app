# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GeneralItemStructure(scrapy.Item):
    # define the fields for your item here like:
    item_name = scrapy.Field()
    item_brand = scrapy.Field()
    item_model_number = scrapy.Field()
    item_operating_system = scrapy.Field()
    item_processor_type = scrapy.Field()
    item_processor_gen = scrapy.Field()

    item_ram = scrapy.Field()
    item_disk_type = scrapy.Field()
    item_disk_size = scrapy.Field()
    item_screen_size = scrapy.Field()

    item_rating = scrapy.Field()
    item_price = scrapy.Field()
    item_site_name = scrapy.Field()
    item_image_link = scrapy.Field()
    item_link = scrapy.Field()
    pass

class ItemStructure(scrapy.Item):
    #item_id = scrapy.Field()
    item_name = scrapy.Field()
    item_brand = scrapy.Field()
    item_model_number = scrapy.Field()
    item_operating_system = scrapy.Field()
    item_processor_type = scrapy.Field()
    item_processor_gen = scrapy.Field()
    item_ram = scrapy.Field()
    item_disk_type = scrapy.Field()
    item_disk_size = scrapy.Field()
    item_screen_size = scrapy.Field()

    Laptops = scrapy.Field()

    pass
   
