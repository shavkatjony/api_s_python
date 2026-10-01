import requests
from datetime import datetime
MY_LAT = 35.167397
MY_LONG = 129.068878

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()


iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

if 

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()

print(sunrise)

sunrise_hour = sunrise.split("T")[1].split(":")[0]
print("Sunrise Hour (UTC):", sunrise_hour)

