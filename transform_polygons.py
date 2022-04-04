from turtle import *
from random import randint, randrange
#import tkinter as tk

MAX = 20
MIN = -20
PENCOLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
all_shapes = []

def main():

    screen = Screen()
    screen.setup(400, 400)
    screen.setworldcoordinates(MIN, MIN, MAX, MAX)

    colormode(255)
    pencolor(PENCOLOR)

    draw_axes()
    pencolor(randint(0, 255), randint(0, 255), randint(0, 255))

    #nick_project()
    #preston_project()
    #alden_project()
    #aiden_project()
    tyson_project()
    #example()
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
    shape_A = [ (3,0), (0.45,-6), (3,-8), (6.45,-6) ]

    draw_polygon(shape_A)

    shape_B = rotate(60, shape_A)

    shape_C = rotate(60, shape_B)

    shape_D = rotate(60, shape_C)

    shape_E = rotate(60, shape_D)

    shape_F = rotate(60, shape_E)

    reflect( 'x' , shape_A)

    reflect( 'x' , shape_B)

    reflect( 'x' , shape_C)

    reflect( 'x' , shape_D)

    reflect( 'x' , shape_E)

    reflect( 'x' , shape_F)

def preston_project():
    Rec1 = [(0, 0), (1, 0), (1,1),(0, 1)]
    Rec2 = [(0, 0), (2, 0), (2, 1), (0, 1)]
    Rec4 = [(0, 0), (4,0), (4, 1), (0, 1)]
    Rec5 = [(0, 0), (5,0), (5, 1), (0, 1)]
    Rec6 = [(0, 0), (6,0), (6, 1), (0, 1)]
    Rec7 = [(0, 0), (7,0), (7, 1), (0, 1)]
    Rec8 = [(0, 0), (8,0), (8, 1), (0, 1)]

    draw_polygon(Rec1)
    draw_polygon(Rec2)
    draw_polygon(Rec4)
    draw_polygon(Rec5)
    draw_polygon(Rec6)
    draw_polygon(Rec7)
    draw_polygon(Rec8)


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

def example():
    shape1 = [(1, 2), (3, 5), (-3, -2)]
    shape2 = [(3, 4), (-1, -3), (-4, -6), (-2, 4)]



    translate((-3, 4), shape1)

    dilate(2, shape2)

    rotate(180, shape1)

    reflect('y', shape2)

def alden_project():
    """
    Picture created exactly as planned!
    4 figures, translations and reflections used, no rotations.
    90%
    """
    Squair = [(2, 10), (4, 10), (4, 8), (2, 8)]
    Rectangle = [(4, -1), (6, -1), (6, 3), (4, 3)]
    Triangle = [(4, -1), (6, -1), (4, -3)]

    Squair2 = reflect('y', Squair)

    draw_polygon(Squair)
    draw_polygon(Rectangle)
    draw_polygon(Triangle)

    translate((0, -2), Squair)
    translate((-2, -2), Squair)
    translate((0, -4), Squair)
    translate((2, -2), Squair)

    translate((0, -2), Squair2)
    translate((-2, -2), Squair2)
    translate((0, -4), Squair2)
    translate((2, -2), Squair2)

    reflect('y', Rectangle)
    reflect('y', Triangle)

def aiden_project():
    """
    Great job! This was well-planned and accurately described.
    4 shapes, translation, reflection, and dilation used (no rotation)
    95%
    """
    Triangle = [ (1,6), (2,8), (4,9) ]
    Octagon = [ (-1,6), (1,6), (2,5), (2,3), (1,2), (-1,2), (-2,3), (-2,5) ]
    Rectangle = [ (-7,9), (7,9), (7,-6), (-7,-6) ]
    Rectangle2 = [ (2,1), (7,1), (7,-1), (2,-1) ]

    draw_polygon(Triangle)
    draw_polygon(Octagon)
    draw_polygon(Rectangle)
    draw_polygon(Rectangle2)

    reflect('y', Triangle)
    translate((0,-4), Octagon)
    dilate(2, Rectangle)

    #Mr. L addition:
    reflect('y', Rectangle2)

def tyson_project():
    """
    Included 8 shapes, translations, reflections, and rotations. 
    Some inaccuracies, mainly rotations (watch out for those!), but overall accurate and a good picture!
    95%
    """
    trapezoid = [(-10,-3) , (-6,0) , (6,0), (10,-3)] 
    rectangle = [(-6,0), (-6,7), (-5,7), (-5,0)]
    draw_polygon (trapezoid)
    draw_polygon (rectangle)
    translate((3,0), rectangle)
    translate((5,0), rectangle)
    translate((8,0), rectangle)
    translate((10,0), rectangle)
    translate((12,0), rectangle)
    triangle = [(-7,7), (0,10), (0,7)]
    draw_polygon(triangle)
    reflect ('y', triangle)
    Rectangle1 =[(6 ,0), (0 ,0), (0 ,1), (6 ,1)]
    Rectangle2 =[(7 ,-1), (7 ,-2), (0 , -2), (0, -1)]
    Rectangle3 =[( 9, -3), (9 , -4), (0 ,-4), (0 , -3)]
    draw_polygon(Rectangle1)
    draw_polygon(Rectangle2)
    draw_polygon(Rectangle3)
    rotate(180, Rectangle1)
    rotate(180, Rectangle2)
    rotate(180, Rectangle3)
    Rect4 = [(-2, 6), (-2, 10), (-4, 10), (-4, 6)]
    draw_polygon(Rect4)
    reflect('y', Rect4)
    Rect5 = [(2, 6), (2, 10), (4, 10), (4, 6)]
    draw_polygon(Rect5)
    translate((0, 6), rotate(90, Rect5, "CCW", False))

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