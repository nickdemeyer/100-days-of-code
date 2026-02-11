#drill 1 sum of all reps #print total reps per exercise

workouts = [["pushups", 4, 12], ["pullups", 4, 10], ["dips", 4, 9]]

for i, workout in enumerate(workouts):
    print(f"total reps {workout[0]}: {workout[1]* workout[2]}")
print()

#drill 2 print exercise with most total reps

most_reps = 0
best_exercise = "" #lege container die we later vervangen door bv pushups - zodra de loop controleert parkeer je de exercise naam hier in waar de meeste reps zijn

for workout in workouts:
    name = workout[0]
    total_reps = workout[1] * workout[2]

    if total_reps > most_reps: #iedere keer als we een groter getal tegenkomen dan we al hadden ervoor 
        most_reps = total_reps #dit is voor aan te passen iedere keer de loop een grotere total_reps vind
        best_exercise = name
print(f"{best_exercise} has the most total reps: {most_reps}")
print()
#drill 3 print only names of exercises without reps and sets

for i, workout in enumerate(workouts):
    print(f"{workout[0]}")
print()

#drill 4 calculate average reps per set over all exercises

total_sets = 0
total_reps = 0

for workout in workouts:
    sets = workout[1]
    reps = workout[2]

    total_reps += sets * reps
    total_sets += sets
average = total_reps // total_sets
print(f"the average reps u doing is {average}")
print()

#drill 5 search if exercise name exists

user_inp = input("type exercise name u looking for: ")
found = False #dit is als manier die door iedere lijst gaat de loop loopt door iedere workout[0] en controleert of het dan true is, zo heb je 1 print nadat het door de volledige loop is gelopen.

for workout in workouts:
    if workout[0] == user_inp:
        found = True
        
if found:
    print("exercise in list")
else:
    print("exercise not in list")