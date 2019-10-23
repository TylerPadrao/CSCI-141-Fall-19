"""
Tyler Padrao
This program uses a function to solve the real roots of a quadratic equation, prints the number of roots from the
equation, and also displays the equation in ax^2 + bx + c form.
"""
import math
def quadratic_roots():
    """
    This function prompts the user for an input of values for a, b, and c.
    :Precondition: This function prompts the user for an input of values for a, b, and c.
    :Precondition: Values entered by user are entered as a string, but after converted to an integer value.
    :Postcondition: After the function is called, the output displays the equation, the number of roots, and the real
    roots if the output consists of any.
    """
    first_number = input("Enter a value for a: ")
    second_number = input("Enter a value for b: ")
    third_number = input("Enter a value for c: ")
    a = int(first_number)
    b = int(second_number)
    c = int(third_number)

    # This print statement prints the equation with the values the user entered in ax^2 + bx + c form.
    print(first_number + "x^2 + " + second_number + "x + " + third_number)

    #1. In the first if statement, the code checks if the root is less than zero, then prints "No roots."
    #2. In the first elif statement, the code checks if the root is greater than zero. Next, it proceeds with the quadratic formulas
    #to find the real roots.
    #3. In the second elif statement, the code checks if the root is equal to zero. Next, it proceeds with the quadratic formula
    #to find the real root.
    if b**2 - (4*a*c) < 0:
        print("No roots.")
    elif b**2 - (4*a*c) > 0:
        print("Two roots.")
        quadratic_equation = (b * -1 + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
        quadratic_equation_minus = (b * -1 - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
        print(quadratic_equation)
        print(quadratic_equation_minus)
    elif b**2 - (4*a*c) == 0:
        print("One root.")
        quadratic_equation = (b * -1 + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
        print(quadratic_equation)

quadratic_roots()


