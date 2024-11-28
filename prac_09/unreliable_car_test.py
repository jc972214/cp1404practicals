"""Prac 09 - Unreliable Car Test"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test Functionality of Unreliable Car Subclass"""
    my_unreliable_car = UnreliableCar("Honda Jazz", 100, 50)
    my_unreliable_car.drive(100)
    print(my_unreliable_car)


main()
