#different ways to remove items

fruits = ["apple", "banana", "orange", "grape", "apple"]
print("start:", fruits)

#remove() - removes first matching value
fruits.remove("apple")
print("after remove('apple'):", fruits)

#pop() - remove and returns last item
last = fruits.pop()
print("popped:", last)
print("after pop():", fruits)

#pop(index) - remove at specific position
second = fruits.pop(1)
print("popped index 1:", second)
print("after pop(1):", fruits)

#del - delete by index
del fruits[0]
print("after del fruits[0]:", fruits)

#clear() - empty the list
fruits.clear()
print("after clear():", fruits)