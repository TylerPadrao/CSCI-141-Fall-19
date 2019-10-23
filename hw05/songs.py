import turtle
def square(color):
    """
    This function draws a single 10 X 10 square with a filled color of the user's choice.
    :Precondition: Start with turtle facing east, pen up, and the tracer true.
    :Postcondition: The turtle is facing east and the tracer is true as the pen is down.
    """
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.end_fill()

def paint_line(string):
    """
    This function draws a color filled box for each character in a string that the user can input. This function uses
    a nested for loop to perform this. If and elif statements are also used to check the ascii values of the characters
    and assigns them colors based on their ascii values. Also if a string is on a new line, the filled boxes will move
    down to the next line.
    :Precondition: Start with turtle facing east, pen up, and the tracer true.
    :Postcondition: The turtle is facing east and the tracer is true as the pen is down.
    """
    for line in string:
        for char in line:
            if ord(char) < 70:
                color = "blue"
            elif 70 <= ord(char) < 100:
                color = "red"
            elif 100 <= ord(char) < 110:
                color = "green"
            elif 110 <= ord(char) < 122:
                color = "pink"
            elif 122 < ord(char):
                color = "orange"
            print(char)
            square(color)
            turtle.up()
            turtle.forward(10)
            turtle.down()

            if char == ("\n"):
                turtle.up()
                turtle.right(90)
                turtle.forward(10)
                turtle.left(90)
                turtle.up()
                turtle.backward((len(line)) * 10)
                turtle.down()
                square(color)

def picture(file):
    """
    This function draws calls the paint_line() function to draw a sequence of colored boxes. This function allows the user
    to open a file of their choice and print the sequence of colored boxes based on their file. The turtle also goes to
    the top left corner of the window to start drawing.
    :Precondition: Start with turtle facing east, pen up, and the tracer true.
    :Postcondition: The turtle is facing east and the tracer is true as the pen is down.
    """
    turtle.up()
    turtle.goto(-325, 275)
    file = open(file)
    paint_line(file)
    file.close()

def main():
    """
    This function is a main function which calls the picture function, sets the turtle speed to zero, and allows the
    user to input a file of their choice.
    :Precondition: Start with turtle facing east, pen up, and the tracer true.
    :Postcondition: The turtle is facing east and the tracer is true as the pen is down.
    """
    turtle.speed(0)
    picture("Song.txt")
    turtle.done()

main()