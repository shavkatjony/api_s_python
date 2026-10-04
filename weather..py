import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "htd6hy78bder5t7ygfr6",
    "username": "shavkatjon",
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)