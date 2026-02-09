print("=== nummer zoeken ===")

nummers = [1, 6, 15]

while True:
    user_input = int(input("guess number between 1-20: "))
    if user_input in nummers:
        print(" in the list")
        break
    else:
        print("not in the list")
        