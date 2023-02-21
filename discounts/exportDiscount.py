import pandas
import json
import requests
import time

brand: str = "tac"
with open("./config.json", "r") as file:
    config: dict = json.load(file)[brand]

base_url: str = config['shop_url']
api_version: str = config['api_version']
resource_url: str = "price_rules/{price_rule_id}/discount_codes"
resource_url_title: str = "price_rules/{price_rule_id}"

params: dict = {
    "limit": 250
}
headers = {
    "X-Shopify-Access-Token": config['api_token']
}
price_rule_id: str = "1228234162404"
delay = 0.51
try:
    iter = 0
    response = requests.get(base_url + "/admin/api/" + api_version + "/" + resource_url.format(
        price_rule_id=price_rule_id) + ".json", params=params, headers=headers)
    discount_codes = response.json()['discount_codes']
    # total = response.headers['']
    next_url = None
    if response.links['next']:
        next_url = response.links['next']['url']
    while next_url:
        try:
            response = requests.get(next_url, headers=headers)
            if response.status_code == 200:
                discount_codes += response.json()['discount_codes']
                iter += 1
                print("completed", iter, "iterations", "| API Rate:",
                      response.headers['X-Shopify-Shop-Api-Call-Limit'])
                if response.links['next']:
                    next_url = response.links['next']['url']
                else:
                    next_url = None
            else:
                print("Status Code:", response.status_code,
                      "Error:", response.json()["errors"])
                delay += 0.1
        except KeyError as e:
            print("Error KeyError", e)
            next_url = None
        except Exception as e:
            print("Error:", e,"| Response:", response.content)
        time.sleep(delay)
except Exception as e:
    print("Error", e)

responseTitle = requests.get(base_url + "/admin/api/" + api_version + "/" + resource_url_title.format(
        price_rule_id=price_rule_id) + ".json", headers=headers)

title = responseTitle.json()['price_rule']['title']
df = pandas.DataFrame(discount_codes)
df = df[["code"]]
df.columns = ["Vouchers"]
df.to_csv(f'{title}.csv', index=False)
print("Completed All")
print("Final Delay:", delay, "sec")
