from turtle import *
import tkinter as tk

MAX = 300
MIN = -300
PENCOLOR = (20, 150, 60)

def main():
    window = tk.Tk()
    build_ui(window)

    screen = Screen()
    colormode(255)
    pencolor(PENCOLOR)

    draw_axes()

    test()
    #mrl_project()

    screen.exitonclick()

def build_ui(window):
    label = tk.Label(text = "Trasnformation builder").pack()
    button_make_poly = tk.Button(text = "Create Polygon",
                                    width=30,
                                    height = 10,
                                    command = lambda: make_poly(entry_num_points)
                                    ).pack()
    entry_num_points = tk.Entry(width = 50).pack()
    window.mainloop()

def make_poly(points):
    if points <= 2:
        return False
    for i in points:
        pass
    


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

def mrl_project():
    pass

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



if __name__ == "__main__":
    main()