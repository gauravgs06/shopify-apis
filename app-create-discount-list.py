from discounts.createCouponsFromList import createDiscount
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
createDiscount(1250292367588, base_url+api_version, headers)