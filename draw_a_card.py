import random


def card():
	return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][random.randint(0, 12)]
	

def suit():
	return ['♠', '♦', '♥', '♣'][random.randint(0, 3)]

def print_card(card, suit):
	lines = []
	
	space = ' '
	if card == '10':
		space = ''
	
	# add the individual card on a line by line basis
	lines.append('┌─────────┐')
	lines.append('│{}{}       │'.format(card, space))  # use two {} one for char, one for space or char
	lines.append('│         │')
	lines.append('│         │')
	lines.append('│    {}    │'.format(suit))
	lines.append('│         │')
	lines.append('│         │')
	lines.append('│       {}{}│'.format(space, card))
	lines.append('└─────────┘')
	
	for line in lines:
		print(line)
		
	return True


while 1:
	times = input("How many cards would you like to draw? ")
	if times == 'exit':
		break
	for x in range(int(times)):
		print_card(card(), suit())
		print('')