"""File to define Fish class."""

__author__ = "730773852"


class Fish:
    """Modifies and creates Fish object."""

    age: int

    def __init__(self):
        """Contructer for Fish object."""
        self.age = 0  # sets the age to 0
        return None

    def one_day(self):
        """Increses age by 1."""
        self.age += 1
        return None
