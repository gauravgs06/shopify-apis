import requests
import json
import pandas

brand:str = "tac"
with open("./config.json", "r") as file:
    config:dict = json.load(file)[brand]

base_url:str = config['shop_url']
api_version:str = config['api_version']
resource_url:str = "price_rules/{price_rule_id}/discount_codes"

params: dict = {
    "limit": 250
}
headers = {
    "X-Shopify-Access-Token": config['api_token']
}
price_rule_id: str = "1222504579300"
try:
    iter = 0
    response = requests.get(base_url + "/admin/api/" + api_version + "/" + resource_url.format(price_rule_id=price_rule_id) + ".json", params=params, headers=headers)
    discount_codes  = response.json()['discount_codes']
    # total = response.headers['']
    next_url = None
    if response.links['next']:
        next_url = response.links['next']['url']
    while next_url:
        response = requests.get(next_url, headers=headers)
        discount_codes += response.json()['discount_codes']
        iter += 1
        print("completed",iter,"iterations")
        if response.links['next']:
            next_url = response.links['next']['url']
        else:
            next_url = None
except Exception as e:
    print(e)

pandas.DataFrame(discount_codes).to_csv(f'discount-{price_rule_id}-{brand}.csv',index=False)
print("Completed All")