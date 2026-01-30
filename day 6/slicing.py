# getting parts of a list

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#list[start:end] - end is not included
print("first 3:", number[0:3])  # [0, 1, 2]
print("middle:", number[3:7])  # [3,4, 5, 6]
print("ending 3:", number[7:10])  # [7, 8, 9]

#shortcuts
print("first 5:", number[:5])  # [0, 1, 2, 3, 4]
print("from 5 to end:", number[5:])  # [5, 6, 7, 8, 9]
print("whole list:", number[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#with step
print("every 2nd:", number[::2])  # [0, 2, 4, 6, 8]
print("reverse:", number[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

