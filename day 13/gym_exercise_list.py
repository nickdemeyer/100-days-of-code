print("=== gym exercises to do ===")

list = []

while True:
    print("1. view exercises")
    print("2. add exercise")
    print("3. delete exercise")
    print("4. exit")
    user_input = input(f"choose a number 1-4:")

    if user_input == "1":
        if list == []:
            print(f"no exercises yet")
        else:
            for index, exercise in enumerate(list):
                print(f"{index + 1}. {exercise}")
    elif user_input == "2":
        user_input = input(f"which exercise you want to add?")
        list.append(user_input)
        print(f"you successfully added {user_input}")
    elif user_input == "3":
        if list == []:
            print(f"no exercises to delete")
        else:
            for index, exercise in enumerate(list):
                print(f"{index + 1}. {exercise}")
        user_input = int(input(f"which exercise number you want to delete?"))
        number = user_input - 1
        list.pop(number)
        print(f"you successfully deleted number {user_input} of your list")
    elif user_input == "4":
        print("exiting program...")
        break
    else:
        print("invalid input,choose number 1-4")
        continue