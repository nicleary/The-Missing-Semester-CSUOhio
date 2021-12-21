import requests
import json

headers = {
    'Authorization': 'Bearer API KEY HERE',
    'Content-Type': 'application/json'
}

response = requests.request('POST', 'https://api.github.com/user/repos', headers=headers, data=json.dumps({
    'name': 'My Test Repo from Python'
}))

print(response.json())
