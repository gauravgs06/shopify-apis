import requests
import json
import time
url = "https://kehpl.myshopify.com/admin/api/2022-07/price_rules.json"
payload_edp = {
    "price_rule": {
        "value_type": "fixed_amount",
        "value": "-598.0",
        "customer_selection": "all",
        "target_type": "line_item",
        "target_selection": "entitled",
        "allocation_method": "across",
        "allocation_limit": None,
        "once_per_customer": False,
        "usage_limit": 1,
        "starts_at": "2023-01-10T00:00:00+05:30",
        "ends_at": None,
        "entitled_product_ids": [],
        "entitled_variant_ids": [],
        "entitled_collection_ids": [
          414003331300  
        ],
        "entitled_country_ids": [],
        "prerequisite_product_ids": [],
        "prerequisite_variant_ids": [],
        "prerequisite_collection_ids": [],
        "customer_segment_prerequisite_ids": [],
        "prerequisite_customer_ids": [],
        "prerequisite_subtotal_range": None,
        "prerequisite_quantity_range": None,
        "prerequisite_shipping_price_range": None,
        "prerequisite_to_entitlement_quantity_ratio": {
            "prerequisite_quantity": None,
            "entitled_quantity": None
        },
        "prerequisite_to_entitlement_purchase": {
            "prerequisite_amount": None
        },
        "title": "GPAY JAN Fragrances - ",
    }
}

payload_lipstick = {
  "price_rule": {
    "value_type": "fixed_amount",
    "value": "-599.0",
    "customer_selection": "all",
    "target_type": "line_item",
    "target_selection": "entitled",
    "allocation_method": "across",
    "allocation_limit": None,
    "once_per_customer": False,
    "usage_limit": 1,
    "starts_at": "2022-12-21T00:00:00+05:30",
    "ends_at": None,
    "entitled_product_ids": [],
    "entitled_variant_ids": [],
    "entitled_collection_ids": [
      412710764772
    ],
    "entitled_country_ids": [],
    "prerequisite_product_ids": [],
    "prerequisite_variant_ids": [],
    "prerequisite_collection_ids": [],
    "customer_segment_prerequisite_ids": [],
    "prerequisite_customer_ids": [],
    "prerequisite_subtotal_range": None,
    "prerequisite_quantity_range": None,
    "prerequisite_shipping_price_range": None,
    "prerequisite_to_entitlement_quantity_ratio": {
      "prerequisite_quantity": None,
      "entitled_quantity": None
    },
    "prerequisite_to_entitlement_purchase": {
      "prerequisite_amount": None
    },
    "title": "GPAY JAN Lipstick - "
  }
}
payload_tint = {
  "price_rule": {
    "value_type": "fixed_amount",
    "value": "-206.0",
    "customer_selection": "all",
    "target_type": "line_item",
    "target_selection": "entitled",
    "allocation_method": "across",
    "allocation_limit": None,
    "once_per_customer": False,
    "usage_limit": 1,
    "starts_at": "2023-01-01T00:00:00+05:30",
    "ends_at": None,
    "entitled_product_ids": [],
    "entitled_variant_ids": [],
    "entitled_collection_ids": [
      414096916708
    ],
    "entitled_country_ids": [],
    "prerequisite_product_ids": [],
    "prerequisite_variant_ids": [],
    "prerequisite_collection_ids": [],
    "customer_segment_prerequisite_ids": [],
    "prerequisite_customer_ids": [],
    "prerequisite_subtotal_range": None,
    "prerequisite_quantity_range": None,
    "prerequisite_shipping_price_range": None,
    "prerequisite_to_entitlement_quantity_ratio": {
      "prerequisite_quantity": None,
      "entitled_quantity": None
    },
    "prerequisite_to_entitlement_purchase": {
      "prerequisite_amount": None
    },
    "title": "GPAY JAN Tints - "
  }
}

headers = {
  'X-Shopify-Access-Token': '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',
  'Content-Type': 'application/json',
}
start_counter = 2
upto_counter = 10
payload = payload_edp
title = payload['price_rule']['title']
counter = start_counter
while counter <= upto_counter:
  payload['price_rule']['title'] = title + str(counter)
  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
  if (response.status_code == 200) or (response.status_code == 201):
    print("Created",counter,"of",upto_counter)
    counter += 1
  
  time.sleep(0.51)
