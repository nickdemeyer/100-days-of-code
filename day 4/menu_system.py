#a program that keeps running until you quit

print("=== simple menu ===")

while True:
    print()
    print("1. say hello")
    print("2. say goodbye")
    print("3. show time")
    print("4. exit")
    print()

    choice = input("enter your choice (1-4): ")

    if choice == "1":
        print("hello!")
    elif choice == "2":
        print("goodbye!")
    elif choice == "3":
        print("time to code!")
    elif choice == "4":
        print("exiting program...")
        break
    else:
        print("invalid choice, please try again")

print("program ended")
    