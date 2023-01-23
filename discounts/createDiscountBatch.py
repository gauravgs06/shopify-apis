import requests
import json
import time
import random
import string
BASE_API_URL = "https://kehpl.myshopify.com/admin/api/2022-07/"
base_url = "https://kehpl.myshopify.com/admin/api/2022-07/price_rules/{price_rule_id}/batch.json"
headers = {
    'X-Shopify-Access-Token': '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',
    'Content-Type': 'application/json',
}

PREFIX = "GPAY"
SUFFIX = "J"
BATCH_SIZE = 100
TOTAL_COUPONS = 1_00_000

price_rule_id = "1222505824484"

iterations = TOTAL_COUPONS//BATCH_SIZE
counter = 0
start_time = time.time()
while counter < iterations:
    coupons = [{"code": PREFIX + "".join(random.choices(
        string.ascii_uppercase + string.digits, k=8)) + SUFFIX} for _ in range(BATCH_SIZE)]
    payload = {
        "discount_codes": coupons
    }
    url = base_url.format(price_rule_id=price_rule_id)
    response = requests.post(url=url, headers=headers,
                             data=json.dumps(payload))
    if response.status_code == 201:
        url = BASE_API_URL + "/price_rules/{price_rule_id}/batch/{batch_id}.json".format(
            price_rule_id=price_rule_id, batch_id=response.json()["discount_code_creation"]["id"])
        iter = 0
        while True:
            try:
                response_batch = requests.get(url, headers=headers)
                if response_batch.status_code == 200 and response_batch.json()["discount_code_creation"]["status"] == "completed":
                    print("Created", (counter+1) *
                          BATCH_SIZE, "of", TOTAL_COUPONS)
                    counter += 1
                    break
                else:
                    print("Status Code:", response.status_code,"| Status:",response.json()["discount_code_creation"]["status"])
                time.sleep(1)
            except Exception as e:
                print("Status Code:", response.status_code,"| Error:", e)
    time.sleep(0.6)

end_time = time.time()
print("Total Time Taken:", end_time-start_time, "sec")
