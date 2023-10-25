from discounts.exportDiscount import exportDiscounts
from lib.apiClient import SyncAPIClient
import json

# import threading

brand = "tac"
with open("./config.json", "r") as file:
    config = json.load(file)[brand]

shop_url = config["shop_url"]
base_url = shop_url + "/admin/api/"
api_version = config["api_version"]
headers = {
    "X-Shopify-Access-Token": config["api_token"],
    "Content-Type": "application/json",
}

SyncAPIClient.setTimeDelay(0.51)
priceRules = [
    1257169354980,
    1257183281380,
    1257196060900,
    1257205727460,
    1257217392868,
    1257232302308,
]
for priceRule in priceRules:
  exportDiscounts(priceRule, base_url + api_version, headers, params={"limit": 250})
