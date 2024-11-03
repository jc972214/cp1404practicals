"""CP1404 Practical - Guitar"""
import datetime


class Guitar:
    """Represent guitar details"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):
        """Return a string representation of the Guitar"""
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        today = datetime.date.today()
        current_year = int(today.strftime("%Y"))
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
