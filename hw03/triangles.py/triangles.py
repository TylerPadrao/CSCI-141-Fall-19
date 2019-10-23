"""
Tyler Padrao
This program creates a recursion sequence of multiple triangles.
"""
import turtle
def draw_triangle(side):
    """
    This function draws a triangle with a specific length side when the function is called.
    :Precondition: Start with turtle facing east, pen up, and the tracer true.
    :Postcondition: The turtle is facing east and the tracer is true as the pen is down.
    """
    turtle.left(120)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.left(120)

def triangles_depth(side, depth):
    """
    This function draws a sequence of triangles which uses recursion to complete the series.
    :Precondition: Start with turtle facing east, pen up, and the tracer true.
    :Postcondition: The turtle is facing east and the tracer is true as the pen is down.
    :Postcondition: The recursive call draws the whole sequence of triangles when the depth is called to 4.
    """
    if depth == 0:
        return None
    else:
        turtle.left(120)
        turtle.forward(side)
        turtle.right(120)
        triangles_depth(side / 2, depth - 1)
        turtle.forward(side)
        triangles_depth(side / 2, depth - 1)
        turtle.right(120)
        turtle.forward(side)
        turtle.left(120)

turtle.speed(4)
triangles_depth(150, 4)
turtle.done()