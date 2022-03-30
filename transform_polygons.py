from turtle import *
MAX = 300
MIN = -300
PENCOLOR = (20, 150, 60)

def main():
    screen = Screen()
    colormode(255)
    pencolor(PENCOLOR)

    draw_axes()

    mrl_project()

    screen.exitonclick()

def mrl_project():

    square = [(100, 100), (100, 200), (200, 200), (200, 100)]
    triangle = [(50, 50), (200, 50), (150, 100)]
    poly_list = [square, triangle]

    for shape in poly_list:
        draw_polygon(shape)
        translate((-30, 30), shape)
        reflect('y', shape)
        rotate(90, shape)
        pencolor(shift_pencolor(pencolor(), 60))

def shift_pencolor(pc, shift):
    new_pc = [int(pc[0] + shift), int(pc[1] + shift), int(pc[2] + shift)]
    print(new_pc)
    for i in range(len(new_pc)):
        if new_pc[i] > 255:
            new_pc[i] = new_pc[i] % 255
    return tuple(new_pc)




def draw_axes():
    pu()
    goto(0, MAX)
    pd()
    goto(0, MIN)
    pu()
    goto(MAX, 0)
    pd()
    goto(MIN, 0)

def draw_polygon(points):
    points.append(points[0])
    pu()
    begin_poly()
    goto(points[0])
    pd()
    for point in points[1:]:
        goto(point)
    end_poly()
    return get_poly()

def translate(vector, shape):
    new_shape = []
    for coord in shape:
        new_shape.append((coord[0] + vector[0], coord[1] + vector[1]))
    draw_polygon(new_shape)
    return new_shape

def reflect(axis, shape):
    new_shape = []
    for coord in shape:
        if axis == 'x':
            new_shape.append((coord[0], -1 * coord[1]))
        elif axis == 'y':
            new_shape.append((-1 * coord[0], coord[1]))
    draw_polygon(new_shape)
    return new_shape

def rotate(deg, shape, dir = 'CW'):
    deg = deg % 360
    new_shape = []
    if deg == 0:
        return shape
    elif deg == 180:
        for coord in shape:
            new_shape.append((-1 * coord[0], -1 * coord[1]))
    elif deg == 90:
        if dir == 'CW':
            for coord in shape:
                new_shape.append((coord[1], -1 * coord[0]))
        elif dir == 'CCW':
            for coord in shape:
                new_shape.append((-1 * coord[1], coord[0]))
    draw_polygon(new_shape)
    return new_shape





if __name__ == "__main__":
    main()