#input from user
person = input("what is your birthyear? ")

#current year
current_year = 2025
future = 2050

#input to integer
int_birthyear = int(person)

#calculate age
age = current_year - int_birthyear
print(f"you are {age} years old")
age_future = future - int_birthyear
print("you are", age_future, "years old in 2050")

