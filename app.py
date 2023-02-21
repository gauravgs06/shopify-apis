from discounts.createDiscountSet import createDiscountSet, payload_edp, payload_hairmask
from discounts.createDiscountBatch import createDiscountBatch
from lib.apiClient import SyncAPIClient

import json
# import threading

brand = "tac"
with open("./config.json", "r") as file:
    config = json.load(file)[brand]

shop_url = config['shop_url']
base_url = shop_url + "/admin/api/"
api_version = config['api_version']
headers = {
    "X-Shopify-Access-Token": config['api_token'],
    'Content-Type': 'application/json',
}

SyncAPIClient.setTimeDelay(0.51)
discountSetGenerator = createDiscountSet(base_url + api_version,
                                         payload_edp, headers=headers, count=5, start_counter=6)

for discountSet in discountSetGenerator:
    if discountSet.status_code == 201 or discountSet.status_code == 200:
        title = discountSet.json()['price_rule']['title']
        id = discountSet.json()['price_rule']['id']
        print("Created:", title)
        print("Starting with Discount Code Import on:", title)
        createDiscountBatch(id, base_url+api_version, headers)
    else:
        print("Error: Could not create duscount set:", json.loads(
            discountSet.request.body)['price_rule']['title'])
