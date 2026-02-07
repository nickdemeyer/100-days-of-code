print("=== Workout Tracker ===")

workouts = []

while True:
    print("1. view workouts")
    print("2. add workout")
    print("3. update workout")
    print("4. delete workout")
    print("5. exit")
    choice = input("choose what you want to do: ")

    if choice == "1":
        if workouts == []:
            print("No workouts yet.")
        else:
            for i, workout in enumerate(workouts):
                print(f"{i + 1}. {workout[0]} - {workout[1]} sets")

    elif choice == "2":
        user_input1 = input("name workout: ")
        user_input2 = input("sets done: ")
        workouts.append([user_input1, user_input2])
        print(f"you successfully added workout: {user_input1} - {user_input2} sets")

    elif choice == "3":
        for i, workout in enumerate(workouts):
            print(f"{i + 1}. {workout[0]} - {workout[1]} sets")
        user_input = int(input("which workout do you want to change? "))
        index = user_input - 1
        
        new_set = int(input("new sets number: "))
        workouts[index][1] = new_set

        print("workout successfully updated")

    elif choice == "4":
        if workouts == []:
            print("no workouts to delete")
        else:
            for i, workout in enumerate(workouts):
                print(f"{i + 1}. {workout[0]} - {workout[1]} sets")
        user_input = int(input("which workout number do you want to delete? "))
        index = user_input - 1
        workouts.pop(index)
        print(f"you deleted successfully your workout")

    elif choice == "5":
        print("exiting...")
        break