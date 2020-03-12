def solution(N, A):
    uses = {x:0 for x in range(1, N+2)}
    max = 0
    for x in A:
        if x > N:
            uses = {x:0 for x in range(1, N+2)}
            uses[x] += max
        else:
            uses[x] += 1
            if uses[x] > max:
                max = uses[x]
    return [uses[x] + uses[N+1] for x in range(1, N+1)]