print("mini score tracker")

score = 0
print("answer the yes or no questions: ")
while True:
    quest1 = input("is this black?")
    if quest1 == "yes":
        score = score + 1
        print("correct")
    elif quest1 == "no":
        print("oopss continue")
    
    quest2 = input("is it red?")
    if quest2 == "yes":
        score = score + 1
        print("correct")
    elif quest2 == "no":
        print("oopss continue")
    
    quest3 = input("we are monday today?")
    if quest3 == "yes":
        score = score + 1
        print("correct")
    elif quest3 == "no":
        print("ooppss continue")

    quest4 = input("are you a nice person?")
    if quest4 == "yes":
        score = score + 1
        print("correct")
    elif quest4 == "no":
        print("ooppss continue")

    quest5 = input("the sky is blue?")
    if quest5 == "yes":
        score = score + 1
        print("correct")
    elif quest5 == "no":
        print("oopss ")
    break

print(f"your total score is: {score}/5")