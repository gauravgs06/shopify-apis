import json
import shopify

brand = "tac"
with open("./config.json", "r") as file:
    config = json.load(file)[brand]

shop_url = config['shop_url']
base_url = shop_url + "/admin/api/"
api_version = config['api_version']
api_token = config['api_token']

session = shopify.Session(shop_url, api_version, api_token)
shopify.ShopifyResource.activate_session(session)

