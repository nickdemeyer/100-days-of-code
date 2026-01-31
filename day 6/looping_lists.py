#looping through lists

fruits = ['apple', 'banana', 'cherry', 'date']

#method 1: using a for loop
print("method 1:")
for fruit in fruits:
    print(fruit)

print()

#method 2: with index
print("method 2:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

print()

#method 3: enumerate(best method)
print("method3:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

