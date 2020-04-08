"""
Find number of two consecutive lists where A[:n] and A[n+1:] have the same leader.
"""

# Works, using 8-1 solution. Has to be slow as nails.
# Complexity: O(n**2)
def O_n_squared_solution(A):
    equi_leaders = 0
    for i, x in enumerate(A):
        head_leader = find_new_leader(A[:i])
        tail_leader = find_new_leader(A[i:])
        if tail_leader != -1 and head_leader != -1 and A[head_leader] == A[tail_leader + i]:
            equi_leaders += 1
            
    return equi_leaders

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    head_dict = {A[0]: 1}
    tail_dict = {}
    
    head_len = 1
    tail_len = len(A) - 1
    
    head_leader = [A[0], 1]
    tail_leader = None
    
    equi_leaders = 0
    
    # Build the starting and ending dictionaries
    tail_dict, lead = find_new_leader(A[1:])
    
    if lead is not None:
        tail_leader = [lead, tail_dict[lead]]
            
    #print(head_dict)
    #print(head_leader)
    #print(tail_dict)
    #print(tail_leader)
    
    for i, x in enumerate(A[1:]):
        if head_leader is not None and tail_leader is not None and head_leader[0] == tail_leader[0]:
            equi_leaders += 1
            #print("At position " + str(i) + ', ' + str(head_leader) + " matched " + str(tail_leader))
        
        # Add/increment head_dict
        if x in head_dict:
            head_dict[x] += 1
        else:
            head_dict[x] = 1
            
        # Remove/decrement tail_dict
        # Note: we're moving left to right, so what
        # we're removing should always be in tail_dict
        tail_dict[x] -= 1
        
        head_len += 1
        tail_len -= 1
        # If the number we just encountered was the leader of the head,
        # increment it's count
        if head_leader is not None and x == head_leader[0]:
            head_leader[1] += 1
        # Make sure it's going to still be a leader
        if head_leader is not None and head_leader[1] < head_len // 2:
            _, lead = find_new_leader(A[:i+2])
            if lead is not None:
                head_leader = [lead, head_dict[lead]]
            else:
                head_leader = None
        
        else:
            _, lead = find_new_leader(A[:i+2])
            if lead is not None:
                head_leader = [lead, head_dict[lead]]
            else:
                head_leader = None
                
        # If the number we encountered was the leader of the tail
        # decrement it's count
        if tail_leader is not None and x == tail_leader[0]:
            tail_leader[1] -= 1
        # Make sure it's still goint to be a leader
        if tail_leader is not None and tail_leader[1] < tail_len // 2:
            _, lead = find_new_leader(A[i+2:])
            if lead is not None:
                tail_leader = [lead, tail_dict[lead]]
            else:
                tail_leader = None
            
        else:
            _, lead = find_new_leader(A[i+2:])
            if lead is not None:
                tail_leader = [lead, tail_dict[lead]]
            else:
                tail_leader = None
    
    return equi_leaders
        
    
# When necessary, find a new leader using 8-1 solution
def find_new_leader(A):
    counts = {}
    leader = None
    #print("Checking " + str(A))
    for x in A:
        try:
            counts[x] += 1
        except KeyError:
            counts[x] = 1
        if counts[x] > len(A) // 2:
            leader = x
    #print("Found leader " + str(leader))
    return (counts, leader)