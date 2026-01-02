#check if someone can vote

print("Welcome to the voting app!")
print()

age = int(input("enter you age: "))
print()
if age >= 18:
    print("you can vote")
else:
    years_left = 18 - age
    print(f"you cannot vote yet")
    print()
    print(f"wait {years_left} more years to vote")

    