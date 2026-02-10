print("list check empty or not")

items = []

item1 = input("item 1: ")
if item1 != "":
    items.append(item1)
item2 = input("item 2: ")
if item2 != "":
    items.append(item2)
item3 = input("item 3: ")
if item3 != "":
    items.append(item3)

if items == []:
    print("list is empty")
else:
    print("list is filled with items.")