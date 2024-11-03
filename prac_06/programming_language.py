"""
CP1404 Practical 6 - Programming Languages
Expected Time to Solve: 30 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language"""

    def __init__(self, name, typing, reflection, date):
        """Construct a Programming Language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.date = date

    def __str__(self):
        """Return a string representation of a Programming Language"""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.date}"

    def is_dynamic(self):
        """Determine if a Programming Language is dynamic"""
        return self.typing == 'Dynamic'
