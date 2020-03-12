# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binary = bin(N)[2:]
    if binary.count('1') == len(binary) or binary.count('1') < 2:
        return 0
    zeros = binary.split('1')
    if len(zeros):
        return len(max(zeros, key=len))
    return 0