#keep asking until correct password

correct_password = "pythonRocks!"
attempts = 0

print("=== login system ===")

while True: #loop forever until break
    password = input("enter password: ")
    attempts = attempts + 1

    if password == correct_password:
        print("access granted")
        print(f"you took {attempts} attempts")
        break
    else:
        print("incorrect password, try again")

print("=== end of program ===")