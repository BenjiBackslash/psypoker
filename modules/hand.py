from enum import Enum


class Hands(Enum):
    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGHEST_CARD = 1

    def __str__(self):
        return self.name.replace("_", "-").lower()
