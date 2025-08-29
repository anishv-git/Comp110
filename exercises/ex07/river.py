"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730773852"


class River:
    """This class creates and modifies River object."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove Fish older than 3 and Bears older than 5 from the River."""
        new_fish_list = []
        new_bear_list = []

        # Copy only fish that are age 3 or younger
        for fish in self.fish:
            if fish.age <= 3:
                new_fish_list.append(fish)

        # Copy only bears that are age 5 or younger
        for bear in self.bears:
            if bear.age <= 5:
                new_bear_list.append(bear)

        # Update the river's fish and bear lists
        self.fish = new_fish_list
        self.bears = new_bear_list

        return None

    def bears_eating(self):
        """If there are at least 5 Fish in the river, each Bear eats 3 Fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # Get's rid of 3 fish
                bear.eat(3)  # Increase bear's hunger score by 3

    def check_hunger(self):
        """For every bear, if its hunger_score is less than 0 it gets removed."""
        new_bear_list = self.bears
        i: int = 0

        for bear in new_bear_list:
            if bear.hunger_score < 0:
                self.bears.pop(i)
                i += 1

        self.bears = new_bear_list

        return None

    def repopulate_fish(self):
        """For every pair of fish, 4 more are added."""
        new_fish: int = (len(self.fish) // 2) * 4
        if (len(self.fish) / 2) >= 1:
            while new_fish > 0:
                self.fish.append(Fish())
                new_fish -= 1
        return None

    def repopulate_bears(self):
        """For every pair of fish, one more is added."""
        new_bears: int = len(self.bears) // 2
        if (len(self.bears) / 2) >= 1:
            while new_bears > 0:
                self.bears.append(Bear())
                new_bears -= 1

        return None

    def remove_fish(self, amount: int):
        """Removes the FIRST fish in the river."""
        for _ in range(amount):
            if len(self.fish) > 0:  # Check to make sure there are still fish to remove
                self.fish.pop(0)

    def view_river(self):
        """Displays fish and bear population in given format."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day for every day of the week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
