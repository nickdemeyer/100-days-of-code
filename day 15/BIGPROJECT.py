print("=== student grade manager ===")
students = []

while True:
    print("1. view students")
    print("2. add student")
    print("3. update grade")
    print("4. remove student")
    print("5. exit")
    choice = input("choose your option:")

    if choice == "1":
        if students == []:
            print("student list empty")
        else:
            for index, student in enumerate(students):
                print(f"{index + 1}. {student[0]} - {student[1]}")

    elif choice == "2":
        user_inp1 = input("student name: ")
        user_inp2 = input("student grade: ")
        students.append([user_inp1, user_inp2])
        print(f"{user_inp1} - {user_inp2} added to list")

    elif choice == "3":
        for z, student in enumerate(students):
            print(f"{z + 1}. {student[0]} - {student[1]}")
        user_inp = input("number change grade student: ")
        newgrade = input("new grade: ")
        students[z][1] = newgrade
        print("grade updated")

    elif choice == "4":
        for index, student in enumerate(students):
            print(f"{index + 1}. {student[0]} - {student[1]}")
        user_inp = int(input("select number to delete student: "))
        index = user_inp - 1
        students.pop(index)
        print("student successfully removed")

    elif choice == "5":
        print("exiting...")
        break