# dear deveoloper this codes is now be the complete in like 4 month , until then we have to make perfection 
#the number of triels to understand the full api throuth the different courses and tutorials is more than 30 resources 
# date: start date :2026,08,12 , 

# started using the postman api platform and the  working with questiins 
import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    print(data['title'])
    print([data['link'])
    print()