user_name = input("Enter name: ")
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)

choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello " + user_name)
    elif choice == "G":
        print("Goodbye " + user_name)
    else:
        print("Invalid Choice")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")
