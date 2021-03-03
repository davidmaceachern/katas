'''
This work is based on an optimised solution found: 
https://github.com/rsDojo/sortable-poker-hands/blob/4f476f429dc9b354db2b23b9b6052cb46d0a3f9f/daniel-nicole/python/sortable_poker_hands.py

High level design

A hand consists of cards, start by breaking down these objects into their values
then evaluate the rules that determine if one hand can beat another.
1. Parse the hand
2. Encode the values of each card
3. Identify what type of hand has been provided

Future work
- Finish understanding how the main algorithm matches the patterns of each hand
- Alternatively approach this from first principles by converting the Texas Hold'em
rules into pseudocode before converting into a potentially unoptimised Python script.
'''

class PokerHand(object):
    '''
    A poker hand can be one of the following with the lowest first:
    https://en.wikipedia.org/wiki/Texas_hold_%27em#Hand_values
    
    2: Highcard
    2: Pair
    2: Two pairs
    2: Three of a kind
    2: Straight
    2: Flush
    2: Full house
    2: Four of a kind
    1: Straight flush or Royal flush as these are the same.
    
    Start by matching a straight flush and returning a 2
    for any other type of hand. Though the hand name as a string might also 
    be required to address error TypeError: '<' not supported between instances of 'PokerHand' and 'PokerHand'
    ''' 
    def __repr__(self):  return self.hand

    def __init__(self, hand: str):
        self.hand = hand
        self.cards = [PokerCard(card) for card in hand.split(' ')]
        self.cards.sort()
        self.hand_weight = self._calculate_hand_weight()
        
    def is_suited(self):
        for i in range(len(self.cards)-1):
            if self.cards[i].suit != self.cards[i+1].suit:
                return False
        return True
    
    def _calculate_hand_weight(self):
        suited = self.is_suited()
        if suited:
            return 1
        else:
            return 2
        
class PokerCard(object):
    '''
    Returns the details about a poker card.
    
    Highest value first, the possible cards are:
    A K Q J 10 9 8 7 6 5 4 3 2
    
    A card is represented by two characters, the rank and the suit.
    
    We can generate a card weight.
    ''' 
    def __repr__(self):
        return self.card_weight
    
    def __init__(self, card: str):
        self.card = card
        self.rank = card[0]
        self.suit = card[1]
        self.card_weight = self.get_card_weight()

    def __lt__(self, other):
        '''
        Allow two instances of PokerCard to be compared in size.
        '''
        return True if self.card_weight < other.card_weight else False
            
    def get_card_weight(self):
        '''
        Determine card rank and return its relative value.
        Using ord() which when given a string representing one Unicode character, 
        return an integer representing the Unicode code point of that character
        then subtract from 63 to convert to our card weight range
        '''
        if self.rank == 'T':
            return 5
        if self.rank == 'J':
            return 4
        if self.rank == 'Q':
            return 3
        if self.rank == 'K':
            return 2
        if self.rank == 'A':
            return 1
        return (63 - ord(self.rank))
