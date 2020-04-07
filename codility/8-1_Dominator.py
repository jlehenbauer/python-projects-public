"""
Return the minimum index of a number that exists in more than half of the array, or -1 if no such number exists.
"""
def solution(A):
    counts = {}
    for x in A:
    	# Both this solution and 'if x in counts' complete this task with adequate performance
    	# TODO: test which is faster (assumption: try/except, since it doesn't have to look through keys)
        try:
            counts[x] += 1
        except KeyError:
            counts[x] = 1
        if counts[x] > len(A) // 2:
            return A.index(x)
    return -1