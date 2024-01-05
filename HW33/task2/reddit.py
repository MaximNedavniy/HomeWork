from access_token import access_token
import requests
basic_auth=access_token
headers={"Authorization": f"Bearer {basic_auth}"}
postId = "18yki30"
sort = "old"
threaded = False
url=f'http://oauth.reddit.com/comments/{postId}/'
params = {
    "sort": sort,
    "threaded": threaded
}
response = requests.get(url, headers=headers, params=params)
data=response.json()

for index, child in enumerate(data[1]["data"]["children"], 1):
    body = child["data"].get("body", "N/A")
    author = child["data"].get("author", "N/A")
    print(f'{index}) Author: "{author}" Message: "{body}"')
