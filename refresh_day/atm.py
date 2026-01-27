print("=== atm machine ===")

balance = 1000

while True:
    print()
    print("1. check balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")
    print()

    choice = input("choice: ")

    if choice == "1": 
        print("balance:", balance)
    elif choice == "2":
        amount = float(input("amount to deposit:"))
        balance = balance + amount
        print("you deposited:", amount)
        print("your new balance is:", balance)
    elif choice == "3":
        amount = float(input("amount to withdraw:"))
        if amount > balance:
            print("not enough money!")
        else:
             balance = balance - amount
             print("withdraw amount:", amount)
             print("new balance:", balance)
    elif choice == "4":
        print("goodby")
        break
print("ATM closed")