"""Password Checker"""

MINIMUM_LENGTH = 4

def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * "*")


def get_password(min_length):
    password = input("Enter your password: ")
    while len(password) < min_length:
        print(f"Error: Invalid Password. Needs at least {min_length} characters.")
        password = input("Enter your password: ")
    return password


main()
