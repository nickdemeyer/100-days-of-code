print("===grocery list===")

list = []

while True:
    print("1. view list")
    print("2. add item")
    print("3. remove item")
    print("4. exit")    

    choice = input("Choose an option: ")
    if choice == "1":
        if list == []:
            print("list is empty.")
        else:
            for i, item in enumerate(list):
                print(f"{i + 1}. {item}")
        
    elif choice == "2":
        item = input("Enter item to add: ")
        list.append(item)
        print(f"{item} added to the list.")

    elif choice == "3":
        item = int(input("Enter item number to remove: "))
        index = item - 1
        if 0 < item <= len(list):
            removed_item = list.pop(index)
            print(f"{removed_item} removed from the list.")
        else:
            print("Invalid item number.")

    elif choice == "4":
        print("Exiting the program.")
        break