password = input("Enter your password: ")
while len(password) <= 0:
    print("Error: Invalid Password")
    password = input("Enter your password: ")
print(len(password)*"*")
