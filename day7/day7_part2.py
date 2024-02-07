from pstats import SortKey
import pytest
from functools import cmp_to_key

class Hand:
    def __init__(self, cards, type, bid):
        self.cards = cards # list of cards in integers, A = 14, K = 13, Q = 12, J = 1, T = 10
        self.type = type # 0 = high card, 1 = one pair, 2 = two pairs, 3 = three of a kind, 4 = full house, 5 = four of a kind, 6 = Five of a kind
        self.bid = bid

    def __eq__(self, other):
        return self.cards == other.cards and self.type == other.type and self.bid == other.bid
    
    def print(self):
        print("cards: ", self.cards, ", type: ", self.type, ", bid: ", self.bid)

def compare_hands(hand1, hand2):
    if hand1.type > hand2.type:
        return 1
    elif hand1.type < hand2.type:
        return -1
    elif hand1.type == hand2.type:
        for i in range(5):
            if hand1.cards[i] > hand2.cards[i]:
                return 1
            elif hand1.cards[i] < hand2.cards[i]:
                return -1
    return 0
    
def test_compare_hands():
    hand1 = Hand([3, 2, 10, 3, 13], 1, 765)
    hand2 = Hand([10, 5, 5, 10, 5 ], 3, 684)
    print("hand1: ", hand1.cards, ", ", hand1.type, ", ", hand1.bid)
    print("hand2: ", hand2.cards, ", ", hand2.type, ", ", hand2.bid)
    assert compare_hands(hand1, hand2) == -1

    hand1 = Hand([12, 12, 12, 1, 14], 5, 483)
    hand2 = Hand([10, 5, 5, 1, 5 ], 5, 684)
    print("hand1: ", hand1.cards, ", ", hand1.type, ", ", hand1.bid)
    print("hand2: ", hand2.cards, ", ", hand2.type, ", ", hand2.bid)
    assert compare_hands(hand1, hand2) == 1

def sort_hands(hands):
    return sorted(hands, key=cmp_to_key(compare_hands))

def test_sort_hands():
    hand1 = Hand([12, 12, 12, 1, 14 ], 5, 483)
    hand2 = Hand([3, 2, 10, 3, 13], 1, 765)
    hand3 = Hand([10, 5, 5, 1, 5 ], 5, 684)
    hands = [hand1, hand2, hand3]
    print("Before sort: ", hands[0].cards, ", ", hands[1].cards, ", ", hands[2].cards)
    hands = sort_hands(hands)
    print("After sort: ", hands[0].cards, ", ", hands[1].cards, ", ", hands[2].cards)
    assert hands[0] == hand2
    assert hands[1] == hand3
    assert hands[2] == hand1

def string_to_cards(string):
    cards = []
    for char in string:
        if char == 'A':
            cards.append(14)
        elif char == 'K':
            cards.append(13)
        elif char == 'Q':
            cards.append(12)
        elif char == 'J':
            cards.append(1)
        elif char == 'T':
            cards.append(10)
        else:
            cards.append(int(char))
    return cards

def test_string_to_cards():
    assert string_to_cards("QQQJA") == [12, 12, 12, 1, 14 ]
    assert string_to_cards("32T3K") == [3, 2, 10, 3, 13]

def get_type(cards):
    savedCards = []
    found = False
    for card in cards:
        found = False
        for savedCard in savedCards:
            if savedCard[0] == card:
                place = savedCards.index(savedCard)
                nr = savedCard[1]
                savedCards[place] = (card, nr + 1)
                found = True
                break                
        if found == False:
            savedCards.append((card, 1))

    savedCards = sorted(savedCards, key=lambda x: x[1], reverse=True)

    # Place Joker (1) in best position for the hand
    nrJokers = 0
    for savedCard in savedCards:
        if savedCard[0] == 1:
            nrJokers = savedCard[1]
            savedCards.remove(savedCard)
            break

    if nrJokers == 5 or savedCards[0][1] + nrJokers == 5:
        return 6
    if savedCards[0][1] + nrJokers == 4:
        return 5
    if savedCards[0][1] + nrJokers == 3:
        if savedCards[1][1] == 2:
            return 4
        return 3
    if savedCards[0][1] + nrJokers == 2:
        if savedCards[1][1] == 2:
            return 2
        return 1
    return 0

def test_get_type():
    assert get_type([12, 12, 12, 1, 14 ]) == 5
    assert get_type([3, 2, 10, 3, 13]) == 1
    assert get_type([10, 5, 5, 1, 5 ]) == 5
    assert get_type([13, 13, 6, 7, 7 ]) == 2
    assert get_type([13, 10, 1, 1, 10 ]) == 5

def read_file(lines):
    hands = []     
    for line in lines:
        parts = line.split(" ")
        cards = string_to_cards(parts[0])
        type = get_type(cards)
        bid = int(parts[1])
        hands.append(Hand(cards, type, bid))
    return hands
    
def test_read_file():
    hand1 = Hand([3, 2, 10, 3, 13], 1, 765)
    hand2 = Hand([10, 5, 5, 1, 5 ], 5, 684)
    hand3 = Hand([13, 13, 6, 7, 7 ], 2, 28)
    hand4 = Hand([13, 10, 1, 1, 10 ], 5, 220)
    hand5 = Hand([12, 12, 12, 1, 14 ], 5, 483)

    with open('day7/test_input_day7.txt', 'r') as file:
        hands = read_file(file.readlines())

        assert hand1 == hands[0]
        assert hand2 == hands[1]
        assert hand3 == hands[2]
        assert hand4 == hands[3]
        assert hand5 == hands[4]

def test_day6_part1():
    with open('day7/test_input_day7.txt', 'r') as file:
        hands = read_file(file.readlines())
        hands = sort_hands(hands)
        totalWinnings = 0

        for i, hand in enumerate(hands):
            rank = i + 1
            totalWinnings += rank * hand.bid

        assert totalWinnings == 5905

# Main Code
with open('day7/input_day7.txt', 'r') as file:
    hands = read_file(file.readlines())
    hands = sort_hands(hands)
    totalWinnings = 0

    for i, hand in enumerate(hands):
        rank = i + 1
        totalWinnings += rank * hand.bid

    print("totalWinnings: ", totalWinnings)