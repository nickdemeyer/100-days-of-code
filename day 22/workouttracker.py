def view_workout(workouts):
    if workouts == []:
        print("no workouts")
    else:
        for i, workout in enumerate(workouts):
            print(f"{i + 1}. {workout["date"]}: {workout["exercise"]} - {workout["sets"]} sets - {workout["reps"]} reps - {workout["weight"]} kg")

def add_workout(workouts):
    user_inp1 = input("add date: ")
    user_inp2 = input("add name exercise: ")
    user_inp3 = int(input("add amount of sets: "))
    user_inp4 = int(input("add amount of reps: "))
    user_inp5 = int(input("add weight used: "))
    workout = {"date": user_inp1, "exercise": user_inp2, "sets": user_inp3, "reps": user_inp4, "weight": user_inp5}
    workouts.append(workout)
    print("workout added")

def update_workout(workouts):
    if workouts == []:
        print("no workouts")
        return
    view_workout(workouts)
    user_inp1 = int(input("choose workout number to change: "))
    i = user_inp1 - 1
    user_inp2 = input("choose date/exercise/sets/reps/weight: ")
    if user_inp2 == "date":
        user_inp3 = input("type new date: ")
        workouts[i]["date"] = user_inp3
        print("date updated")
    elif user_inp2 == "exercise":
        user_inp3 = input("type exercise: ")
        workouts[i]["exercise"] = user_inp3
        print("exercise updated")
    elif user_inp2 == "sets":
        user_inp3 = int(input("new sets amount: "))
        workouts[i]["sets"] = user_inp3
        print("sets updated")
    elif user_inp2 == "reps":
        user_inp3 = int(input("new reps amount: "))
        workouts[i]["reps"] = user_inp3
        print("reps updated")
    elif user_inp2 == "weight":
        user_inp3 = int(input("new weight amount: "))
        workouts[i]["weight"] = user_inp3
        print("weight updated")

def delete_workout(workouts):
    if workouts == []:
        print("no workouts")
        return
    view_workout(workouts)
    user_inp1 = int(input("choose workout number to delete: "))
    i = user_inp1 - 1
    workouts.pop(i)
    print("workout deleted")
    
def main():
    workouts = []

    while True:
        print("1. view workouts")
        print("2. add workout")
        print("3. update workout")
        print("4. delete workout")
        print("5. exit")
        choice = int(input("choose which number to continue: "))

        if choice == 1:
            view_workout(workouts)
        elif choice == 2:
            add_workout(workouts)
        elif choice == 3:
            update_workout(workouts)
        elif choice == 4:
            delete_workout(workouts)
        elif choice == 5:
            print("exiting...")
            break
main()