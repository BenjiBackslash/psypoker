from modules.hand import Hands
from modules.calc_repeats import CardRepeats


class CalcHand(object):
    def __init__(self, cards):
        self._cards = cards

    def is_flush(self):
        return len(set([c.get_suit() for c in self._cards])) == 1

    def _check_straight(self,numbers):
        for i in range(1, len(numbers)):
            if numbers[i]-numbers[i-1] != 1:
                return False
        return True

    def is_straight(self):
        numbers = [c.get_number() for c in self._cards]
        numbers.sort()
        sequences = [numbers]
        if numbers[-1] == 14 and not numbers[-2] == 14:
            ace_as_1_seq = [1]
            for n in numbers[0:4]:
                ace_as_1_seq.append(n)
            sequences.append(ace_as_1_seq)
        return any([self._check_straight(seq) for seq in sequences])

    def calc_hand(self):
        is_straight = self.is_straight()
        is_flush = self.is_flush()

        if is_straight:
            if is_flush:
                return Hands.STRAIGHT_FLUSH

        best_flush = Hands.HIGHEST_CARD
        best_straight = Hands.HIGHEST_CARD
        if is_straight:
            best_straight = Hands.STRAIGHT
        elif is_flush:
            best_flush = Hands.FLUSH

        best_repeat = CardRepeats(self._cards).calc_best_repeat()

        return max(best_straight, best_flush, best_repeat, key=lambda h: h.value)
