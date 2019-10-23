
def counter_rec(num: int):
    """
    Return A list of numbers from 0 to num.
    Ex: counter(5) = [4,3,2,1,0]
    """
    if num == 0:
        return []

    if num == 1:
        return [0]

    if num > 1:
        print(num)
        return [num].extend(counter_rec(num - 1))
        # [a,b].extend([c,d]) = [a,b,c,d]

    """
    Base Case
    Iterative Case to get to Base Case
    """

def counter_iter(num: int):
    """
    Ex: counter_iter(5) = [0,2,4,6,8] (i=0,0 i=1,2 i=2,4)
    """
    list = []
    for i in range(0,num):
        list.append(i * 2)
    return list


if __name__ == "__main__":
    #print(counter_iter(5))
    print(counter_rec(5))
def gcd_rec(a, b):
    if b == 0:
        return a
    return gcd_rec(b, a % b)

def gcd_iter(a, b):
    if b == 0:
        return a
    if a == 0:
        return b

    # gcd_iter(10, 10) = 10
    while a != b:
        if b == 0:
            break

        if a > b:
            a = a - b
        else:  # b > a
            b = b - a

    return a

"""
if __name__ == "__main__":
    print(gcd_iter(10, 10))

    print(gcd_iter(13, 24))
    print(gcd_iter(24, 13))

    print(gcd_iter(24, 12))
    print(gcd_iter(12, 24))


a=13 b=24

13, 11

11, 2

2, 1

1, 0
"""

"""
24 12
12 0
"""