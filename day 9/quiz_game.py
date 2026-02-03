print("welcome to the quiz!")

score = 0
answer1 = 7
user1 = input("how many days are in the week?")
if user1.isdigit() == False:
    print("please enter a number next time")
    user1 = input("how many days are in the week?")
    if int(user1) == answer1:
        print("correct!")
        score = score + 1
        print(f"your score is {score}/3")
    else:
        print("incorrect")
    
answer2 = "dad"
user2 = input("you have a mom and...")
if user2 == answer2:
    print("correct!")
    score = score + 1
    print(f"your score is {score}/3")
else:
    print("incorrect")

answer3 = "egg"
user3 = input("what do i eat a lot?")
if user3 == answer3:
    print("correct!")
    score = score + 1
    print(f"your score is {score}/3")
else:
    print("incorrect")
print()
print(f"your final score is {score}/3")

if score == 3:
    print("perfect score!")
elif score == 2:
    print("well done!")
elif score <= 1:
    print("keep practicing!")