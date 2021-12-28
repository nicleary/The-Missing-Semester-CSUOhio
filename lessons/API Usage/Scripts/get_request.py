import requests
import json

headers = {
    'Authorization': 'Bearer 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',
    'Content-Type': 'application/json'
}

data = {
    'name': 'Again another cool repo 2'
}


response = requests.request('POST', 'https://api.github.com/user/repos', headers=headers, data=json.dumps(data))

print(response.json())
