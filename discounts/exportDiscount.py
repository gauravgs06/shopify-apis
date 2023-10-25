from lib.apiClient import RequestTask, SyncAPIClient

import pandas
import requests
import time


def exportDiscounts(price_rule_id, url: str, headers=None, payload=None, params={"limit": 250}):
    RESOURCE_URL: str = "/price_rules/{price_rule_id}/discount_codes.json"
    RESOURCE_URL_TITLE: str = "/price_rules/{price_rule_id}.json"
    API_URL: str = url + RESOURCE_URL
    apiClient = SyncAPIClient.getApiClient()
    try:
        iter = 0
        final_url = API_URL.format(price_rule_id=price_rule_id)
        response = apiClient.runAdhocTask(RequestTask(
            method="GET", url=final_url, headers=headers, payload=payload, params=params, priority=1))
        discount_codes = response.json()['discount_codes']
        next_url = None
        if response.links['next']:
            next_url = response.links['next']['url']
        while next_url:
            try:
                response = apiClient.runAdhocTask(RequestTask(
                    method="GET", url=next_url, headers=headers, priority=1))
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
            except KeyError as e:
                print("Error KeyError", e)
                next_url = None
            except Exception as e:
                print("Error:", e, "| Response:", response.content)
    except Exception as e:
        print("Error", e)
    responseTitle = requests.get(url+RESOURCE_URL_TITLE.format(price_rule_id=price_rule_id), headers=headers)

    title = responseTitle.json()['price_rule']['title']
    df = pandas.DataFrame(discount_codes)
    df = df[["code"]]
    df.columns = ["Vouchers"]
    df.to_csv(f'exports/{title}.csv', index=False)
