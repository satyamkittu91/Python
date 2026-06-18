import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        '''Initialize a standard deck of 52 playing cards.
        uses loops for clarity, but list comprehensions are more concise and faster.
        '''
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        '''Return the number of cards in the deck.
        simple len function can be used as the deck is stored as a list in self._cards.
        '''
        return len(self._cards)

    def __getitem__(self, position):
        '''Return the card at the given position.'''
        
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])

from random import choice
print(choice(deck))

print(deck[:3])
print(deck[12::13])

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

# sorting
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    """
    Return a numeric value for sorting a card so that spades rank highest.

    The score is computed from the index of the card's rank in FrenchDeck.ranks,
    scaled by the number of suits, and offset by the card's suit value from
    suit_values.

    Parameters
    ----------
    card : object
        A card object with `rank` and `suit` attributes.

    Returns
    -------
    int
        A sorting key where higher values represent cards that should come later,
        with cards of the spades suit ordered above the others.
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]