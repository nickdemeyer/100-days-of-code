#combining conditions

print("=== movie theater entry ===")
print()

age = int(input("enter your age: "))
has_ticket = input("do you have a ticket? (yes/no): ")
print()
#both conditions must be true
if age >= 18 and has_ticket == "yes":
    print("enjoy the movie!")
elif age >= 18 and has_ticket == "no":
    print("go buy a ticket first.")
elif age < 18 and has_ticket == "yes":
    print("only 18+ allowed.")
else:
    print("come back when you're older and with a ticket.")

    