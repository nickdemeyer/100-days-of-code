print("===calculator===")
print()

while True:
    operator = input("enter operator (+, -, *, /, quit)")

    if operator == "quit":
        break

    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))

    if operator == "+":
        result1 = num1 + num2
        print(f"{num1} + {num2} = {result1}")
    elif operator == "-":
        result2 = num1 - num2
        print(f"{num1} - {num2} = {result2} ")
    elif operator == "*":
        result3 = num1 * num2
        print(f"{num1} * {num2} = {result3}")
    elif operator == "/":
        if num2 != 0:
            result4 = num1 / num2
            print(f"{num1} / {num2} = {result4}")
        else:
            print("error: division by zero not allowed")

 