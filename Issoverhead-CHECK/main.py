import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 18.757420
MY_LONG = 73.413727

My_address="surajpatil12012006@gmail.com"
password="cxndzhfevljmptbt"

print(datetime.now().hour)

def iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LAT + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour=time_now.hour

    if hour <= sunrise or hour >= sunset:
        return True


while True:
    if iss_above() and is_night():
        time.sleep(60)
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=My_address, password=password)
            connect.sendmail(from_addr=My_address, to_addrs=My_address,
                        msg="Subject:see up\n\n you can see the satellite ")





#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude


#Your position is within +5 or -5 degrees of the ISS position.



# if 13.757420 <= iss_latitude <= 23.757420 and 68.413727 <= iss_longitude <= 78.413727:
# if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LAT+5:
#     if 19 <= hour <= 5:
#         print("see up you can see the satellite")

