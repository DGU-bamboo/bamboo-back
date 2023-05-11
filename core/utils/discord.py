import json
import requests

webhook_url = "https://discord.com/api/webhooks/1105920028223754291/uIjsa8YCizvP2SP2tfZTjlYvYKHwL4VzCZGF7bBMZs83I2rJr5F6lGY6KJ4-6rZKv28W"


def send_to_discord(webhook_url, message):
    data = {"content": message}
    headers = {
        "content_type": "application/json",
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    return response
