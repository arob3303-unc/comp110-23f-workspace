"""File to define Bear class."""


class Bear:
    """Bear class."""
    age: int
    hunger_score: int

    def __init__(self):
        """The Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Adds age and deletes hunger after a day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Adds hunger after eating fish."""
        self.hunger_score += num_fish
        return None
