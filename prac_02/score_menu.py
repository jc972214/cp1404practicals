"""Score Menu"""

MENU = """G - Get Valid Score
P - Print Result
S - Show Stars
Q - Quit

"""


def main(score='none'):
    score = get_valid_score(score)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(score)
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print(get_stars(score))
        else:
            print("Invalid Choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank You.")


def get_valid_score(score):
    score = int(input("Enter Valid Score: "))
    while score < 0 or score > 100:
        print("Invalid. Score must be between 0 and 100. Try Again.")
        score = int(input("Enter Valid Score: "))
    return score


def get_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def get_stars(score):
    return "*" * score


main()
