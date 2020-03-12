def solution(A):
    sum_begin = A[0]
    sum_end = sum(x for x in A[1:])
    diff = abs(sum_begin - sum_end)
    for num in A[1:-1]:
        sum_begin += num
        sum_end -= num
        temp_diff = abs(sum_begin - sum_end)
        if temp_diff < diff:
            diff = temp_diff
    return diff