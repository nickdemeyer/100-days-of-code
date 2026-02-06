print("=== contact list menu ===")

contacts = []

while True:
    print("1. show contacts")
    print("2. add contact")
    print("3. delete contact")
    print("4. exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        if contacts == []:
            print("No contacts found.")
        else:
            for i, contact in enumerate(contacts):
                print(f"{i + 1}. {contact}")
    elif choice == 2:
        contact = input("add your contact:")
        contacts.append(contact)
        print(f"your contact {contact} is added to your list")

    elif choice == 3:
        if contacts == []:
            print(f"no contacts to delete")
        else:
            for i, contact in enumerate(contacts):
                print(f"{i + 1}. {contact}")
        contact = int(input("choose number contact to delete:"))
        positie = contact - 1
        contacts.pop(positie)
        print(f"your contact number {contact} is deleted from your list")
    elif choice == 4:
        print("exiting...")
        break

        

