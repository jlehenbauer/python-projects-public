"""
Find number of two consecutive lists where A[:n] and A[n+1:] have the same leader.
"""

# Works, using 8-1 solution. Has to be slow as nails.
def solution(A):
    equi_leaders = 0
    for i, x in enumerate(A):
        head_leader = find_new_leader(A[:i])
        tail_leader = find_new_leader(A[i:])
        if tail_leader != -1 and head_leader != -1 and A[head_leader] == A[tail_leader + i]:
            equi_leaders += 1
            
    return equi_leaders

def solution(A):
    head_dict = {A[0]: 1}
    tail_dict = {}
    
    head_leader = (A[0], 1)
    tail_leader = None
    
    equi_leaders = 0
    
    for x in A[1:]:
        try:
            tail_dict[x] += 1
        except KeyError:
            tail_dict[x] = 1
        if tail_leader == None or tail_dict[x] > tail_leader[0]:
            tail_leader = (x, tail_dict[x])
        
    for x in A[1:]:
        if head_leader[0] == tail_leader[0]:
            equi_leaders += 1
        
        try:
            head_dict[x] += 1
        except KeyError:
            head_dict[x] = 1
            
        tail_dict[x] -= 1
        
        if head_leader[0] == x:
            head_leader[1] += 1
            
            
        if tail_leader[0] == x:
            tail_leader[1] -= 1
            
def find_new_leader(A):
    counts = {}
    for x in A:
        try:
            counts[x] += 1
        except KeyError:
            counts[x] = 1
        if counts[x] > len(A) // 2:
            return A.index(x)
    return -1