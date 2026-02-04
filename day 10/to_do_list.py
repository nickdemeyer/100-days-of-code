print("=== tasks for today ===")

tasks = []

while True:
    print("1. view tasks")
    print("2. add task")
    print("3. remove task")
    print("4. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        if tasks == []:
            print("No tasks for today.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == "2":
        task = input("enter new task:")
        tasks.append(task)
        print(f"{task} added to tasks.")

    elif choice == "3":
        if tasks == []:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            num = int(input("enter task number to remove:"))
            index = num - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"{removed_task} removed from tasks.")
            else:
                print("Invalid task number.")
    elif choice == "4":
        print("Exiting the program.")
        break
