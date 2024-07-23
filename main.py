import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')

SHEET_NAME = "1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494"
sheety_ENDPOINT = "https://api.sheety.co/672b6a5d3244d94030d69c4f61625b07/mainWorkout/sheet1"
NUTRITION_NATURAL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 165
AGE = 23
exercise_text = input("Tell me which exercises you did: ")

headers = {
    'Content-Type': 'application/json',
    "x-app-id": f"{APP_ID}",
    "x-app-key": f"{API_KEY}"
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutrition = requests.post(url=NUTRITION_NATURAL_ENDPOINT, json=parameters, headers=headers)
result = nutrition.json()
print(result)

headers_auth = {
    'Authorization': "Basic TmlzaGFudDMyOk5FVkVSQDEwMjE=",
}

# post for adding a row
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_add_row = requests.post(url=sheety_ENDPOINT, json=sheet_inputs, headers=headers_auth)

    print(sheety_add_row.json())



