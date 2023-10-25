from lib.apiClient import RequestTask, SyncAPIClient
import copy

payload_edp_graph = {
    "query": """
      mutation priceRuleCreate($priceRule: PriceRuleInput!) {
        priceRuleCreate(priceRule: $priceRule) {
          priceRule {
            id
            title
            legacyResourceId
          }
          priceRuleUserErrors {
            code
            field
            message
          }
        }
      }
    """,
    "variables": {
        "priceRule": {
            "allocationLimit": None,
            "allocationMethod": "ACROSS",
            "combinesWith": {
                "orderDiscounts": True,
                "productDiscounts": True,
                "shippingDiscounts": False,
            },
            "customerSelection": {"forAllCustomers": True},
            "itemEntitlements": {
                "collectionIds": ["gid://shopify/Collection/414003331300"],
                "productIds": [],
                "productVariantIds": [],
                "targetAllLineItems": False,
            },
            "itemPrerequisites": {
                "collectionIds": [],
                "productIds": [],
                "productVariantIds": [],
            },
            "oncePerCustomer": False,
            "prerequisiteQuantityRange": {
                "greaterThan": 1,
                "greaterThanOrEqualTo": 1,
                "lessThan": 1,
                "lessThanOrEqualTo": 1,
            },
            "prerequisiteToEntitlementQuantityRatio": None,
            "target": "LINE_ITEM",
            "title": "GPAY Aug Fragrances - ",
            "usageLimit": 1,
            "validityPeriod": {"start": "2023-08-01T00:00:00+05:30"},
            "value": {"fixedAmountValue": "-598"},
        }
    },
}
payload_edp_graph_phone = {
    "query": """
      mutation priceRuleCreate($priceRule: PriceRuleInput!) {
        priceRuleCreate(priceRule: $priceRule) {
          priceRule {
            id
            title
            legacyResourceId
          }
          priceRuleUserErrors {
            code
            field
            message
          }
        }
      }
    """,
    "variables": {
        "priceRule": {
            "allocationLimit": None,
            "allocationMethod": "ACROSS",
            "combinesWith": {
                "orderDiscounts": True,
                "productDiscounts": True,
                "shippingDiscounts": False,
            },
            "customerSelection": {"forAllCustomers": True},
            "itemEntitlements": {
                "collectionIds": ["gid://shopify/Collection/414003331300"],
                "productIds": [],
                "productVariantIds": [],
                "targetAllLineItems": False,
            },
            "itemPrerequisites": {
                "collectionIds": [],
                "productIds": [],
                "productVariantIds": [],
            },
            "oncePerCustomer": False,
            "prerequisiteQuantityRange": {
                "greaterThan": 1,
                "greaterThanOrEqualTo": 1,
                "lessThan": 1,
                "lessThanOrEqualTo": 1,
            },
            "prerequisiteToEntitlementQuantityRatio": None,
            "target": "LINE_ITEM",
            "title": "PhonePe Aug Fragrances - ",
            "usageLimit": 1,
            "validityPeriod": {"start": "2023-08-01T00:00:00+05:30"},
            "value": {"fixedAmountValue": "-598"},
        }
    },
}
payload_lipstick_graph_phone = {
    "query": """
      mutation priceRuleCreate($priceRule: PriceRuleInput!) {
        priceRuleCreate(priceRule: $priceRule) {
          priceRule {
            id
            title
            legacyResourceId
          }
          priceRuleUserErrors {
            code
            field
            message
          }
        }
      }
    """,
    "variables": {
        "priceRule": {
            "allocationLimit": None,
            "allocationMethod": "ACROSS",
            "combinesWith": {
                "orderDiscounts": True,
                "productDiscounts": True,
                "shippingDiscounts": False,
            },
            "customerSelection": {"forAllCustomers": True},
            "itemEntitlements": {
                "collectionIds": ["gid://shopify/Collection/412710764772"],
                "productIds": [],
                "productVariantIds": [],
                "targetAllLineItems": False,
            },
            "itemPrerequisites": {
                "collectionIds": [],
                "productIds": [],
                "productVariantIds": [],
            },
            "oncePerCustomer": False,
            "prerequisiteToEntitlementQuantityRatio": None,
            "target": "LINE_ITEM",
            "title": "PhonePe Aug Lipstick - ",
            "usageLimit": 1,
            "validityPeriod": {"start": "2023-08-01T00:00:00+05:30"},
            "value": {"fixedAmountValue": "-549"},
        }
    },
}
payload_lipstick_graph_gpay = {
    "query": """
      mutation priceRuleCreate($priceRule: PriceRuleInput!) {
        priceRuleCreate(priceRule: $priceRule) {
          priceRule {
            id
            title
            legacyResourceId
          }
          priceRuleUserErrors {
            code
            field
            message
          }
        }
      }
    """,
    "variables": {
        "priceRule": {
            "allocationLimit": None,
            "allocationMethod": "ACROSS",
            "combinesWith": {
                "orderDiscounts": True,
                "productDiscounts": True,
                "shippingDiscounts": False,
            },
            "customerSelection": {"forAllCustomers": True},
            "itemEntitlements": {
                "collectionIds": ["gid://shopify/Collection/412710764772"],
                "productIds": [],
                "productVariantIds": [],
                "targetAllLineItems": False,
            },
            "itemPrerequisites": {
                "collectionIds": [],
                "productIds": [],
                "productVariantIds": [],
            },
            "oncePerCustomer": False,
            "prerequisiteToEntitlementQuantityRatio": None,
            "target": "LINE_ITEM",
            "title": "GPay Aug Lipstick 2 - ",
            "usageLimit": 1,
            "validityPeriod": {"start": "2023-08-01T00:00:00+05:30"},
            "value": {"fixedAmountValue": "-400"},
        }
    },
}

def createDiscountSet(
    baseUrl, discountPayload, headers, count: int, start_counter: int
):
    apiClient = SyncAPIClient.getApiClient()
    url = baseUrl + "/graphql.json"
    upto_counter = start_counter + count - 1
    title = discountPayload["variables"]["priceRule"]["title"]
    counter = start_counter
    while counter <= upto_counter:
        payload = copy.deepcopy(discountPayload)
        payload["variables"]["priceRule"]["title"] = title + str(counter)
        response = apiClient.runAdhocTask(
            RequestTask(method="POST", url=url, headers=headers, payload=payload)
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
