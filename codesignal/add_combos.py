"""
Codewriting

Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

Example

For a = [10, 2], the output should be concatenationsSum(a) = 1344.

a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

For a = [8], the output should be concatenationsSum(a) = 88.

There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.
"""
from itertools import product
def concatenationsSum(a):
    total = 0
    #return sum(list((int(str(pair[0]) + str(pair[1])) for pair in product(a, repeat=2))))
    for pair in product(a, repeat=2):
        total += int(str(pair[0]) + str(pair[1]))
    return total