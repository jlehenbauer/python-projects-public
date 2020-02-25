import timeit

newRoadSystemDumb = '''
def newRoadSystemDumb():
	roadRegister = [[False,False,False,False,True,True,True,True,True,True,False,True,True,True], 
 [True,False,True,True,False,True,True,True,True,False,False,True,False,False], 
 [False,False,False,True,False,False,True,True,False,True,False,True,True,False], 
 [True,True,False,False,True,True,False,False,False,True,True,True,False,True], 
 [False,True,True,True,False,True,True,True,False,False,True,False,True,False], 
 [True,True,False,True,True,False,True,False,True,True,True,True,True,True], 
 [True,False,True,True,False,True,False,False,False,False,True,True,True,True], 
 [False,True,False,True,True,False,True,False,True,True,True,True,False,False], 
 [True,True,False,False,False,True,True,True,False,False,True,True,True,True], 
 [True,False,True,False,False,True,False,True,True,False,True,False,True,True], 
 [True,True,True,True,True,True,False,True,True,True,False,True,False,False], 
 [True,True,False,False,True,True,False,False,True,True,True,False,True,True], 
 [True,True,False,False,True,True,True,True,True,False,True,False,False,False], 
 [False,False,True,True,True,True,False,False,True,True,True,False,False,False]]
	for x, y in zip(map(sum, roadRegister), map(sum, zip(*roadRegister))):
		if x != y:
			return False

	return True
'''

newRoadSystemNotDumb = '''
def newRoadSystemNotDumb():
	roadRegister = [[False,False,False,False,True,True,True,True,True,True,False,True,True,True], 
 [True,False,True,True,False,True,True,True,True,False,False,True,False,False], 
 [False,False,False,True,False,False,True,True,False,True,False,True,True,False], 
 [True,True,False,False,True,True,False,False,False,True,True,True,False,True], 
 [False,True,True,True,False,True,True,True,False,False,True,False,True,False], 
 [True,True,False,True,True,False,True,False,True,True,True,True,True,True], 
 [True,False,True,True,False,True,False,False,False,False,True,True,True,True], 
 [False,True,False,True,True,False,True,False,True,True,True,True,False,False], 
 [True,True,False,False,False,True,True,True,False,False,True,True,True,True], 
 [True,False,True,False,False,True,False,True,True,False,True,False,True,True], 
 [True,True,True,True,True,True,False,True,True,True,False,True,False,False], 
 [True,True,False,False,True,True,False,False,True,True,True,False,True,True], 
 [True,True,False,False,True,True,True,True,True,False,True,False,False,False], 
 [False,False,True,True,True,True,False,False,True,True,True,False,False,False]]
	incoming = [0 for x in roadRegister]
	outgoing = [0 for x in roadRegister]
	for i, city in enumerate(roadRegister):
		for j, road in enumerate(city):
			if road:
				outgoing[i] += 1
				incoming[j] += 1
	return all(incoming[i] == outgoing[i] for i in range(len(roadRegister)))
'''

testRoads = [[False,False,False,False,True,True,True,True,True,True,False,True,True,True], 
 [True,False,True,True,False,True,True,True,True,False,False,True,False,False], 
 [False,False,False,True,False,False,True,True,False,True,False,True,True,False], 
 [True,True,False,False,True,True,False,False,False,True,True,True,False,True], 
 [False,True,True,True,False,True,True,True,False,False,True,False,True,False], 
 [True,True,False,True,True,False,True,False,True,True,True,True,True,True], 
 [True,False,True,True,False,True,False,False,False,False,True,True,True,True], 
 [False,True,False,True,True,False,True,False,True,True,True,True,False,False], 
 [True,True,False,False,False,True,True,True,False,False,True,True,True,True], 
 [True,False,True,False,False,True,False,True,True,False,True,False,True,True], 
 [True,True,True,True,True,True,False,True,True,True,False,True,False,False], 
 [True,True,False,False,True,True,False,False,True,True,True,False,True,True], 
 [True,True,False,False,True,True,True,True,True,False,True,False,False,False], 
 [False,False,True,True,True,True,False,False,True,True,True,False,False,False]]

print(timeit.timeit(newRoadSystemDumb, number=5000))

print(timeit.timeit(newRoadSystemNotDumb, number=5000))