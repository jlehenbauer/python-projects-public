import random
class coin(object):
	"""docstring for coin"""
	def __init__(silverSideUp):
		super(coin).__init__()
		coin.silverSideUp = False

pile1 = []
pile2 = []
pileSize = int(random.randint(300,800))

def makePile():
	pile1.clear()
	pile2.clear()
	for i in range(0, pileSize):
		pile1.append(coin())
		i += 1

	for x in range(0, 20):
		pile1[random.randint(1,pileSize)].silverSideUp = True

	if countSilver1() != 20:
		pile1.clear()
		makePile()
	return

def splitPile(pilea, pileb):
	for i in range(0, len(pilea)//2):
		moveCoin(random.randint(0,len(pilea)-1), pilea, pileb)

def countSilver1():
	count = 0
	for i in range(0, len(pile1)):
		if pile1[i].silverSideUp:
			count += 1
	return count

def countSilver2():
	count = 0
	for i in range(0, len(pile2)):
		if pile2[i].silverSideUp:
			count += 1
	return count

def moveCoin(pos, pile1, pile2):
	pile2.append(pile1[pos])
	del pile1[pos]
	return

def flipCoin(pos, pile):
	if pile[pos].silverSideUp:
		pile[pos].silverSideUp = False
	else:
		pile[pos].silverSideUp = True
	return

def flipPile(pile):
	for i in range(0, len(pile)):
		flipCoin(i, pile)
	return

def tossCoin(pos, pile):
	if random.randint(1,2) == 1:
		pile[pos].silverSideUp = False
	else:
		pile[pos].silverSideUp = True
	return

def tossPile(pile):
	for i in range(0, len(pile)):
		tossCoin(i, pile)
	return

def printStatus():
	print("Pile 1 contains " + str(len(pile1)) + " coins")
	print("Pile 2 contains " + str(len(pile2)) + " coins")
	print("Pile 1 contains " + str(countSilver1()) + " silver coins")
	print("Pile 2 contains " + str(countSilver2()) + " silver coins")
	return

def checkSolution():
	if countSilver1() == countSilver2():
		print("Success! You've been freed!")
	else:
		print("You will rot in this dungeon forever...")

'''Make and detail original pile'''
makePile()
print("Original pile state")
print("Pile 1 contains " + str(len(pile1)) + " coins")
print("Pile 1 contains " + str(countSilver1()) + " silver coins")

'''Flip original and split - Mr. Lehenbauer's original method''
print("Flipping original pile")

flipPile(pile1)

printStatus()

print("Moving")

splitPile(pile1, pile2)

printStatus()

checkSolution()
'''


'''Try randomizing by tossing all coins in the air various times'''
'''Mr. Austin's original method''
print("Tossing all coins and splitting")
tossnum = int(input("How many tosses?"))
for i in range(0, tossnum):
	tossPile(pile1)
splitPile(pile1, pile2)
printStatus()
'''

'''Reece's Method''
flipPile(pile1)
splitPile(pile1, pile2)
flipPile(pile2)
tossPile(pile1)
tossPile(pile2)

printStatus()
checkSolution()
'''


'''Cozza's Dad's solution'''
print("Move 20 and flip all")
for x in range(0,20):
	p = random.randint(0, len(pile1)-1)
	flipCoin(p, pile1)
	moveCoin(p, pile1, pile2)

printStatus()

checkSolution()

