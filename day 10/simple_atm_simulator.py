print("=== welcome to ATM ===")
print("make your choice:")

balance = 1000
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("enter your choice (1-4): ")
    if choice == "1":
        print(f"Your balance is: ${balance}")
    elif choice == "2":
        deposit = float(input("Enter amount to deposit: $"))
        if deposit > 0:
            balance = balance + deposit
            print(f"your new balance will be: ${balance}")
        else:
            print("Deposit amount must be positive.")
    elif choice == "3":
        withdraw = float(input("Enter amount to withdraw: $"))
        if withdraw <= 0:
            print("withdraw amount must be positive.")
        elif withdraw > balance:
            print("Insufficient funds.")
        else:
            balance = balance - withdraw
            print(f"your new balance will be: ${balance}")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
