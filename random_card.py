import random


def card():
	return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][random.randint(0, 12)]
	
def suit():
	return ['♠', '♦', '♥', '♣'][random.randint(0, 3)]

def pick_card_with_replacement(number_of_cards):
	cards = []
	
	for num in range(number_of_cards):
		cards.append((card(), suit()))

	return cards

def pick_card_without_replacement(number_of_cards):
	cards = []

	while len(cards) < number_of_cards:
		new_card = (card(), suit())
		if new_card not in cards:
			cards.append(new_card)

	return cards

def print_cards(cards):
	lines = []

	if len(cards) % 2:
	# add the individual card on a line by line basis
		while cards != []:

			space = ' '
			if cards[0][0] == '10':
				space = ''

			lines.append('┌─────────┐')
			lines.append('│{}{}       │'.format(cards[0][0], space))  # use two {} one for char, one for space or char
			lines.append('│         │')
			lines.append('│         │')
			lines.append('│    {}    │'.format(cards[0][1]))
			lines.append('│         │')
			lines.append('│         │')
			lines.append('│       {}{}│'.format(space, cards[0][0]))
			lines.append('└─────────┘')

			del cards[0]

	else:
		while cards != []:

			space1 = ' '
			if cards[0][0] == '10':
				space1 = ''
			space2 = ' '
			if cards[1][0] == '10':
				space2 = ''

			lines.append('┌─────────┐ ┌─────────┐')
			lines.append('│{}{}       │ │{}{}       │'.format(cards[0][0], space1, cards[1][0], space2))  # use two {} one for char, one for space or char
			lines.append('│         │ │         │')
			lines.append('│         │ │         │')
			lines.append('│    {}    │ │    {}    │'.format(cards[0][1], cards[1][1]))
			lines.append('│         │ │         │')
			lines.append('│         │ │         │')
			lines.append('│       {}{}│ │       {}{}│'.format(space1, cards[0][0], space2, cards[1][0]))
			lines.append('└─────────┘ └─────────┘')

			del cards[0]
			del cards[0]
	
	for line in lines:
		print(line)
		
	return True

def print_card_list(cards):
	for card in cards[:-1]:
		print(card[0] + card[1], end=", ")
	print(cards[-1][0] + cards[-1][1])

"""
TODO: 
 ///- add checks for card limits (without replacement)
 ///- add better menu for options selection

"""
while 1:
	replacement_choice = input("Would you like to draw with or without replacement? (type \'with\' or \'without\') \n")

	if replacement_choice == "exit":
		break

	display_choice = input("Would you like the cards printed or returned as a list? (type \'print\' or \'list\') \n")

	if display_choice == "exit":
		break

	elif replacement_choice == "with":
		times = input("How many cards would you like to draw? (type \'exit\' to exit) \n")
		print('')
		if times == 'exit':
			break
		if display_choice == "print":
			print_cards(pick_card_with_replacement(int(times)))
		elif display_choice == "list":
			print_card_list(pick_card_with_replacement(int(times)))
		print('')

	elif replacement_choice == "without":
		times = input("How many cards would you like to draw? (type \'exit\' to exit) \n")
		print('')
		if times == 'exit':
			break
		if display_choice == "print" and int(times) <= 52:
			print_cards(pick_card_without_replacement(int(times)))
		elif display_choice == "list" and int(times) <= 52:
			print_card_list(pick_card_without_replacement(int(times)))
		else:
			print("Please select a valid choice.")
		print('')


	else:
		print("Please select a valid choice.")