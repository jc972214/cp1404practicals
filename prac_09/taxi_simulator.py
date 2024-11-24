"""Prac 09 - Taxi Simulator"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Execute Taxi Simulator"""
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower().strip()
    while choice != "q":
        bill = 0
        if choice == "c":
            current_taxi = choose_taxis(taxis)
        elif choice == "d":
            bill = determine_cost(current_taxi, taxis)
        else:
            print("Invalid choice")
        bill_to_date += bill
        print(f"Bill to date: {bill_to_date}")
        print(MENU)
        choice = input(">>> ").lower().strip()


def determine_cost(current_taxi, taxis):
    """Determines the cost of a taxi"""
    try:
        taxi_trip = int(input("Drive how far? "))
        taxis[current_taxi].drive(taxi_trip)
        print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare()}")
        return taxis[current_taxi].get_fare()
    except TypeError:
        print("No taxi selected")
    except ValueError:
        print("Invalid distance")


def choose_taxis(taxis):
    """Choose a taxi from list of taxis"""
    print("Taxis available:")
    for count, taxi in enumerate(taxis):
        print(f"{count} - {taxi}")
    try:
        current_taxi = int(input("Choose taxi: ").strip())
        if current_taxi > (len(taxis) - 1):
            print("Invalid taxi choice.")
            current_taxi = None
        return current_taxi
    except ValueError:
        print("Invalid taxi choice.")


main()
