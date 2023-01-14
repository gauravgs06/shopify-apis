import requests
import json
import pandas

brand = "tac"
with open("./config.json", "r") as file:
    config = json.load(file)[brand]

base_url = config['shop_url']
api_version = config['api_version']
resource_url = "orders"

params = {
    "created_at_min": "2022-11-01T00:00:00+05:30",
    "limit": 250,
    "status":"any"
}
headers = {
    "X-Shopify-Access-Token": config['api_token']
}

try:
    iter = 0
    response = requests.get(base_url + "/admin/api/" + api_version + "/" + resource_url + ".json", params=params, headers=headers)
    orders  = response.json()['orders']
    # total = response.headers['']
    next_url = None
    if response.links['next']:
        next_url = response.links['next']['url']
    while next_url:
        response = requests.get(next_url, headers=headers)
        orders += response.json()['orders']
        iter += 1
        print("completed",iter,"iterations")
        if response.links['next']:
            next_url = response.links['next']['url']
        else:
            next_url = None
except Exception as e:
    print(e)

pandas.DataFrame(orders).to_csv(f'orders-{brand}.csv',index=False)
print("Completed All")