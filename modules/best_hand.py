from modules.hand import Hands
from modules.calc_hand import CalcHand
import itertools


def calc_best_combination(hand, deck):
    current_best_hand = Hands.HIGHEST_CARD
    for j in range(len(deck) + 1):
        deck_pick = deck[0:j]
        for hand_pick in itertools.combinations(hand, len(deck) - j):
            option_hand = CalcHand(hand_pick + deck_pick).calc_hand()
            if option_hand.value == Hands.STRAIGHT_FLUSH.value:
                return Hands.STRAIGHT_FLUSH
            elif option_hand.value > current_best_hand.value:
                current_best_hand = option_hand
    return current_best_hand
