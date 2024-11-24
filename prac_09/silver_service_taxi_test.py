"""Prac 09 - Silver Service Taxi Test"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
    my_silver_taxi.drive(18)
    print(my_silver_taxi)
    print(my_silver_taxi.get_fare())


main()
