from functools import reduce
def fibonacci(n):
	b = [1, 2, 3, 4]
	print(reduce(lambda x, y: x + y, range(n)))

	print(list([0] * x for x in reduce(lambda a, b: a + [a[-1] + a[-3]], range(n-2), [0, 0, 1])))

fibonacci(int(input("Give a number: ")))