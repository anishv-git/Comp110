"""File to define Bear class."""

__author__ = "730773852"


class Bear:
    """Mutating and creating the Bear object."""

    age: int
    hunger_score: int

    def __init__(self):
        """Contructer for Bear object."""
        self.age = 0
        self.hunger_score = 0

        return None

    def one_day(self):
        """Increses age by 1 and decreases hunger score by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase bear hunger score by the amount fish that is given to it."""
        self.hunger_score += num_fish
