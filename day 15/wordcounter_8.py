print("=== word counter ===")

user_input = input("give me a sentence: ")
delete_spaces = len(user_input.replace(" ", ""))
print(f"there are {delete_spaces} letters in ur sentence")