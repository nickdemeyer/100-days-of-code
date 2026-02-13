print("=== workout tracker ===")

def view_workouts(workouts):
    if workouts == []:
        print("no workouts")
    else:
        for i, workout in enumerate(workouts):
            print(f"{i + 1}. {workout[0]} - {workout[1]} sets - {workout[2]} reps - {workout[3]} kg")

def add_workout(workouts):
    user_inp1 = int(input("exercise: "))
    user_inp2 = int(input("sets: "))
    user_inp3 = int(input("reps: "))
    user_inp4 = int(input("weight: "))
    workouts.append([user_inp1, user_inp2, user_inp3, user_inp4])
    print("workout added")

def update_workout(workouts):
    if workouts == []:
        print("no workouts")
        return
    view_workouts(workouts)
    user_inp = int(input("choose workout number u want to change: "))
    i = user_inp - 1
    user_inp2 = input("choose update sets,reps or weight: ")
    if user_inp2 == "sets":
        new_inp = int(input("new sets: "))
        workouts[i][1] = new_inp
        print("updated")
    elif user_inp2 == "reps":
        new_inp = int(input("new reps: "))
        workouts[i][2] = new_inp
        print("updated")
    elif user_inp2 == "weight":
        new_inp = int(input("new weight: "))
        workouts[i][3] = new_inp
        print("updated")

def delete_workout(workouts):
    if workouts == []:
        print("no workouts")
        return
    view_workouts(workouts)
    user_inp = int(input("choose workout number u want to delete: "))
    i = user_inp - 1
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
        choice = input("choose option 1-5: ")
        if choice == "1":
            view_workouts(workouts)
        elif choice == "2":
            add_workout(workouts)
        elif choice == "3":
            update_workout(workouts)
        elif choice == "4":
            delete_workout(workouts)
        elif choice == "5":
            print("exiting...")
            break
main()