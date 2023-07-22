from lib.apiClient import RequestTask, SyncAPIClient
import copy

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
        "starts_at": "2023-07-01T00:00:00+05:30",
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
        "title": "GPAY July Fragrances - ",
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
        "starts_at": "2023-03-01T00:00:00+05:30",
        "ends_at": "2023-04-11T00:00:00+05:30",
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
        "title": "GPAY Mar Lipsticks - ",
    }
}

payload_hairmask = {
    "price_rule": {
        "value_type": "fixed_amount",
        "value": "-479.0",
        "customer_selection": "all",
        "target_type": "line_item",
        "target_selection": "entitled",
        "allocation_method": "across",
        "allocation_limit": None,
        "once_per_customer": False,
        "usage_limit": 1,
        "starts_at": "2022-02-01T00:00:00+05:30",
        "ends_at": None,
        "entitled_product_ids": [
            7512506433760
        ],
        "entitled_variant_ids": [],
        "entitled_collection_ids": [],
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
        "title": "GPAY FEB Hairmask - "
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

payload_holicolor = {
    "price_rule": {
        "value_type": "fixed_amount",
        "value": "-750.0",
        "customer_selection": "all",
        "target_type": "line_item",
        "target_selection": "entitled",
        "allocation_method": "across",
        "allocation_limit": None,
        "once_per_customer": False,
        "usage_limit": 1,
        "starts_at": "2023-03-01T00:00:00+05:30",
        "ends_at": None,
        "entitled_product_ids": [
            7578254147812
        ],
        "entitled_variant_ids": [],
        "entitled_collection_ids": [],
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
        "title": "GPAY MAR COLOR - "
    }
}


def createDiscountSet(baseUrl, discountPayload, headers, count: int, start_counter: int):
    apiClient = SyncAPIClient.getApiClient()
    url = baseUrl + "/price_rules.json"
    upto_counter = start_counter + count - 1
    title = discountPayload['price_rule']['title']
    counter = start_counter
    while counter <= upto_counter:
        payload = copy.deepcopy(discountPayload)
        payload['price_rule']['title'] = title + str(counter)
        response = apiClient.runAdhocTask(
            RequestTask(
                method="POST", url=url, headers=headers, payload=payload
            )
        )
        # print("Created:", counter, "of", upto_counter)
        counter += 1
        yield response


# if __name__ == '__main__':
#     headers = {
#         'X-Shopify-Access-Token': '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',
#         'Content-Type': 'application/json',
#     }
#     BASE_URL = "https://kehpl.myshopify.com/admin/api/"
#     API_VERSION = "2023-01"
#     createDiscountSet(BASE_URL + API_VERSION, payload_edp, headers=headers, count=2, start_counter=1)
