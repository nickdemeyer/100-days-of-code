#different ways to add items

shopping = []
print("start shopping:", shopping)

#append () -add to end
shopping.append("milk")
shopping.append("bread")
shopping.append("eggs")
print("after appending:", shopping)

#insert() - add to specific position
shopping.insert(0, "apples")  # add apples to start
shopping.insert(2, "cheese") #add to index 2
print("after insert:", shopping)

#extend() - add multiple items at once
more_items = ["butter", "coffee"]
shopping.extend(more_items)
print("after extend", shopping)
