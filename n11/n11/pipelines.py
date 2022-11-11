# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itertools import product
import pymongo
from itemadapter import ItemAdapter
import json
import os.path

base_laptops_list = []
all_laptops_list = []
class main_pipeline:

    def __init__(self):
        #connecting to the mongodb
        self.conn = pymongo.MongoClient('localhost', 27017)
        #creating db
        db = self.conn['ECOM_DB']
        
        #deleting collection
        db.AllLaptopsNHTT.drop()
        db.BaseLaptopsN11.drop()

        #creating collection
        self.collection = db['AllLaptopsNHTT']


    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        global all_laptops_list
        all_laptops_list.append(dict(item))
        if(item['item_site_name'] == "n11"):
            item['item_site_name'] = "EnBilgisayar"
            all_laptops_list.append(dict(item))

        with open('AllLaptopsNHTT.json','w',encoding='utf-8') as fp:
            json.dump(all_laptops_list,fp)
        
        
        return item

        

###################################
class base_laptopsN11_pipeline:

    def __init__(self):
        #connecting to the mongodb
        self.conn = pymongo.MongoClient('localhost', 27017)

        #creating db
        db = self.conn['ECOM_DB']
        
        #deleting collection
        db.BaseLaptopsN11.drop()

        #creating collection
        self.collection = db['BaseLaptopsN11']

    def process_item(self, item, spider):
        global base_laptops_list
        if(item['item_site_name'] == "n11"):
            item['item_site_name'] = "EnBilgisayar"
            self.collection.insert_one(dict(item))
            base_laptops_list.append(dict(item))
            with open('BaseLaptopsN11.json','w',encoding='utf-8') as fp:
                json.dump(base_laptops_list,fp)

        return item    


        

