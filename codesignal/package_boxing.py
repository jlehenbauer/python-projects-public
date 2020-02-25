"""Before delivery, all orders at Jet are packed into boxes to protect them from damage.

Consider a package pkg of a given size that needs to be packed into a box chosen from a list of available boxes. The package should fit inside the box, keeping in mind that the size of the package should not exceed the size of the box in any dimension (note that the package can be rotated to fit and it can be positioned upside down). For the sake of efficiency, among the available boxes that fit, the one with smallest volume should be chosen.

Given a package pkg and available boxes, find the 0-based index of the smallest-by-volume box such that the package fits inside it, or return -1 if there is no such box.

Example

For pkg = [4, 2, 5] and boxes = [[4, 3, 5], [5, 2, 5]], the output should be
packageBoxing(pkg, boxes) = 1.
The package fits into both boxes, but the volume of the first one (4 * 3 * 5 = 60) is greater than the volume of the second (5 * 5 * 2 = 50).

For pkg = [4, 4, 2] and boxes = [[2, 4, 4], [4, 4, 3]], the output should be
packageBoxing(pkg, boxes) = 0.
The package can fit into the first box if it is rotated, and into the second box as-is, but the first box is chosen because it has less volume overall.

For pkg = [4, 5, 3] and boxes = [[3, 10, 2], [2, 6, 7], [1, 1, 1]], the output should be
packageBoxing(pkg, boxes) = -1.
The package doesn't fit into any of the available boxes.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer pkg

Array of three positive integers denoting the size of the package as its width, height and length.

Guaranteed constraints:
1 ≤ pkg[i] ≤ 500.

[input] array.array.integer boxes

Every box is given as an array of three positive integers denoting its width, height and length.
It is guaranteed that each box has a unique volume.

Guaranteed constraints:
0 ≤ boxes.length ≤ 15,
1 ≤ boxes[i][j] ≤ 500.

[output] integer

The 0-based index of the smallest-by-volume box such that the package fits inside it, or -1 if there is no such box.
"""


def packageBoxing(pkg, boxes):
    ret = -1
    fits = 501**3
    volp, maxp, minp = pkg[0]*pkg[1]*pkg[2], max(pkg), min(pkg)
    midp = volp/(maxp*minp)
    for i, box in enumerate(boxes):
        volb, maxb, minb = box[0]*box[1]*box[2], max(box), min(box)
        midb = volb/(maxb*minb)
        if maxp <= maxb and minp <= minb and midp <= midb and volb < fits:
            fits = volb
            ret = i
        pkg.append(pkg.pop(0))
    return ret


print(packageBoxing([4, 2, 5], [[4, 3, 5], [5, 2, 5]]))
print(packageBoxing([16, 48, 91], [[23,91,82], [32,5,64], [24,29,74], [91,86,74], [64,69,59], [37,32,96], [18,14,84], [78,18,97], [50,67,37], [20,46,48], [86,29,19], [32,28,72]]))