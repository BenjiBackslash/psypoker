from modules.hand import Hands

_occur_list_to_hand = {
    (1, 4): Hands.FOUR_OF_A_KIND,
    (2, 3): Hands.FULL_HOUSE,
    (1, 1, 3): Hands.THREE_OF_A_KIND,
    (1, 2, 2): Hands.TWO_PAIRS,
    (1, 1, 1, 2): Hands.ONE_PAIR
}


class CardRepeats(object):
    def __init__(self, cards):
        self._cards = cards
        self._repeats_dict = None

    def calc_repeats(self):
        self._repeats_dict = {}
        for c in self._cards:
            n = c.get_number()
            if n in self._repeats_dict:
                self._repeats_dict[n] += 1
            else:
                self._repeats_dict[n] = 1

    def calc_best_repeat(self):
        self.calc_repeats()
        best_repeat = Hands.HIGHEST_CARD
        occur_list = list(self._repeats_dict.values())
        occur_list.sort()
        t = tuple(occur_list)
        if t in _occur_list_to_hand:
            best_repeat = _occur_list_to_hand[t]
        return best_repeat
