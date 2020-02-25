'''
Easy

Codewriting

300

Determine whether the given string can be obtained by one concatenation of some string to itself.

Example

For inputString = "tandemtandem", the output should be
isTandemRepeat(inputString) = true;
For inputString = "qqq", the output should be
isTandemRepeat(inputString) = false;
For inputString = "2w2ww", the output should be
isTandemRepeat(inputString) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
2 ≤ inputString.length ≤ 20.

[output] boolean

true if inputString represents a string concatenated to itself, false otherwise.
'''


def isTandemRepeat(inputString):
    for i in range(1, len(inputString)):
        if inputString[:i] == inputString[i:]:
            return True
    return False


def isTrackingTandemRepeat(inputString):
    for i in range(1, len(inputString)):
        if inputString[:i] == inputString[i:2*i]:
            word = inputString[:i]
            split_string = inputString[i:]

            while len(split_string) > 0:
                print(split_string[:i])
                if split_string[:i] == word:
                    split_string = split_string[i:]
                else:
                    break
            if len(split_string) == 0:
                return int(len(inputString)/len(word))
    return 1


print(isTandemRepeat("tandemtandem"))
print(isTrackingTandemRepeat("tandemtandem"))

print(isTandemRepeat("nonononona"))
print(isTrackingTandemRepeat("nonononano"))

print(isTandemRepeat("hellohell"))
print(isTrackingTandemRepeat("hellohell"))

print(isTandemRepeat("whynot?"))
print(isTrackingTandemRepeat("whynot?"))

isTandemRepeat("")