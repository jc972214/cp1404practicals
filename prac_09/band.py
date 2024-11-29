"""Prac 09 - Band Class"""

class Band:
    """Band Class"""
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        return f"{self.name} ({self.members})"

    def __repr__(self):
        return str(vars(self))

    def add(self, member):
        self.members.append(member)

    def play(self):
        for member in self.members:
            return f"{member} is playing"