import sys
import math

def howMany(start, end, step):
	count = 0
	for i in range(start, end):
		if i % step == 0:
			count += 1
	return count

def solution(A, B, K):
	new_list = list(range(1, B))[K+1::K]
	return len([x for x in new_list if x >= A])

def divide(A, B, K):
	return int(round_half_up((B - A) / K))

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


if __name__ == "__main__":
	a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
	print(howMany(a, b, c))
	print(solution(a, b, c))
	print(divide(a, b, c))
