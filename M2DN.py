import sys

def ones(first, second):
	print("Multiply the ones digit in " + str(first) + " by the ones digit in " + str(second))

	ones_product = int(input(str(first%10) + " x " + str(second%10) + " = "))

	if (ones_product == (first%10)*(second%10)):
		print("Great job! It was " + str(ones_product))
		print()
	else:
		print("Oops! Try again!")
		print("...")
		print("..")
		print(".")
		onesa(first, second)

def onesa(first, second):
	print("Multiply the ones digit in " + str(first) + " by the tens digit in " + str(second))

	onesa_product = int(input(str(first%10) + " x " + str(second-second%10) + " = "))

	if (onesa_product == (first%10)*(second-second%10)):
		print("Great job! It was " + str(onesa_product))
		print()
	else:
		print("Oops! Try again!")
		print("...")
		print("..")
		print(".")
		onesa(first, second)

	print("Multiply the tens digit in " + str(first) + " by the ones digit in " + str(second))

def onesb(first, second):
	onesb_product = int(input(str(first-first%10) + " x " + str(second%10) + " = "))

	if (onesb_product == (first-first%10)*(second%10)):
		print("Great job! It was " + str(onesb_product))
		print()
	else:
		print("Oops! Try again!")
		print("...")
		print("..")
		print(".")
		onesb(first, second)

	print("Multiply the tens digit in " + str(first) + " by the tens digit in " + str(second))

def tens(first, second):
	tens_product = int(input(str(first-first%10) + " x " + str(second-second%10) + " = "))

	if (tens_product == (first-first%10)*(second-second%10)):
		print("Great job! It was " + str(tens_product))
		print()
	else:
		print("Oops! Try again!")
		print("...")
		print("..")
		print(".")
		tens(first, second)

def addup(first, second):
	print("Now, add all those together")

	result = int(input("What did you get? "))

	if result == first*second:
		print("Correct! It was " + str(first*second) + ".")

	else:
		print("Oops! Try again!")
		print("...")
		print("..")
		print(".")
		addup(first, second)

def main():
	print("What two 2-digit numbers do you want to multiply?")
	first = int(input("First number: "))
	second = int(input("Second number: "))

	ones(first, second)

	onesa(first, second)

	onesb(first, second)

	tens(first, second)

	addup(first, second)

	print("Well done, you've learned to multiply two digit numbers!")
	exit()


main()