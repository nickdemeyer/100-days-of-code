#smart calculator

print("=== SMART CALCULATOR ===")

#user input
num1 = float(input("enter first number: "))
operator = input("enter operator (+, -, *, /): ")
num2 = float(input("enter second number: "))

#variables
result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2

#outcome
if operator == "+":
    print(f"{num1} + {num2} = {result1}")
elif operator == "-":
    print(f"{num1} - {num2} = {result2}")
elif operator == "*":
    print(f"{num1} * {num2} = {result3}")
elif operator == "/":
    if num2 != 0:
        result4 = num1 / num2
        print(f"{num1} / {num2} = {result4}")
    else:
        print("error: division by zero is not allowed")