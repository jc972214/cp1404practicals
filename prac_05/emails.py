"""Emails Exercise"""

email_to_name = {}
user_email = input("Enter your email address: ")
while user_email != "":
    try:
        name = user_email.title().split("@")[0]
        if "." in name:
            name = name.split(".")
            name = " ".join(name)
        print(f"Is your name {name}? (y/n)")
        correct_name = input("")
        if correct_name.lower() != "y" and correct_name != "":
            name = input("Name: ").title()
        email_to_name[user_email] = "".join(name)

    except KeyError:
        print("Email address is not valid")
    user_email = input("Enter your email address: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
