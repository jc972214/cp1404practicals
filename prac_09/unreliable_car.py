"""Prac 09 - Unreliable Car"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Initialise an unreliable car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Override drive method so unreliable car only drives
         when reliability is less than a random number"""
        if randint(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            print("Car was unreliable")
            return distance
