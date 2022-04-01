from turtle import *
from random import randint, randrange
#import tkinter as tk

MAX = 10
MIN = -10
PENCOLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
all_shapes = []

def main():

    screen = Screen()
    screen.setup(400, 400)
    screen.setworldcoordinates(-10, -10, 10, 10)

    colormode(255)
    pencolor(PENCOLOR)

    draw_axes()
    pencolor(randint(0, 255), randint(0, 255), randint(0, 255))

    nick_project()
    #mrl_project()
    """ 
    print(all_shapes)

    for shape in all_shapes:
        pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        reflect('x', shape) """

    screen.exitonclick()

    
def shift_pencolor(pc, shift):
    new_pc = [int(pc[0] + shift), int(pc[1] + shift), int(pc[2] + shift)]
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

def convert_points(shapes):
    local_max = 0
    for shape in shapes:
        new_max = max([x for x,y in shape] + [y for x,y in shape])
        if new_max > local_max:
            local_max = new_max

    new_shapes = []
    for shape in shapes:
        new_shape = []
        for x, y in shape:
            point = (x / local_max * MAX, y / local_max * MAX)
            new_shape.append(point)
        new_shapes.append(new_shape)
        
    return new_shapes


def draw_polygon(points):
    points.append(points[0])
    pu()
    begin_poly()
    goto(points[0])
    pd()
    for point in points[1:]:
        goto(point)
    end_poly()
    all_shapes.append(get_poly())
    return get_poly()

def translate(vector, shape, draw = True):
    new_shape = []
    for coord in shape:
        new_shape.append((coord[0] + vector[0], coord[1] + vector[1]))
    if draw: draw_polygon(new_shape)
    return new_shape

def reflect(axis, shape, draw = True):
    new_shape = []
    for coord in shape:
        if axis == 'x':
            new_shape.append((coord[0], -1 * coord[1]))
        elif axis == 'y':
            new_shape.append((-1 * coord[0], coord[1]))
    if draw: draw_polygon(new_shape)
    return new_shape

def rotate(deg, shape, dir = 'CW', draw = True):
    deg = deg % 360
    new_shape = []
    if deg == 0:
        return shape
    elif deg == 60:
        if dir == 'CW':
            for coord in shape:
                x = coord[0]/2 - coord[1]*(3**.5)/2
                y = coord[0]*3**.5/2 + coord[1]/2
                new_shape.append((x, y))
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
    if draw: draw_polygon(new_shape)
    return new_shape

def dilate(factor, shape, draw = True):
    new_shape = []
    for coord in shape:
        new_shape.append((factor * coord[0], factor * coord[1]))
    if draw: draw_polygon(new_shape)
    return new_shape
    
def nick_project():
    kite = [(4, 1),  (7, 3), (4, 9), (1, 3)]

    draw_polygon(kite)

    rotate(60, rotate(60, rotate(60, rotate(60, rotate(60, kite)))))


def mrl_project():
    pencolor(shift_pencolor(pencolor(), 110))

    rectangle = [(9, 0), (9, 2), (10, 2), (10, 0)]
    triangle = [(-2, 3), (0, 5), (2, 3)]

    draw_polygon(rectangle)
    draw_polygon(triangle)

    # Reflect Rectangle over y-axis
    opp_rect = reflect('y', rectangle)

    # Dilate Triangle with scale factor of 2, translate <0, -3>
    # Dilate Triangle with scale factor of 2, translate <-6, -3>
    # Dilate Triangle with scale factor of 2, translate <6, -3>
    translate((0, -3), dilate(2, triangle, False))
    translate((-6, -3), dilate(2, triangle, False))
    translate((6, -3), dilate(2, triangle, False))


    # Translate Rectangle <-2, 0>
    # Translate Rectangle <-4, 0>
    # Translate Rectangle <-6, 0>
    # Translate Rectangle <-8, 0>
    translate((-2, 0), rectangle)
    translate((-4, 0), rectangle)
    translate((-6, 0), rectangle)
    translate((-8, 0), rectangle)

    # Translate Opposite Rectangle <2, 0>
    # Translate Opposite Rectangle <4, 0>
    # Translate Opposite Rectangle <6, 0>
    # Translate Opposite Rectangle <8, 0>
    translate((2, 0), opp_rect)
    translate((4, 0), opp_rect)
    translate((6, 0), opp_rect)
    translate((8, 0), opp_rect)

    # Rotate Rectangle 90 CCW, translate <-5, -7>
    # Rotate Rectangle 90 CCW, translate <-3, -7>
    # Rotate Rectangle 90 CCW, translate <-1, -7>
    # Rotate Rectangle 90 CCW, translate <1, -7>
    # Rotate Rectangle 90 CCW, translate <3, -7>
    # Rotate Rectangle 90 CCW, translate <5, -7>
    # Rotate Rectangle 90 CCW, translate <7, -7>
    # Rotate Rectangle 90 CCW, translate <9, -7>
    translate((-7, -7), rotate(90, rectangle, 'CCW', False))
    translate((-5, -7), rotate(90, rectangle, 'CCW', False))
    translate((-3, -7), rotate(90, rectangle, 'CCW', False))
    translate((-1, -7), rotate(90, rectangle, 'CCW', False))
    translate((1, -7), rotate(90, rectangle, 'CCW', False))
    translate((3, -7), rotate(90, rectangle, 'CCW', False))
    translate((5, -7), rotate(90, rectangle, 'CCW', False))
    translate((7, -7), rotate(90, rectangle, 'CCW', False))
    translate((9, -7), rotate(90, rectangle, 'CCW', False))


def build_ui(window):
    label = tk.Label(text = "Trasnformation builder").pack()
    button_make_poly = tk.Button(text = "Create Polygon",
                                    width=30,
                                    height = 10,
                                    command = lambda: make_poly(entry_num_points.get())
                                    ).pack()
    entry_num_points = tk.Entry(width = 50).pack()
    window.mainloop()



if __name__ == "__main__":
    main()