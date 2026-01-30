#creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Nick", 27, True, 1.85]  # Can mix types!

#accessing items (indexing starts at 0)
print("first fruit:", fruits[0])  # apple
print("second fruit:", fruits[1])  # banana
print("last fruit:", fruits[2])  # orange

#negative indexing (from the end)
print("last item:", fruits[-1])  # orange
print("second to last:", fruits[-2])  # banana

#length of list
print("number of fruits:", len(fruits))  