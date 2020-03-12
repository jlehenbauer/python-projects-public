def solution(X, Y, D):
    length = Y - X
    if length % D == 0:
        return length // D
    else:
        return (length // D) + 1
