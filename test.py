import requests


payload={"a": 10, "b":2}

response = requests.post("http://127.0.0.1:5000/minus", json=payload)
print(response.text)