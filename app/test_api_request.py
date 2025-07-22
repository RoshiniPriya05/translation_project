import requests

response = requests.post(
    "http://127.0.0.1:8000/translate",
    params={
        "text": "hello",
        "source_lang": "en",
        "target_lang": "fr"
    }
)

print("Status Code:", response.status_code)
print("Response:", response.json())
