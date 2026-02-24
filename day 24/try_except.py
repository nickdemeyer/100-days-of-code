#oefening try/except block

import json

bestandsnaam = "workouts.json"

try:
    with open(bestandsnaam, "r") as f:
        workouts = json.load(f)
        print(workouts)
except FileNotFoundError:
    print("file not found")

