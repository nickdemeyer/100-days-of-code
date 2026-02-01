print("=== to do list manager ===")

tasks = []

while True:
    print()
    print("1. add task")
    print("2. view tasks")
    print("3. remove task")
    print("4. delete all tasks")
    print("5. exit")

    choice = input("choice: ")

    if choice == "1":
        task = input("enter task: ")
        tasks.append(task)
        print(f"added: {task}")
    elif choice == "2":
        if len(tasks) == 0:
            print("no tasks in the list.")
        else:
            print("tasks to complete:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
    elif choice == "3":
        if len(tasks) == 0:
            print("no tasks to remove.")
        else:
            print("tasks to complete:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            task_num = int(input("enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"removed: {removed_task}")
            else:
                print("invalid task number.")
    elif choice == "4":
        if len(tasks) == 0:
            print("no tasks to delete.")
        else:
            confirm = input(f"delete all {len(tasks)} tasks? (y/n): ")
            if confirm.lower() == "y":
                tasks.clear()
                print("all tasks deleted.")
            else:
                print("deletion cancelled.")
    elif choice == "5":
        print("exiting...")
        break
    else:
        print("invalid choice")
print("program terminated.")