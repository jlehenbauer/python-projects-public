def solution(A):
    small = 1
    for x in sorted(A):
        if x == small:
            small += 1
    return small