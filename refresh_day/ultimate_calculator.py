print("=== ultimate calculator ===")

history = []

while True:
    print()
    print("operations:")
    print(" + (add)")
    print(" - (substract)")
    print(" * (multiply)")
    print(" / (divide)")
    print(" history (show history)")
    print(" clear (clear history)")
    print(" quit (exit)")
    print()

    operation = input("choose operation: ")

    if operation == "+":
        num1 = float(input("first number:"))
        num2 = float(input("second number:"))
        result = num1 + num2
        print("result:", result)

        calc = f"{num1} + {num2} = {result}"
        history.append(calc)
    elif operation == "-":
        num1 = float(input("first number:"))
        num2 = float(input("second number:"))
        result = num1 - num2
        print("result:", result)

        calc = f"{num1} - {num2} = {result}"
        history.append(calc)
    elif operation == "*":
        num1 = float(input("first number:"))
        num2 = float(input("second number:"))
        result = num1 * num2
        print("result:", result)

        calc = f"{num1} * {num2} = {result}"
        history.append(calc)
    elif operation == "/":
        num1 = float(input("first number:"))
        num2 = float(input("second number:"))
        if num2 == 0:
            print("cannot divide by zero")
        else:
            result = num1 / num2
            print("result:", result)

            calc = f"{num1} / {num2} = {result}"
            history.append(calc)
    elif operation == "history":
        if len(history) == 0:
            print("no data yet")
        else:
            print()
            print("=== history ===")
            for calculation in history:
                print(calculation)
    elif operation == "quit":
        print("goodbye")
        break
    elif operation == "clear":
        history = []
        print("history cleared!")
    else:
        print("invalid history")
    
print("calculator closed")