import math
def rectangleRotation(a, b):
    pt = 0
    radius = pow(a/2,2)+pow(b/2,2)
    radius = int(math.ceil(pow(radius,.5)))
    
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            x = i*math.cos(math.radians(-45)) - j*math.sin(math.radians(-45))
            y = i*math.sin(math.radians(-45)) + j*math.cos(math.radians(-45))
            if -a/2<=x<=a/2 and -b/2<=y<=b/2:
                pt += 1
    return pt

















def area(a, b):
    return a*b


def my_rec_area(a, b):
    a, b = min(a, b), max(a, b)
    ahw = a/math.sqrt(2)//2
    bhw = b/math.sqrt(2)//2
    print(ahw, bhw)
    rec1 = (2*ahw+1)*(2*bhw+1)
    print(rec1)

    if (a/math.sqrt(2)/2) - (a/math.sqrt(2)//2) < .5:
        ahw -= 1
    else:
        ahw += 1
    if (b/math.sqrt(2)/2) - (b/math.sqrt(2)//2) < .5:
        bhw -= 1
    else:
        bhw += 1
    rec2 = (2*ahw)*(2*bhw)
    print(rec2)
    return rec1+rec2


a = int(input("First side: "))
b = int(input("Second side: "))
the_area = area(a, b)
rot_area = rectangleRotation(a,b)
my_area = my_rec_area(a, b)
print("My rot. rec area is " + str(my_area))
print("The rot. area is " + str(rot_area))
print("The difference is " + str(rot_area - my_area))

'''
file = open("my_rectangle_rotation.txt", "w")
for x in range(1, 51):
    for y in range(1, 51):
        file.write(str(x) + "," + str(y) + "," + str(myrecarea(x,y)) + "," + str(rectangleRotation(x,y)) + "\n")
'''
