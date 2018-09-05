from modules.best_hand import calc_best_combination
from modules.card import Card


def parse_input_line(line):
    parts = line.split(" ")
    cards = [Card(card_str) for card_str in parts]
    hand = cards[0:5]
    deck = cards[5:10]
    return tuple(hand), tuple(deck)


def make_result_line(hand, deck, best_combination):
    result = "Hand: "
    for c in hand:
        result += str(c)
        result += " "
    result += "Deck: "
    for c in deck:
        result += str(c)
        result += " "
    result += "Best hand: "
    result += str(best_combination)
    result += "\n"
    return result


if __name__ == "__main__":
    results = []
    with open("res/sample_input", "r") as fdr:
        lines = fdr.readlines()
    for line in lines:
        line = line.lstrip().rstrip()
        hand, deck = parse_input_line(line)
        best_combination = calc_best_combination(hand, deck)
        result_line = make_result_line(hand, deck, best_combination)
        results.append(result_line)
    with open("res/output", "wt") as fdw:
        fdw.writelines(results)




