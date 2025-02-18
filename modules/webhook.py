import requests
import json

def send_alert_to_discord(message, webhook_url="https://discord.com/api/webhooks/1341228311216656465/FPTG_jTkduNSaaVnZaWPegAbf2nq99YgQndZXsr3w6BNf2-EW3DXpJF-HKptQEV0Jt5s"):
    """Send an alert to a Discord Webhook."""
    data = {"content": message}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code != 204:
        print(f"Failed to send alert: {response.status_code}")
    else:
        print("Alert sent to Discord successfully!")
