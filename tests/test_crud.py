import requests

url = "http://127.0.0.1:5000/standards"
payload = {"name": "test_standard1", "description": "This is the test standard 1"}
r = requests.post(url, data=payload)
print(r.text)