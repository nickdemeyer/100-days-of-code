#useful list methods

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("original numbers:", numbers)

#sort() - sorts the list 
numbers.sort()
print("sorted:", numbers)

#reverse() - reverses the list
numbers.reverse()
print("reversed:", numbers)

#count() - how many times value appears
numbers = [1, 2, 3, 2, 4, 2, 5]
print("count of 2:", numbers.count(2))

#index() - find position of value
print("position 4:", numbers.index(4))

#check if item exists
if 3 in numbers:
    print("3 is in the list")

if 10 not in numbers:
    print("10 is not in the list")