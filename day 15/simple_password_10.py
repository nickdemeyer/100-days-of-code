print("=== simpele password loop ===")
password = "python123"

while True:
    user_input = input("type your password: ")
    if password == user_input:
        print("access granted")
        break
    else:
        print("wrong password try again")