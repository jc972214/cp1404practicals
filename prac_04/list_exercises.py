"""List Exercises for Practical 4"""


def main():
    numbers = []

    for number in range(5):
        num = int(input(f"Number: "))
        numbers.append(num)

    first_number(numbers)
    last_number(numbers)
    smallest_number(numbers)
    largest_number(numbers)
    average_number(numbers)

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    security_checker(usernames)


def first_number(numbers):
    first = numbers[0]
    print(f"The first number is {first}")


def last_number(numbers):
    last = numbers[-1]
    print(f"The last number is {last}")


def smallest_number(numbers):
    smallest = min(numbers)
    print(f"The smallest number is {smallest}")


def largest_number(numbers):
    largest = max(numbers)
    print(f"The largest number is {largest}")


def average_number(numbers):
    average_numbers = sum(numbers) / len(numbers)
    print(f"The average of numbers is {average_numbers}")


def security_checker(usernames):
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
