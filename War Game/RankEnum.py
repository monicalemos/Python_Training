from enum import Enum

class RankEnum(Enum):
    @classmethod
    def items(cls):
        return list(map(lambda r: r.name, cls))

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __str__(self):
        return self.name.capitalize()

if __name__ == "__main__":
    pass
