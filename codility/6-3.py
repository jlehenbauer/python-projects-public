"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
"""

def solution_31pct(A):
    total = 0
    for i, r in enumerate(A):
        # Get all following disks within r
        if i + r < len(A):
            total += r
        else:
            total += len(A) - (i + 1)
        # Get new previous disks
        begin = 0 if i-r-1 < 0 else i-r-1
        if r == 0:
            begin += 1
        end = i
        #print(A[begin:end])
        for i2, r2 in enumerate(A[begin:end]):
            #print("i:" + str(i) + " r:" + str(r) + " i2:" + str(i2) + " r2:" + str(r2))
            #print("checking: {} + ({}) + {} < {})".format(r2, begin, i2, i))
            if r2 + begin + i2 < i:
                #print("Adding one")
                total += 1
    return total

def solution_not_correct(A):
    total = 0
    touched = {}
    for i, r in enumerate(A):
        #print("Add these to the circle for radius " + str(r) + " at position " + str(i))
        begin = 0 if i-r-1 < 0 else i-r-1
        end = i+r+1 if i+r+1 < len(A) else len(A)
        #print(A[begin : end])
        touched[i] = []
        for j, r2 in enumerate(A[begin : end]):
            if begin != 0:
                j += begin
            #print("Checking positions j: " + str(j) + " against i: " + str(i))
            if j > i:
                touched[i].append(j)
            elif j < i:
                if i not in touched[j]:
                    touched[i].append(j)
    #print(touched)
    return sum(len(x) for x in touched.values())

def solutionBAD(A):
    total = 0
    for i, r in enumerate(A):
        # Get all following disks within r
        if i + r < len(A):
            total += r
        else:
            total += len(A) - (i + 1)
        # Get disks behind within r (not counted previously)
        #print(i)
        #print(0 if i-r < 0 else i-r)
        for j in range((0 if i-r < 0 else i-r), i):
            #print("checking if " + str(i) + " > " + str(A[j]) + " + " + str(j))
            if i - r >= j and A[j] + j <= r:
                #print("Adding one")
                total += 1
    return total
