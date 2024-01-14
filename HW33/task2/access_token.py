import requests
import base64
access_token = "***"
if __name__ == "__main__":
    id_ = "***"
    secret = "***"
    basic_auth = base64.b64encode(f"{id_}:{secret}".encode()).decode()
    url='https://www.reddit.com/api/v1/access_token'
    username = "***"
    password = "***"
    headers={"Authorization": f"Basic {basic_auth}"}
    params = {"grant_type":"password", "username":username, "password":password}
    print(basic_auth)
    response = requests.post(url, headers=headers, data=params)
    print(response.status_code)
    print(response.json())
