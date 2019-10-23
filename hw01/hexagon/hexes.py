import turtle
def draw_hexagon():
    turtle.down()
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)


turtle.speed(4)


def repeat_hexagon():
    draw_hexagon()
    turtle.left(60)
    draw_hexagon()
    turtle.left(60)
    draw_hexagon()
    turtle.left(60)
    draw_hexagon()
    turtle.left(60)
    draw_hexagon()
    turtle.left(60)
    draw_hexagon()
    turtle.left(60)
    draw_hexagon()
    turtle.left(60)


repeat_hexagon()
turtle.right(60)
repeat_hexagon()
turtle.done()















