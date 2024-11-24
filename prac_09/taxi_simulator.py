"""Prac 09 - Taxi Simulator"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower().strip()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
        else:
            print("invalid")
        print(MENU)
        choice = input(">>> ").lower().strip()


def display_taxis(taxis):
    print("Taxis available:")
    for count, taxi in enumerate(taxis):
        print(f"{count} - {taxi}")


main()
