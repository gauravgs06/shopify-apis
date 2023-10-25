# from discounts.createDiscountSet import createDiscountSet, payload_edp, payload_lipstick
from discounts.createDiscountSetGraphQL import createDiscountSet, payload_edp_graph
from discounts.createDiscountBatch import createDiscountBatch
from discounts.exportDiscount import exportDiscounts
from lib.apiClient import SyncAPIClient

# import dotenv
import json

# import threading
# dotenv.load_dotenv("./.env")

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
                                         payload_edp_graph, headers=headers, count=10, start_counter=16)

for discountSet in discountSetGenerator:
    if discountSet.status_code == 201 or discountSet.status_code == 200:
        title = discountSet.json()["data"]["priceRuleCreate"]['priceRule']['title']
        id = discountSet.json()["data"]["priceRuleCreate"]['priceRule']['legacyResourceId']
        print("Created:", title)
        print("Starting with Discount Code Import on:", title)
        createDiscountBatch(id, base_url+api_version, headers)
        print("Discount Code Creating")
        print("Starting with Code Exporting...")
        exportDiscounts(id, url=base_url + api_version,
                        headers=headers, params={"limit": 250})
    else:
        print("Error: Could not create duscount set:", json.loads(
            discountSet.request.body)["data"]["priceRuleCreate"]['priceRule']['title'])
