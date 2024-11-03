"""CP1404 Practical - Guitar Test"""

from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Other Guitar", 2014, 10)

    print(f"{guitar.name} get_age() - Expected {102}. Got {guitar.get_age()}")
    print(f"{other_guitar} get_age() - Expected {10}. Got {other_guitar.get_age()}")


main()
