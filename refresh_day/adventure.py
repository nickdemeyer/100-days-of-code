print("=== Dark Forest Adventure ===")
print()
print("you're at a crossroads in a dark forest.")
print()

choice1 = input("did you go left or right?")

if choice1 == "left":
    print("you find a treasure!")

    choice2 = input("do you open or leave it?")

    if choice2 == "open":
        print("game over! you got trapped!")
    else:
        print("congratz you can exit! you win!")

elif choice1 == "right":
    print("you encouter a bear")

    choice3 = input("you try to sneak by or fight?")

    if choice3 == "sneak by":
        print("you succesfully escaped!")
    else:
        print("oh dear, you dead!")
else:
    print("invalid choice!")