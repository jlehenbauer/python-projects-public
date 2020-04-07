""" Adapted solution from 7-1 """

def solution(S):
    stack = []
    for x in S:
        if x == '(':
            stack.append(x)
        else:
            if stack and x == ')':
                stack.pop()
            else:
                return 0
    return 0 if stack else 1