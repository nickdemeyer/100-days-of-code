print("===simple calculator===")
print()

#get numbers from user
num1 = input("enter first number: ")
num2 = input("enter second number: ")

#convert to numbers (floats allow decimals)
num1 = float(num1)
num2 = float(num2)

#calculate everything
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

#print results
print("===results===")
print(num1, "+", num2, "=", addition)
print(num1, "-", num2, "=", subtraction)
print(num1, "*", num2, "=", multiplication)
print(num1, "/", num2, "=", division)

