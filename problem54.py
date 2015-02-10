import json
from collections import Counter
with open('p054_poker.txt') as f:
	    content = f.readlines()

class Card:
	def __init__(self, val, suit):
		self.suit 	=suit
		if val == 'J':
			self.val 	= 11
			return
		if val == 'Q':
			self.val	= 12
			return
		if val == 'K':
			self.val	= 13
			return
		if val == 'A':
			self.val	= 14
			return
		if val == 'T':
			self.val	= 10
			return
		self.val = int(val)
	def __str__(self):
		return str(self.val)+str(self.suit)+" "

class Hand:
	def __init__(self, cards):
		self.cards = sorted(cards, key=lambda card: (card.val,card.suit)  )
		self.values = set([ self.cards[0].val, self.cards[1].val, self.cards[2].val, self.cards[3].val, self.cards[4].val  ])
		self.Values = [ self.cards[0].val, self.cards[1].val, self.cards[2].val, self.cards[3].val, self.cards[4].val  ]
		self.suits = set([ cards[0].suit, cards[1].suit, cards[2].suit, cards[3].suit, cards[4].suit  ])
		self.Suits = [ cards[0].suit, cards[1].suit, cards[2].suit, cards[3].suit, cards[4].suit  ]
	def __str__(self):
		return str(self.cards[0])+str(self.cards[1])+str(self.cards[2])+str(self.cards[3])+str(self.cards[4])
	def has_royalFlush(self):
		if self.cards[0].val == 10:
			if self.Values[0]+4 == self.Values[1]+3 == self.Values[2]+2 == self.Values[3]+1 == self.Values[4]:
				if self.Suits[0]== self.Suits[1]== self.Suits[2]== self.Suits[3]== self.Suits[4]:
					return 1
		return 0

	def has_straighFlush(self):
		if self.Values[0]+4 == self.Values[1]+3 == self.Values[2]+2 == self.Values[3]+1 == self.Values[4]:
			if self.Suits[0]== self.Suits[1]== self.Suits[2]== self.Suits[3]== self.Suits[4]:
				return self.Values[0]
		return 0
	def has_fourKind(self):
		for val in self.values:
			if self.Values.count(val)==4:
				return val
		return 0
	def has_fullHouse(self):
		has_two = False
		for val in self.values:
			if self.Values.count(val)==2:		#First we check for a pair
				has_two = True
		if has_two:					#if there is a pair
			for val in self.values:			
				if self.Values.count(val)==3:	#We check for three of a kind
					return val		#We return the value of the group of three. Maybe we need to return the value of the pair
		return 0					#Else we return a 0
	def has_Flush(self):
		if len(self.suits)==1:
			return 1
		return 0
	def has_straigh(self):
		if self.Values[0]+4 == self.Values[1]+3 == self.Values[2]+2 == self.Values[3]+1 == self.Values[4]:
			return self.Values[0]
		return 0
	def has_threeKind(self):
		for val in self.values:
			if self.Values.count(val)==3:
				return val
		return 0
	def has_twotwoKind(self):
		cont =0	
		last_val = 0 
		for val in sorted(self.values):
			if self.Values.count(val)==2:
				cont+=1
				last_val=val
		if cont == 2:
			return last_val
		return 0
	def has_twoKind(self):
		for val in self.values:
			if self.Values.count(val)==2:
				return val
		return 0

	def get_points(self):
		points=[]
		points.append(self.has_royalFlush())
		points.append(self.has_straighFlush())
		points.append(self.has_fourKind())
		points.append(self.has_fullHouse())
		points.append(self.has_Flush())
		points.append(self.has_straigh())
		points.append(self.has_threeKind())
		points.append(self.has_twotwoKind())
		points.append(self.has_twoKind())
		# The 2 highest values
		single_val =  [k for k,v in Counter(self.Values).items() if v==1]
		single_val = sorted(self.Values)
		if len(single_val)>0:
			points.append(self.Values[-1])
		if len(single_val)>1:
			points.append(self.Values[-2])
		return points


		

import time
start=time.time()

counter =0 
for hand in content:
	hand  = hand.replace('\n','')
	cards = hand.split(' ')
	Cards = []
	for card in cards:
		Cards.append(Card(card[0],card[1]))
	hand1 = Hand(Cards[:5])
	hand2 = Hand(Cards[5:])

	for h1, h2 in zip(hand1.get_points() ,hand2.get_points()):
		if h1 > h2:
			counter+=1
			break
		if h2 > h1:
			break

the_ans=counter
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
