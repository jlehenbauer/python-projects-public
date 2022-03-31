from cmath import rect
from turtle import *
#import tkinter as tk

MAX = 10
MIN = -10
PENCOLOR = (20, 150, 60)

def main():
    #window = tk.Tk()
    #build_ui(window)

    screen = Screen()
    screen.setup(400, 400)
    screen.setworldcoordinates(-10, -10, 10, 10)

    colormode(255)
    pencolor(PENCOLOR)

    draw_axes()

    #test()
    mrl_project()

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

def mrl_project():
    pencolor(shift_pencolor(pencolor(), 75))

    rectangle = [(9, 0), (9, 2), (10, 2), (10, 0)]

    # Reflect Rectangle over y-axis
    opp_rect = reflect('y', rectangle, False)

    draw_polygon(rectangle)
    draw_polygon(opp_rect)


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


def test():

    square = [(100, 100), (100, 200), (200, 200), (200, 100)]
    triangle = [(50, 50), (200, 50), (150, 100)]
    hexagon = [(-50, -100), (-50, -200), (-100, -250), (-150, -200), (-150, -100), (-100, -50)]
    poly_list = [square, triangle, hexagon]

    for shape in poly_list:
        draw_polygon(shape)
        translate((-30, 30), shape)
        reflect('y', shape)
        rotate(90, shape)
        pencolor(shift_pencolor(pencolor(), 60))


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