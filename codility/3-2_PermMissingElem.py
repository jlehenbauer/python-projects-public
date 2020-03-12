def solution(A):
    vals = {x:0 for x in range(1, len(A)+2)}
    for elem in A:
        vals[elem] += 1
    for key, val in vals.items():
        if val == 0:
            return key
    return 0