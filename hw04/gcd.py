"""
Tyler Padrao
This program uses multiple functions to create a program finding the greatest common denominator using tail recursion
and iterative functions.
"""
def gcd_rec(a, b):
    """
    This function finds the GCD using tail recursion. if the second number the user inputs is equal to zero, then it
    returns the first number since the GCD would be equal to either the first or second number. If the second number is not equal to zero,
    the function calls the tail recursion finding the greatest common denominator.
    """
    if b == 0:
        return a
    else:
        return gcd_rec(b, a%b)

def gcd_iter(a, b):
    """
    This function finds the GCD using a while loop. If a is less than b or b is less than a, the counter is equal to the smaller
    of the two. When their equal, it will return a. Then, the while loop is called which checks if b is equal to zero which returns a, and also
    vise versa. Next, if the modulus of a or b is equal to zero, it will return the counter and if the modulus is not equal to zero, it will
    decrement the counter, which will eventaully find the GCD.
    """
    counter = 0
    if a < b:
        counter = a
    elif b < a:
        counter = b
    else:
        return a
    while counter >= 0:
        if b == 0:
            return a
        elif a == 0:
            return b
        elif a % counter == 0 and b % counter == 0:
            return counter
            break
        else:
            counter = counter - 1

def test_gcd_rec():
    """
    This function uses a series of tests to test the recursive function.
    """
    print(gcd_rec(10, 10))
    print(gcd_rec(10, 65))
    print(gcd_rec(10, 8))
    print(gcd_rec(9, 10))
    print(gcd_rec(456, 6))
    print(gcd_rec(57, 99))
    print(gcd_rec(0, 10))
    print(gcd_rec(10, 0))
    print(gcd_rec(69, 6578))
    print(gcd_rec(100, 25))

def test_gcd_iter():
    """
    This function uses a series of tests to test the iteration function.
    """
    print(gcd_iter(10, 10))
    print(gcd_iter(10, 65))
    print(gcd_iter(10, 8))
    print(gcd_iter(9, 10))
    print(gcd_iter(456, 6))
    print(gcd_iter(57, 99))
    print(gcd_iter(0, 10))
    print(gcd_iter(10, 0))
    print(gcd_iter(69, 6578))
    print(gcd_iter(100, 25))

def main():
    """
    This function prompts the user to choose finding the GCD using either recursive or iteration. Then, it will prompt the user to
    enter two numbers. Lastly, it will print the GCD. This function also calls the two test functions for both iterative and recursion.
    """

    recursive_or_iterative = input("Select the GCD function to use:\n\n 1. Recursive\n 2. Iterative\n\n")
    choice = int(recursive_or_iterative)

    a = int(input("Please select the first number: "))
    b = int(input("Please select the second number: "))
    recursive = gcd_rec(a, b)
    iterative = gcd_iter(a, b)
    if choice == 1:
        answer = gcd_rec(a, b)
        print("The greatest common denominator is " + str(answer))
    else:
        answer = gcd_iter(a, b)
        print("The greatest common denominator is " + str(answer))

if __name__ == "__main__":
    test_gcd_rec()
    test_gcd_iter()
    main()