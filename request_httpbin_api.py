import requests

payload = {'username': 'yamach', 'password': 'chuqur'}
r = requests.post('https://httpbin.org/post', data=payload)

print("Status Code:", r.status_code)
print("Response Text:", r.text[:200]) # Previews server output

r.raise_for_status() # Raises an HTTPError for 4xx/5xx responses
r_dict = r.json()
print(r_dict['form'])
