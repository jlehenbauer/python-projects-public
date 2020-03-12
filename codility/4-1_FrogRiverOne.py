def solution(X, A):
    leaves = {x:0 for x in range(1, X+1)}
    leaf_positions = []
    for i, leaf in enumerate(A):
        if leaves[leaf] == 0:
            leaves[leaf] += 1
            leaf_positions.append(i)
        if len(leaf_positions) == X:
            return leaf_positions[-1]
    return -1
