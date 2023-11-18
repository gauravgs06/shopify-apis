import requests
import json
import pandas, numpy, time

brand = "tac"
with open("./config.json", "r") as file:
    config = json.load(file)[brand]

base_url = config["shop_url"]
api_version = config["api_version"]
resource_url = "orders"

# input = pandas.read_excel("Diwali Gifting - 1.xlsx")
# productList = pandas.read_csv("products-tac-2023-Oct-27.csv").set_index("handle")
with open("./orders-dump.json", "r") as file:
    orders = json.load(file)["orders"]
params = {"api_version": "2023-10"}
orderTotal = 0.01
headers = {
    "X-Shopify-Access-Token": config["api_token"],
    "Content-Type": "application/json",
}

for order in orders:
    orderId = order["id"]
    
    response = requests.put(
            base_url + "/admin/api/" + api_version + "/" + resource_url + "/"+ orderId +".json",
            headers=headers,
            data=json.dumps(payload),
        )