# -*- coding: utf-8 -*-

"""Playing cards module for teaching loops"""
import random
from typing import List, Tuple

suit_symbols = {"clubs": "♣", "diamonds": "♦", "hearts": "♥", "spades": "♠"}
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    """
    Class describing playing card objects
    """
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = ranks.index(rank)+1
    def __repr__(self):
        return f"{suit_symbols[self.suit]}{self.rank}"
    def __gt__(self, other): 
        if(self.value>other.value): 
            return True
        else: 
            return False

"""
Function to get an ordered full 52-card deck
"""
def full_deck()-> List[Card]:
    deck = []
    for suit in suit_symbols.keys():
        for rank in ranks:
            deck.append(Card(suit,rank))
    return deck

def deck_from_list(input: List[Tuple])->List[Card]:
    return [Card(*card) for card in input]

"""
Function to shuffle deck of cards (list of Card objects) 
"""
def shuffle(deck: List[Card]) -> List[Card]:
    for i,card in enumerate(deck):
        r = random.randint(0,len(deck)-1)
        deck[r],deck[i] = deck[i],deck[r]
    return deck

# Get a small random deck
def small_random_deck(size: int) -> List[Card]:
    deck = full_deck().copy()
    if size>52: size=52
    return shuffle(deck)[:size]

# Get a small random deck that is guaranteed to have at least one heart and one diamond
def safe_small_random_deck(size: int) -> List[Card]:
    deck = full_deck().copy()
    if size>52: size=52
    subdeck = shuffle(deck)[:size]
    has_hearts = False
    has_diamonds = False
    for c in subdeck:
        if c.suit == 'hearts':
            has_hearts = True
        elif c.suit == 'diamonds':
            has_diamonds = True
        if has_hearts and has_diamonds:
            break
    if not has_hearts:
        if subdeck[0].suit != 'diamonds':
            subdeck[0] = Card('hearts', ranks[random.randint(0,len(ranks)-1)])
        else:
            subdeck[1] = Card('hearts', ranks[random.randint(0,len(ranks)-1)])
    if not has_diamonds:
        if subdeck[0].suit != 'hearts':
            subdeck[0] = Card('diamonds', ranks[random.randint(0,len(ranks)-1)])
        else:
            subdeck[1] = Card('diamonds', ranks[random.randint(0,len(ranks)-1)])
    shuffle(subdeck)
    return subdeck

# add card to a deck, useful for testing (not destructive)
def insert_card(deck : List[Card], rank : int, suit: str, index : int =random.random() ) -> List[Card]:
    new_deck = deck.copy()
    new_card = Card(suit, rank)
    first_half = new_deck[:index]
    second_half = new_deck[index:]
    first_half.append(new_card)
    out_deck = first_half + second_half
    return out_deck

