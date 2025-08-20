from enum import Enum

class SuitEnum (Enum):
    @classmethod
    def items(cls):
        return list(map(lambda r: r.name, cls))

    DIAMONDS = 0
    CLUBS = 1
    HEARTS = 2
    SPADES = 3

    def __str__(self):
        return self.name.capitalize()

if __name__ == "__main__":
    pass