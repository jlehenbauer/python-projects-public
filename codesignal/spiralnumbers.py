#[9, 8, 7, 6, 5]      [2n-1, 2n-2, 2n-3, 2n-4, 2n-5]
#[10, 21, 20, 19, 4]  [2n, 2n+(2n+1), 2n+(2n-2), 2n+(2n-3), ]
#[11, 22, 25, 18, 3]
#[12, 23, 24, 17, 2]
#[13, 14, 15, 16, 1]



#[7,6,5,4]  [2n-1, 2n-2, 2n-3, 2n-4]
#[8,15,14,3]  [2n, 2n+(2n-1), 2n+(2n-2), 2n-(2n-3)]
#[9,16,13,2]  [2n+1, 2n+2n, 2n+(2n-3), 2n-(2n-2)]
#[10,11,12,1] [2n+2, 2n+3, 2n+4, 2n-(2n-1)]

#[3, 2]  [2n-1, 2n-2]
#[4, 1]  [2n, 2n-(2n-1)]

def spiralnumbers(s):
	a = []
	n = 1
	x = 1
	dirx = -1
	y = 1
	diry = -1

	for i in range(0, s):
		a.append([])
		for j in range(0, s):
			a[i].append(0)
	print(a)
	print('''hello''')

	while n <= s**2:
		while y%s != 0:
			a[y*diry][x*dirx] = n
			n += 1
			y += 1
		print(a)
		print(x)
		print(y)
		print(x%s)
		while x%s != 0:
			a[y*diry][x*dirx] = n
			n += 1
			x += 1
		diry *= -1

	print(a)

	
print("Please type an integer to make a square matrix")	
spiralnumbers(int(input()))