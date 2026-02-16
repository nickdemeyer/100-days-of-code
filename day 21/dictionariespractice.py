#dictionaries practice

#exercise 1
oefening = {"naam" : "squat", "sets" : 3, "gewicht" : 60}
print(oefening.get("gewicht"))
oefening.update({"gewicht" : 70})
print(oefening.get("gewicht"))

#exercise 2 stock management
stock = {"creatine": 500, "proteine": 2000}
stock.update({"pre-workout": 250})
user_inp = input("fill in product: ")
if user_inp in stock:
    print(f"yes we have {stock.get(user_inp)}g")
else:
    print("not available")

#exercise 3 personal message gym members
members = {"tom": "bench press", "sarah": "deadlift", "julia": "pull ups"}
for name, exercise in members.items():
    print(f"{name} favoroute exercise is {exercise}")

#exercise 4 tracker structure
workout_log = {"16/02/26": {"exercise": "pulldown", "sets": 5, "weight": 50 }}
print(f"i did today {workout_log["16/02/26"]["weight"]}kg")