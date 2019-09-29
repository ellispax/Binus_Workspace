# -*- coding: utf-8 -*-
#card shuffle
import itertools, random
 
# make a deck of cards
cards = ['Spade', 'Hearts', 'Diamonds', 'Club']
deck = list(itertools.product([2,3,4,5,6,7,8,9,10,'King','Ace','Queen','Jack'], cards))
 
# using random function to shuffle the deck
random.shuffle(deck)
 
# draw card from user
no_of_cards = int(input("How many cards you want to display?: "))
print("You got:")
for i in range(no_of_cards):
    print(deck[i][0], "of", deck[i][1])

