import requests
import json

headers = {
    'Authorization': 'Bearer API KEY HERE',
    'Content-Type': 'application/json'
}

response = requests.request('GET', 'https://api.github.com/user/repos', headers=headers)

print(response.json())
