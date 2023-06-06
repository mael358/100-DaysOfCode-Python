from datetime import datetime

import requests

GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 164
AGE = 22

APPLICATION_ID = ""
APPLICATION_KEY = ""
SHEET_TOKEN = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

input_text = input("Tell me which exercises you did: ")

request = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY
}

response_nutrition = requests.post(url=exercise_endpoint, json=request, headers=headers)
exercises = response_nutrition.json()

spreadsheet_endpoint = "https://api.sheety.co/9cdcd4b07eddb6a51c7a4163986dca47/myWorkouts/workouts"

today = datetime.now()
print(f"Date: {today.strftime('%Y%m%d')}")
print(f"Time: {today.strftime('%X')}")

sheet_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

for exercise in exercises['exercises']:
    workout_payload = {
        "workout": {
            "date": today.strftime('%Y%m%d'),
            "time": today.strftime('%X'),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=spreadsheet_endpoint, json=workout_payload, headers=sheet_headers)
    print(sheet_response.text)
