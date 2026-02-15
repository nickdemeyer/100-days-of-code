print("=== workout tracker ===")

def view_workouts(workouts):
    if workouts == []:
        print("no workouts")
    else:
        for i, workout in enumerate(workouts):
            print(f"{i + 1}. {workout[0]} - {workout[1]} sets - {workout[2]} reps - {workout[3]} kg")

def add_workout(workouts):
    inp1 = input("exercise: ")
    inp2 = int(input("sets: "))
    inp3 = int(input("reps: "))
    inp4 = int(input("weight: "))
    workouts.append([inp1, inp2, inp3, inp4])
    print("workout added")

def update_workout(workouts):
    if workouts == []:
        print("no workouts")
        return
    view_workouts(workouts)
    inp1 = int(input("choose workout number to change: "))
    i = inp1 - 1
    inp2 = input("do you want to change sets/reps or weight? ")
    if inp2 == "sets":
        inp3 = int(input("new sets: "))
        workouts[i][1] = inp3
        print("sets updated")
    elif inp2 == "reps":
        inp3 = int(input("new reps: "))
        workouts[i][2] = inp3
        print("reps updated")
    elif inp3 == "weight":
        inp3 = int(input("new weight: "))
        workouts[i][3] = inp3
        print("weight updated")

def delete_workout(workouts):
    if workouts == []:
        print("no workouts")
        return
    view_workouts(workouts)
    inp1 = int(input("choose workout number to delete: "))
    i = inp1 - 1
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
        choice = int(input("choose option 1-5: "))

        if choice == 1:
            view_workouts(workouts) 
        elif choice == 2:
            add_workout(workouts)
        elif choice == 3:
            update_workout(workouts)
        elif choice == 4:
            delete_workout(workouts)
        elif choice == 5:
            print("exiting")
            break

main()