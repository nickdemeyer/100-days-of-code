#list comprehensions - lists in one line

#old way: list of squares
squares = []
for i in range(1,6):
    squares.append(i * i)
    print("squares:", squares)

#new way: list comprehension
squares = [i * i for i in range(1,6)]
print("squares with list comprehension:", squares)

#with condition: even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print("even numbers:", evens)

#transform list
fruits = ['apple', 'banana', 'cherry', 'date']
upper_fruits = [fruit.upper() for fruit in fruits]
print("uppercase:", upper_fruits)