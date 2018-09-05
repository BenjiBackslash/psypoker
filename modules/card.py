_to_number = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def to_number(_char):
    if _char in _to_number:
        return _to_number[_char]
    else:
        return int(_char)


class Card(object):
    def __init__(self, card_string):
        self._card_string = card_string
        self._suit = card_string[1]
        self._number = to_number(card_string[0])

    def get_suit(self):
        return self._suit

    def get_number(self):
        return self._number

    def __str__(self):
        return self._card_string
