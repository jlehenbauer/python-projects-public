def solution(A):
    total = 0
    num_eastbound = 0
    for x in A:
        if x == 0:
            num_eastbound += 1
        else:
            total += num_eastbound
        if total > 1000000000:
            return -1
    return total