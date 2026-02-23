#oefening basis tekst

with open("hello.txt", "w") as f:
    f.write("here we gooooo")

with open("hello.txt", "r") as f:
    inhoud = f.read()
    print("dit staat er in:", inhoud)

#oefening 2 json bestand

import json

info = {"naam": "nick", "age": 27, "gym": "yes"}

with open("data.json", "w") as f:
    json.dump(info, f, indent=2)
    print("info saved")

with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
    print(data["gym"])
