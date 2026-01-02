#check grade based on score

print("==== Grade Checker =====")

score = int(input("enter your score (0-100): "))

if score >= 90:
    print("grade: A")
elif score >= 80:
    print("grade: B")  
elif score >= 70:
    print("grade: C")
elif score >= 60:
    print("grade: D")
else:
    print("grade: F")

    