def diafill(m, n):
	if m == 1 or n == 1:
		return m*n
	elif m == n:
		print(3*n-2)
		return 3*n-2
	else:
		m, n = max(m, n), min(m, n)
		total = 0
		for x in range(1, m+1):
			print(str((n*x)%m) + "/" + str(m))
			if n/m <= ((n*x)%m)/m:
				print("so add 1")
				total += 1
			elif n*x == n*m:
				print("so add 1 and finish")
				total += 1
				print(total)
				return total
			elif (n*x)%m == 0:
				print("so add 3")
				total += 3
			else:
				print("so add 2")
				total += 2
	print(total)
	return total
	
diafill(int(input("What is m? ")), int(input("What is n? ")))