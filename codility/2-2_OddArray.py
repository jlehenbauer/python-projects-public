'''
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
'''
import timeit

# Better for lots of tests of smaller lists O(n**2)
def solution1(A):
    while True:
        if A[0] in A[1:]:
            x = A[0]
            A.remove(x)
            A.remove(x)
        else:
            return A[0]

# Better for bigger lists O(nlogn)
def solution2(A):
    vals = {}
    for x in A:
        if x in vals.keys():
            vals[x] += 1
        else:
            vals[x] = 1
    for key, val in vals.items():
        if val % 2 == 1:
            return key

if __name__ == "__main__":
	print(str(timeit.timeit('solution1([1, 1, 1, 1, 4, 1, 1])', setup='from __main__ import solution1', number=10000)) + " seconds")
	print(str(timeit.timeit('solution2([1, 1, 1, 1, 4, 1, 1])', setup='from __main__ import solution2', number=10000)) + " seconds")
