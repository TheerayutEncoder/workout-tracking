import requests
from datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


QUERY = input("Tell me which exercises you did: ").lower()
GENDER = "male"
WEIGHT = 50
HEIGHT = 161
AGE = 23

NATURAL_EXERCISE_ENDPONT = os.environ.get("NATURAL_EXERCISE_ENDPONT")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

headers = {
     "x-app-id": APP_ID,
     "x-app-key": API_KEY
}

body = {
     "query": QUERY,
     "gender": GENDER,
     "weight_kg": WEIGHT,
     "height_cm": HEIGHT,
     "age": AGE
}

response = requests.post(url=NATURAL_EXERCISE_ENDPONT, json=body, headers=headers)
response.raise_for_status()
results = response.json()
# print(results)

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

detail = {
     "workout": {
             "date": today,
             "time": now_time,
             "exercise": "",
             "duration": "",
             "calories": "",
    }
}


for data in results["exercises"]:
    detail["workout"]["exercise"] = data["user_input"].title()
    detail["workout"]["duration"] = str(data["duration_min"])
    detail["workout"]["calories"] = str(data['nf_calories'])
    response = requests.post(url=SHEETY_ENDPOINT,
                             json=detail,
                             auth=(
                                USERNAME,
                                PASSWORD,
                             )
                             )
    response.raise_for_status()

