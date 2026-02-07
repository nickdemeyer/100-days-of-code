print("=== pokemon boosterbox list ===")

boxes = []

while True:
    print("1. view boxes")
    print("2. add boxes")
    print("3. delete boxes")
    print("4. exit list")
    print()
    choice = input("choose option 1-4")
    print()
    if choice == "1":
        if boxes == []:
            print("no boxes added to list yet")
        else:
            for index, box in enumerate(boxes):
                print(f"{index + 1}. {box}")

    elif choice == "2":
        user_input = input(f"add your box:")
        boxes.append(user_input)
        print(f"your box {user_input} is added to the list")

    elif choice == "3":
        if boxes == []:
            print("no boxes to delete")
        else:
            for index, box in enumerate(boxes):
                print(f"{index + 1}. {box}")
        user_input = int(input("which box do you want to delete? (only numbers from the list work)"))
        output = user_input - 1
        boxes.pop(output)
        print(f"you succesfully deleted number {user_input} from your list")

    elif choice == "4":
        print("exiting...")
        break




