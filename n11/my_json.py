import json, os

os.chdir(r"D:\YazLab\1\Project1\Django Project\en_app\n11")

with open('AllLaptopsNHTT.json') as jsondata:
    data = json.load(jsondata)
with open('BaseLaptopsN11.json') as jsondata2:
    base = json.load(jsondata2)

def find_my_key(search):
    my_keys = []
    for n in search:
        res = {key: n[key] for key in n.keys()
            & {'item_name', 'item_site_name', 'item_price', 'item_rating', 'item_link', 'item_image_link'}}
        my_keys.append(res)
    # print(json.dumps(my_keys, indent=4))
    return my_keys

for l in base:
    # try:    
    #     del l['item_id']
    # except KeyError:
    #     pass
    search = list(filter(lambda x:x["item_model_number"]==l['item_model_number'], data))
    l['laptops'] = find_my_key(search)

# print(json.dumps(base, indent=4))

with open('result.json', 'w') as fp:
    json.dump(base, fp, indent=4)

# print(search[1]['item_site_name'])
# for laptop in data:
#     if laptop['item_price'] <= 4000:
#         print(json.dumps(laptop, indent=4))
