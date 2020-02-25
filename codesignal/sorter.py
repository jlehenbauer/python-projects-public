def sorter1(a, b, c):
	maxN = max(a, b, c)
	minN = min(a, b, c)
	mid = [a, b, c]
	mid.remove(maxN)
	mid.remove(minN)
	return [minN, mid[0], maxN]

def sorter2(a, b, c):
	remList = [a, b, c]
	retList = []

	#Find the smallest element and add to new list
	if remList[0] < remList[1] and remList[0] < remList[2]:
		retList.append(remList[0])
	elif remList[1] < remList[0] and remList[1] < remList[2]:
		retList.append(remList[1])
	else:
		retList.append(remList[2])

	#Remove the smallest element from the originals
	remList.remove(retList[0])

	#Check the remaining and add to new list
	if remList[0] < remList[1]:
		retList.append(remList[0])
	else:
		retList.append(remList[1])

	#Remove the middle element
	remList.remove(retList[1])

	#Add the final element
	retList.append(remList[0])

	return retList



print(sorter1(4, 9, 1))

print(sorter2(3, 8, 2))