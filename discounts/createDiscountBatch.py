import requests
import json
import time
import random
import string
from lib.apiClient import SyncAPIClient, RequestTask


def createDiscountBatch(price_rule_id, url, headers=None, payload=None, params=None, prefix="GPAY", suffix="F", total_coupons=1_00_000):
    RESOURCE_URL: str = "/price_rules/{price_rule_id}/batch.json"
    API_URL = url + RESOURCE_URL

    PREFIX = prefix
    SUFFIX = suffix
    BATCH_SIZE = 100
    TOTAL_COUPONS = total_coupons
    COUPON_LENGTH = 8

    iterations = TOTAL_COUPONS//BATCH_SIZE
    counter = 0
    start_time = time.time()
    apiClient = SyncAPIClient.getApiClient()
    while counter < iterations:
        try:
            coupons = [{"code": PREFIX + "".join(random.choices(
                string.ascii_uppercase + string.digits, k=COUPON_LENGTH)) + SUFFIX} for _ in range(BATCH_SIZE)]
            payload = {
                "discount_codes": coupons
            }
            final_url = API_URL.format(price_rule_id=price_rule_id)
            response = apiClient.runAdhocTask(RequestTask(method="POST", url=final_url, headers=headers,
                                                          payload=payload, params=params, priority=1))
            if response.status_code == 201:
                batch_id = response.json()["discount_code_creation"]["id"]
                batch_url = url + "/price_rules/{price_rule_id}/batch/{batch_id}.json".format(
                    price_rule_id=price_rule_id, batch_id=batch_id)
                iter = 0
                while True:
                    try:
                        response_batch = apiClient.runAdhocTask(
                            RequestTask(batch_url, headers=headers, method="GET"),waitTime=2 if iter == 0 else 0.51)
                        if response_batch.status_code == 200 and response_batch.json()["discount_code_creation"]["status"] == "completed":
                            print("Created", (counter+1) *
                                  BATCH_SIZE, "of", TOTAL_COUPONS)
                            break
                        else:
                            print("Status Code:", response_batch.status_code, "| Status:",
                                  response_batch.json()["discount_code_creation"]["status"], "| API Rate: ", response_batch.headers['X-Shopify-Shop-Api-Call-Limit'])
                        iter += 1
                        # time.sleep()
                    except Exception as e:
                        print("Status Code:", response.status_code, "| Error:", e)
                counter += 1
        except Exception as e:
            print("Error:", e)
    end_time = time.time()
    print("Total Time Taken:", end_time-start_time, "sec")
