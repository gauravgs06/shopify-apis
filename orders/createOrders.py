import requests
import json
import pandas, numpy, time
from datetime import datetime

brand = "tac"
with open("./config.json", "r") as file:
    config = json.load(file)[brand]

base_url = config["shop_url"]
api_version = config["api_version"]
resource_url = "orders"

input = pandas.read_excel("Dispatch - IM (14).xlsx", sheet_name="9th Nov")
productList = pandas.read_csv("products-tac-2023-Oct-31.csv").set_index("handle")
orderTotal = 0.01

headers = {
    "X-Shopify-Access-Token": config["api_token"],
    "Content-Type": "application/json",
}
order_numbers = []
for i in range(input.shape[0]):
    try:
        row = input.iloc[[i]].reset_index()
        line_items = []
        line_total = 0
        if brand == "dev":
            line_items.append({"variant_id": 44456083915068, "quantity": 1})
        else:
            try:
                for handle in row["Product Handle"][0].split("\n"):
                    try:
                        line_items.append(
                            {
                                "variant_id": str(
                                    productList.loc[handle.strip()]["Variant ID"]
                                ),
                                "quantity": 1,
                            }
                        )
                        line_total += productList.loc[handle.strip()]["price"]
                    except Exception as e:
                        print("SKU Error:", e)
            except Exception as e:
                print("Error:", e)
        address = {
            "first_name": (row["FIRST NAME"][0]).strip(),
            "last_name": str(row["Last Name"][0]).strip()
            if str(row["Last Name"][0]) != "nan" and str(row["Last Name"][0]) != " "
            else (row["FIRST NAME"][0]).strip(),
            "address1": str(row["Address - 1"][0]).replace("\n", " ").strip(),
            "address2": (row["Address - 2"][0]).strip()
            if str(row["Address - 2"][0]) != "nan"
            else " ",
            "phone": str(row["Phone"][0]).replace(" ","").strip()[:10],
            "zip": str(row["Pincode"][0]).strip(),
            "city": (row["City"][0]).strip(),
            "province": (row["State Code"][0]).strip(),
            "country": "India",
        }
        payload = {
            "order": {
                "first_name": (row["FIRST NAME"][0]).strip(),
                "last_name": str(row["Last Name"][0]).strip()
                if str(row["Last Name"][0]) != "nan" and str(row["Last Name"][0]) != " "
                else (row["FIRST NAME"][0]).strip(),
                "line_items": line_items,
                "shipping_address": address,
                "phone": str(row["Phone"][0]).replace(" ","").strip()[:10],
                "financial_status": "paid",
                "payment_gateway_names": ["manual"],
                "discount_codes": [
                    {
                        "code": "IM100",
                        "amount": str(line_total - orderTotal),
                        "type": "fixed_amount",
                    }
                ],
                "tags": "Diwali Gift",
            }
        }

        response = requests.post(
            base_url + "/admin/api/" + api_version + "/" + resource_url + ".json",
            headers=headers,
            data=json.dumps(payload),
        )
        print(response.status_code)
        order_numbers.append(response.json()["order"]["name"])
        time.sleep(0.52)
    except Exception as e:
        print(e)
        order_numbers.append("Error")

# pandas.DataFrame(orders).to_csv(f"orders-{brand}.csv", index=False)
print("Completed All")
input["Order No"] = order_numbers
now = datetime.now().strftime("%y%m%d %H%M%S")
input.to_excel(f"Orders-Created-{now}.xlsx", index=False)
