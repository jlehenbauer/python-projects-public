import sys

def howMany(start, end, step):
	start = int(start)
	end = int(end)
	step = int(step)
	count = 0
	for i in range(start, end):
		if i % step == 0:
			count += 1
	print(count)
	return count

if __name__ == "__main__":
	howMany(sys.argv[1], sys.argv[2], sys.argv[3])