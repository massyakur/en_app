insert json, os
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.en_app
collection = db.en_bilgisayar_product

os.chdir(r"D:\YazLab\1\Project1\Django Project\en_app\n11")
with open("result.json") as f:
    data = json.load(f)
    collection.insert_many(data)

client.close()