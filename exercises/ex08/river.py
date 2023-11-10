"""File to define River class!"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730717463"


class River:
    """This is the beginning of the River Class."""
    # Class attributes
    day: int
    week: int
    bears: list()
    fish: list()
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        # Constructor variables
        self.day: int = 0
        self.week: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals on age year."""
        # new lists, so constructor list does not change during loop
        fish_list: list[Fish] = self.fish
        bear_list: list[Bear] = self.bears

        # loops to check fish age
        for fish in self.fish:
            if fish.age > 3:
                fish_list.pop(0)

        # loops to check bear age
        for bear in self.bears:
            if bear.age > 5:
                bear_list.pop(0)

        # updates old list with new list
        self.fish = fish_list
        self.bears = bear_list
        return None

    def bears_eating(self):
        """The function that controls how much the bears eat."""
        # loops to feed bear, and remove fish (food)
        for bear in self.bears:
            if len(self.fish) > 5:
                bear.eat(3)  # adds 3 hunger
                self.remove_fish(3)  # removes 3 fish from river
            else:  # if there are less than 5 fish in river, bear does not eat
                return None
        return None
    
    def check_hunger(self):
        """Kills off a bear if hunger hits negative."""
        # new list, so list during loop does not get altered
        new_l: list[Bear] = self.bears
        # loops thru to check hunger score for bear
        for bear in self.bears:
            if bear.hunger_score < 0:
                new_l.pop(0)  # removes bear if less than zero hunger
        self.bears = new_l
        return None
        
    def repopulate_fish(self):
        """Adds more fish into the river."""
        # variables
        total_fish: int = len(self.fish)  # total amount of fish in river
        new_fish: Fish = Fish()  # creates a new fish
        fish_list: list[Fish] = self.fish  # new list for loop

        # loop that adds 4 fish for every 2 in river
        for fish in self.fish:
            if total_fish >= 2:
                total_fish -= 2
                fish_list.append(new_fish)
                fish_list.append(new_fish)
                fish_list.append(new_fish)
                fish_list.append(new_fish)
                
        self.fish = fish_list
        return None
    
    def repopulate_bears(self):
        """Adds more bears into the river population."""
        # variables
        total_bears: int = len(self.bears)  # total amount of bears
        new_bear: Bear = Bear()  # create new bear
        new_bear_list: list[Bear] = self.bears  # for loop

        # loop adds a new bear for every 2 bears already in river
        for bear in self.bears:
            if total_bears >= 2:
                total_bears -= 2
                new_bear_list.append(new_bear)

        self.bears = new_bear_list
        return None
    
    def remove_fish(self, amount: int):
        """Removes the fish."""
        # new list for loop purposes
        new_fish_idx: list[Fish] = self.fish
        # idx
        i: int = 0
        while i < amount:
            new_fish_idx.pop(0)
            i += 1
        self.fish = new_fish_idx
        return None

    def view_river(self):
        """Let's user view river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
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
        """Simulate one week of life in the river."""
        # increase the week by 1
        self.week += 1
        # idx
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
            print(self.day)
        return None
