import requests

URL = "https://hndbhbcjx6.execute-api.us-east-2.amazonaws.com/hand"
headers = {"Content-Type": "application/json"}
params = {
  "draw_index": 3,
  "nums": [
    5,
    5,
    5,
    6,
    11
  ],
  "suits": [
    1,
    2,
    3,
    2,
    4
  ]
}

r =requests.request("POST", URL, params=params, headers=headers)

print(r.content)