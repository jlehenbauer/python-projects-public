def solution(A):
    for i, x in enumerate(sorted(A)):
        if x != i + 1:
            return 0
    return 1