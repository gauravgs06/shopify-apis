import pandas as pd
import json
from datetime import date

brand = "tac" 
products_json = json.load(open(f'product-list.json', encoding="utf8"))['products']
data = dict()
data["Product ID"] = []
data["Variant ID"] = []
data["SKU"] = []
data['Title'] = []
data['image'] = []
data['handle'] = []
data['MRP'] = []
data['Created Date'] = []
for i in range(len(products_json)):
    product = products_json[i]
    data["SKU"].append(product['variants'][0]['sku'])
    data["Title"].append(product['title'])
    data["Product ID"].append(product['variants'][0]['product_id'])
    data["Variant ID"].append(product['variants'][0]['id'])
    data["handle"].append(product['handle'])
    data["Created Date"].append(product['created_at'])
    data["MRP"].append(product['variants'][0]['compare_at_price'])
    try:
        data["image"].append(product['image']['src'])
    except:
        data["image"].append('')


today = date.today().strftime("%Y-%b-%d")
pd.DataFrame(data).to_csv(f'products-{brand}-{today}.csv',index=False)
