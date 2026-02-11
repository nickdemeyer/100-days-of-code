print("=== progressive overload tracker ===")

workouts = []

while True:
    print("1. view workouts")
    print("2. add workout")
    print("3. update workout")
    print("4. delete workout")
    print("5. check progress")
    print("6. exit")
    choice = input("choose option: ")

    if choice == "1":
        if workouts == []:
            print("workout list empty")
        else:
            for i, workout in enumerate(workouts):
                print(f"{i + 1}. {workout[0]} - {workout[1]} sets - {workout[2]} reps")

    elif choice == "2":
        inp1 = input("exercise: ")
        inp2 = int(input("sets: "))
        inp3 = int(input("reps: "))
        workouts.append([inp1, inp2, inp3])
        print("workout added")

    elif choice == "3":
        if workouts == []:
            print("no workouts to update")
        else:
            for i, workout in enumerate(workouts):
                print(f"{i + 1}. {workout[0]} - {workout[1]} sets - {workout[2]} reps")
        inp1 = int(input("which workout number do you want to change? "))
        i = inp1 - 1
        inp2 = input("change sets or reps? ")
        if inp2 == "sets":
            inp3 = int(input("new sets: "))
            workouts[i][1] = inp3
            print("updated")
        elif inp2 == "reps":
            inp3 = int(input("new reps: "))
            workouts[i][2] = inp3
            print("updated")

    elif choice == "4":
        if workouts == []:
            print("no workouts to delete")
        else:
            for i, workout in enumerate(workouts):
                print(f"{i + 1}. {workout[0]} - {workout[1]} sets - {workout[2]}")
        inp1 = int(input("which workout number do you want to delete? "))
        i = inp1 - 1
        workouts.pop(i)
        print("workout deleted")

    elif choice == "5":
        for i, workout in enumerate(workouts):
            total_reps = workout[1] * workout[2]
            print(f"{i + 1}. {workout[0]} - {total_reps} ")
            if total_reps > 40:
                print("very strong")
            elif total_reps >= 25:
                print("strong")
            elif total_reps < 25:
                print("can better")

    elif choice == "6":
        print("exiting...")
        break