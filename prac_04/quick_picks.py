import random

MIN_NUMBER = 1

MAX_NUMBER = 45


def main():

    get_pick = int(input("How many quick picks? "))
    for number in range(get_pick):
        numbers = []
        pick(numbers)
        print(" ".join(str(number) for number in numbers))

def pick(numbers):
    for i in range(6):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(number)
    numbers.sort()

main()