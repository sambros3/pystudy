import collections
from random import choice
Sard = collections.namedtuple('Sard', ['rank', 'suit'])

class Card:
    rank = ''
    suit = ''

    def __init__(self, _rank, _suit):
        self.rank = _rank
        self.suit = _suit


    def __getitem__(self, position):
        return self._cards[position]
    # def get_card_num(self, _card):
    #     ret_val = 0
    #     if(_card.rank in "2345678910"):
    #         return int(_card.rank)
    #     elif(_card.rank == 'A'):
    #         return 1
    #     elif (_card.rank == 'J'):
    #         return 11
    #     elif (_card.rank == 'Q'):
    #         return 12
    #     elif (_card.rank == 'K'):
    #         return 13
    #     else:
    #         return None


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]



beer_card  = Card('7','diamonds')
print(beer_card)

sard = Sard('7','diamonds')

print(sard)

deck = FrenchDeck()

print(deck)
print(len(deck))
for card in deck:  # doctest: +ELLPSIS
    print(card.suit+ ' '+card.rank)


# i = 0
# while i < len(deck):
# for i in range(0,52):
#     print(deck[i])

# for card in deck:  # doctest: +ELLPSIS
#     print(card)

# print(choice(deck))

# print(Card('12','hearts') in deck)

