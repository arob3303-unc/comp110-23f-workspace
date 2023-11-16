"""File to define Fish class!"""


class Fish:
    """The Fish class."""
    age: int
    
    def __init__(self):
        """The Fish constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Adds age after every day."""
        self.age += 1
        return None
