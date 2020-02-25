import msvcrt
import colorama
import os
from time import sleep
from colorama import Fore, Back, Style
from random import choice
import winsound

def big_digits():
	colorama.init()
	zero = [
'     000000000     ',
'   00:::::::::00   ',
' 00:::::::::::::00 ',
'0:::::::000:::::::0',
'0::::::0   0::::::0',
'0:::::0     0:::::0',
'0:::::0     0:::::0',
'0:::::0     0:::::0',
'0:::::0     0:::::0',
'0:::::0     0:::::0',
'0:::::0     0:::::0',
'0::::::0   0::::::0',
'0:::::::000:::::::0',
' 00:::::::::::::00 ',
'   00:::::::::00   ',
'     000000000     ']

	one = [
'      1111111      ',
'     1::::::1      ',
'    1:::::::1      ',
'    111:::::1      ',
'       1::::1      ',
'       1::::1      ',
'       1::::1      ',
'       1::::l      ',
'       1::::l      ',
'       1::::l      ',
'       1::::l      ',
'       1::::l      ',
' 111111::::::111111',
' 1111::::::::::1111',
' 1::::::::::::::::1',
' 111111111111111111']

	two = [
' 22222222222222    ',
'2::::::::::::::22  ',
'2:::::222222:::::2 ',
'222222     2:::::2 ',
'           2:::::2 ',
'           2:::::2 ',
'        2222::::2  ',
'   22222::::::22   ',
' 22::::::::222     ',
' 2::::22222        ',
'2::::2             ',
'2::::2             ',
'2::::2       222222',
'2:::::2222222:::::2',
'2:::::::::::::::::2',
'2222222222222222222']

	three = [
' 333333333333333   ',
'3:::::::::::::::33 ',
'3::::::33333::::::3',
'3333333     3:::::3',
'            3:::::3',
'            3:::::3',
'    33333333:::::3 ',
'    3:::::::::::3  ',
'    33333333:::::3 ',
'            3:::::3',
'            3:::::3',
'            3:::::3',
'3333333     3:::::3',
'3::::::33333::::::3',
'3:::::::::::::::33 ',
' 333333333333333   ']

	four = [
'       4444444444  ',
'      4:::::::::4  ',
'     4::::::::::4  ',
'    4::::44:::::4  ',
'   4::::4 4:::::4  ',
'  4::::4  4:::::4  ',
' 4::::4   4:::::4  ',
'4::::444444:::::444',
'4:::::::::::::::::4',
'4444444444::::::444',
'          4:::::4  ',
'          4:::::4  ',
'          4:::::4  ',
'        44:::::::44',
'        4:::::::::4',
'        44444444444']

	five = [
'555555555555555555 ',
'5::::::::::::::::5 ',
'5::::::::::::::::5 ',
'5:::::555555555555 ',
'5:::::5            ',
'5:::::5            ',
'5:::::5555555555   ',
'5:::::::::::::::5  ',
'555555555555:::::5 ',
'            5:::::5',
'            5:::::5',
'5555555     5:::::5',
'5::::::55555::::::5',
' 55:::::::::::::55 ',
'   55:::::::::55   ',
'     555555555     ']

	six = [
'        66666666   ',
'       6::::::6    ',
'      6::::::6     ',
'     6::::::6      ',
'    6::::::6       ',
'   6::::::6        ',
'  6::::::6         ',
' 6::::::::66666    ',
'6::::::::::::::66  ',
'6::::::66666:::::6 ',
'6:::::6     6:::::6',
'6:::::6     6:::::6',
'6::::::66666::::::6',
' 66:::::::::::::66 ',
'   66:::::::::66   ',
'     666666666     ']

	seven = [
'7777777777777777777',
'7:::::::::::::::::7',
'7:::::::::::::::::7',
'777777777777::::::7',
'           7::::::7',
'          7::::::7 ',
'         7::::::7  ',
'        7::::::7   ',
'       7::::::7    ',
'      7::::::7     ',
'     7::::::7      ',
'    7::::::7       ',
'   7::::::7        ',
'  7::::::7         ',
' 7::::::7          ',
'77777777           ']

	eight = [
'     888888888     ',
'   88:::::::::88   ',
' 88:::::::::::::88 ',
'8::::::88888::::::8',
'8:::::8     8:::::8',
'8:::::8     8:::::8',
' 8:::::88888:::::8 ',
'  8:::::::::::::8  ',
' 8:::::88888:::::8 ',
'8:::::8     8:::::8',
'8:::::8     8:::::8',
'8:::::8     8:::::8',
'8::::::88888::::::8',
' 88:::::::::::::88 ',
'   88:::::::::88   ',
'     888888888     ']

	nine = [
'     999999999     ',
'   99:::::::::99   ',
' 99:::::::::::::99 ',
'9::::::99999::::::9',
'9:::::9     9:::::9',
'9:::::9     9:::::9',
' 9:::::99999::::::9',
'  99::::::::::::::9',
'    99999::::::::9 ',
'         9::::::9  ',
'        9::::::9   ',
'       9::::::9    ',
'      9::::::9     ',
'     9::::::9      ',
'    9::::::9       ',
'   99999999        ']


	# Fore, Back and Style are convenience classes for the constant ANSI strings that set
	#     the foreground, background and style. The don't have any magic of their own.
	FORES = [ Fore.GREEN, Fore.YELLOW, Fore.WHITE ]
	BACKS = [ Back.BLACK, Back.RED, Back.BLUE, Back.MAGENTA, Back.CYAN ]
	STYLES = [ Style.BRIGHT ]

	numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
	count_p1 = 0
	count_p2 = 0
	min_y, max_y = 1, 100
	min_x, max_x = 2, 100
	clear = lambda: os.system('cls')
	pos = lambda y, x: '\x1b[%d;%dH' % (y, x)

	clear()
	print('%s%s%s%s%s' %(pos(min_y, min_x), 'Hello! please choose one of the options to get started.', choice(FORES), choice(BACKS), choice(STYLES)))
	print('%s%s%s%s%s' %(pos(min_y+1, min_x), 'c: Countdown (shows remaining time in seconds)', choice(FORES), choice(BACKS), choice(STYLES)))
	print('%s%s%s%s%s' %(pos(min_y+2, min_x), 's: Scoreboard (use \'f\' and \'j\' to keep score)', choice(FORES), choice(BACKS), choice(STYLES)))
	print('%s%s%s%s%s' %(pos(min_y+3, min_x), 't: Timer (counts in seconds)', choice(FORES), choice(BACKS), choice(STYLES)))
	print('%s%s%s%s%s' %(pos(min_y+4, min_x), 'q: Quit (can also be used during any program)', choice(FORES), choice(BACKS), choice(STYLES)))
	#print('%s%s%s%s%s' %(pos(min_y, min_x), 'c: Change text styles (can also be used during any program)', choice(FORES), choice(BACKS), choice(STYLES)))


	while True:
		if msvcrt.kbhit():
			key = msvcrt.getch()
			if 47 < ord(key) < 58:
				print_pressed_number(pos, min_y, min_x, numbers, key)
			if ord(key) == ord('c'):
				key = run_countdown(pos, min_y, min_x, numbers, clear)
			if ord(key) == ord('s'):
				key = scoreboard(numbers, count_p1, count_p2, min_y, min_x, max_y, max_x, clear, pos)
			if ord(key) == ord('t'):
				key = run_timer(pos, min_y, min_x, numbers, clear)
			if ord(key) == ord('q'):
				print('%s%s' % (Fore.GREEN, Back.BLACK))
				clear()
				print('Exiting...')
				break

	

def scoreboard(numbers, count_p1, count_p2, min_y, min_x, max_y, max_x, clear, pos):
	clear()
	print('Scoreboard running. Use \'f\' and \'j\' to increment score.')
	while True:
		if msvcrt.kbhit():
			key = msvcrt.getch()
			if ord(key) == ord('f'):
				count_p1 += 1
			if ord(key) == ord('j'):
				count_p2 += 1
			if ord(key) == ord('q'):
				clear()
				print('Exiting...')
				return 'q'
			clear()
			print('Scoreboard running. Use \'f\' and \'j\' to increment score.')
			display_p1_score(pos, min_y+1, min_x, numbers, count_p1)
			display_p2_score(pos, min_y+1, max_x, numbers, count_p2)

def print_pressed_number(pos, min_y, min_x, numbers, key):
	print('%s%s' % (pos(min_y+1, min_x), numbers[ord(key)-48]), end='')

def display_p1_score(pos, y, x, numbers, count):
	if count > 9:
		digit = 0
		for nums in str(count):
			for line in range(len(numbers[int(nums)])):
				print('%s%s' % (pos(y+line+1, x+25*digit), numbers[int(nums)][line]), end='')
			digit += 1
	else:
		for line in range(len(numbers[count])):
			print('%s%s' % (pos(y+line+1, x), numbers[count][line]), end='')

def display_p2_score(pos, y, x, numbers, count):
	if count > 9:
		digit = 0
		for nums in str(count):
			for line in range(len(numbers[int(nums)])):
				print('%s%s' % (pos(y+line+1, x+25*digit), numbers[int(nums)][line]), end='')
			digit += 1
	else:
		for line in range(len(numbers[count])):
			print('%s%s' % (pos(y+line+1, x), numbers[count][line]), end='')

def run_timer(pos, y, x, numbers, clear):
	clear()
	print('Timer running, counting in seconds. Press \'q\' to quit.')
	count = 0
	while True:
		if msvcrt.kbhit():
			key = msvcrt.getch()
			if ord(key) == ord('q'):
				return 'q'
		if count > 9:
			digit = 0
			for nums in str(count):
				for line in range(len(numbers[int(nums)])):
					print('%s%s' % (pos(y+line+1, x+25*digit), numbers[int(nums)][line]), end='')
				digit += 1
		else:
			for line in range(len(numbers[count])):
				print('%s%s' % (pos(y+line+1, x), numbers[count][line]), end='')	
		sleep(1)
		count += 1

def run_countdown(pos, y, x, numbers, clear):
	got_time = True
	count = 0
	clear()
	while got_time:
		try:
			count = int(input('How many seconds would you like the countdown to run?'))
			got_time = False
		except:
			print('Please enter a valid number of seconds')
	clear()
	print('Countdown running, counting in seconds. Press \'q\' to quit.')
	places = len(str(count))
	while True:
		if places > len(str(count)):
			clear()
			places = len(str(count))
		if count == 0:
			duration = 5000  # milliseconds
			freq = 440  # Hz
			winsound.Beep(freq, duration)
			return 'q'
		if msvcrt.kbhit():
			key = msvcrt.getch()
			if ord(key) == ord('q'):
				return 'q'
		if count > 9:
			digit = 0
			for nums in str(count):
				for line in range(len(numbers[int(nums)])):
					print('%s%s' % (pos(y+line+1, x+25*digit), numbers[int(nums)][line]), end='')
				digit += 1
		else:
			clear()
			for line in range(len(numbers[count])):
				print('%s%s' % (pos(y+line+1, x), numbers[count][line]), end='')	
		sleep(1)
		count -= 1




big_digits()
