print("=== simple workout tracker ===")

workouts = []

while True:
    print("1. view workouts")
    print("2. add exercise")
    print("3. update exercise")
    print("4. delete exercise")
    print("5. exit ")
    choice = input("choose option: ")

    if choice == "1":
        if workouts == []:
            print("no workouts added yet")
        else:
            for i, workout in enumerate(workouts):
                print(f"{i + 1}. {workout[0]} - {workout[1]} sets - {workout[2]} reps")
    
    elif choice == "2":
            user_inp1 = input("name exercise: ")
            user_inp2 = input("sets exercise: ")
            user_inp3 = input("reps exercise: ")
            workouts.append([user_inp1, user_inp2, user_inp3])
            print("exercise added")

    elif choice == "3":
        for i, workout in enumerate(workouts):
            print(f"{i + 1}. {workout[0]} - {workout[1]} sets - {workout[2]} reps")
        user_inp = int(input("choose number exercise u want to change: "))
        i = user_inp - 1
        user_inp2 = input("change sets or reps?")
        if user_inp2 == "sets":
            user_inp3 = input("adjust sets: ")
            workouts[i][1] = user_inp3
            print("sets changed")
        elif user_inp2 == "reps":
            user_inp3 = input("adjust reps: ")
            workouts[i][2] = user_inp3
            print("reps changed")

    elif choice == "4":
        for i, workout in enumerate(workouts):
            print(f"{i + 1}. {workout[0]} - {workout[1]} sets - {workout[2]} reps")
        user_inp = int(input("choose number to delete workout: "))
        i = user_inp - 1
        workouts.pop(i)
        print("workout deleted")

    elif choice == "5":
        print("exiting...")
        break