'''
Easy

Codewriting

300

Given a string, check if it can become a palindrome through a case change of some (possibly, none) letters.

Example

For inputString = "AaBaa", the output should be
isCaseInsensitivePalindrome(inputString) = true.

"aabaa" is a palindrome as well as "AABAA", "aaBaa", etc.

For inputString = "abac", the output should be
isCaseInsensitivePalindrome(inputString) = false.

All the strings which can be obtained via changing case of some group of letters, i.e. "abac", "Abac", "aBAc" and 13 more, are not palindromes.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Non-empty string consisting of English letters.

Guaranteed constraints:
4 ≤ inputString.length ≤ 10.

[output] boolean
'''


def isCaseInsensitivePalindrome(s):
    # People should really be discouraged from writing these one-line functions.
    # They may or may not be efficient, because most use lots of slow, built-in functions.
    # In addition, they're terrible for readability.
    # It's a cool exercise, but in the working world, no one wants to read this code:
    return s[:len(s) // 2].lower() == s[(len(s) // 2) + (len(s) % 2):][::-1].lower()


print(isCaseInsensitivePalindrome("AaBaa"))

print(isCaseInsensitivePalindrome("raceCAR"))

print(isCaseInsensitivePalindrome(""))

print(isCaseInsensitivePalindrome("abca"))

print(isCaseInsensitivePalindrome("aaaaa"))

print(isCaseInsensitivePalindrome("aaaaaa"))