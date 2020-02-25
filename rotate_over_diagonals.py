'''
Rotate an n x n matrix m over it's diagonals
clockwise k times.
'''
def rotate_over_diagonals(m, k):
	n = len(m)-1

	for y in range(len(m)//2):
		for x in range(len(m)):
			if x == y or x + y == n:
				print('skipping (' + str(y) + ', ' + str(x) + ')')
				pass
			elif y < x and x + y < n:
				print('starting with (' + str(y) + ', ' + str(x) + ')')
				for i in range(k):
					temp = m[y][x]
					print('moving (' + str(x) + ', ' + str(n-y) + ') to ' + '(' + str(y) + ', ' + str(x) + ')')
					print('moving ' + str(m[x][n-y]) + ' to ' + str(m[y][x]))
					m[y][x] = m[x][n-y]
					m[x][n-y] = m[n-y][n-x]
					m[n-y][n-x] = m[n-x][y]
					m[n-x][y] = temp

	return m


def print_matrix(matrix):
	for line in matrix:
		print(line)


m3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m5x5 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

k = 1

print_matrix(m3x3)
print()
print_matrix(rotate_over_diagonals(m3x3, k))
print()
print_matrix(m5x5)
print()
print_matrix(rotate_over_diagonals(m5x5, k))

