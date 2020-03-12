def solution(N, A):
    solution = [0 for x in range(1, N+1)]
    current_max = 0
    add_max = 0
    for x in A:
        if x > N:
            add_max = current_max
        elif solution[x-1] < add_max:
            solution[x-1] = add_max
        if x <= N:
            solution[x-1] += 1
            if solution[x-1] > current_max:
                current_max = solution[x-1]
    for i in range(len(solution)):
        if solution[i] < add_max:
            solution[i] = add_max
    return solution