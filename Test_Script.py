import requests

url = 'http://127.0.0.1:5000/company_logo'
payload = {'company_name': 'meta'}
response = requests.post(url, json=payload)

print(response.text)