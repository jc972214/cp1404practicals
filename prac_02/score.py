"""Result Checker"""
import random
from random import randint


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(f"Your result is: {result}")
    print()
    random_score = randint(0, 100)
    print(f"The random score is: {random_score}")
    random_result = get_result(random_score)
    print(f"The random result is: {random_result}")


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


main()
