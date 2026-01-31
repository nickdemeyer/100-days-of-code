print("=== to do list manager ===")

tasks = []

while True:
    print()
    print("1. add task")
    print("2. view tasks")
    print("3. remove task")
    print("4. exit")

    choice = input("choice: ")

    if choice == "1":
        task = input("enter task: ")
        tasks.append(task)
        print(f"added: {task}")

    if choice == "4":
        print("exiting...")
        break
print("program terminated.")