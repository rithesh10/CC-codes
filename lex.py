import json
import urllib.request
import os

def lambda_handler(event, context):
    api_key="goldapi-e9hi17mc014uji-io"  # Store this in Lambda environment variables
    url = "https://www.goldapi.io/api/XAU/INR"

    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            gold_price_inr = data.get("price")
            
            if gold_price_inr is None:
                raise ValueError("Gold price not found in API response.")

            return {
                "sessionState": {
                    "dialogAction": {"type": "Close"},
                    "intent": {
                        "name": event["sessionState"]["intent"]["name"],
                        "state": "Fulfilled"
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": f"🪙 The current gold rate is ₹{gold_price_inr:.2f} per ounce."
                    }
                ]
            }

    except Exception as e:
        return {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {
                    "name": event["sessionState"]["intent"]["name"],
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"Sorry, I couldn't retrieve the gold rate right now. Error: {str(e)}"
                }
            ]
        }