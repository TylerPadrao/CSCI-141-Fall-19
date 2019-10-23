"""
Tyler Padrao
This program uses multiple functions to create a program that takes a list of numbers and sorts them in a new list. The
program then uses the bumper sort function to append the index of the histogram to the new list the value amount of
times.
"""
import random
import time
from merge_sort import merge_sort
from quick_sort import quick_sort
MAX_NUM = 300

def bumper_sort(data, k = MAX_NUM):
    """
    This function takes two parameters which is a list of natural numbers and the maximum value. The data(or list of
    natural numbers) is then sorted until it reaches the maximum value. A new list is created so that it appends the
    index of the histogram at the value of times it needs to be done.
    """
    #data: the list of natural numbers to sort
    #k: the max value
    hist = [0] * (k + 1)
    for v in data:
        hist[v] += 1

    new_list = []
    #x is the value at the index of i
    #i is the index
    #we have to append the index of the hist at the value of x times
    for i in range(len(hist)):
        for x in range(hist[i]):
            new_list.append(i)
    return new_list

def main():
    """
    This function is a main function. The main function declares an example list called "warmup_list". the function then
    prints the unsorted warmup list and also prints the sorted warmup list. Next, a for loop is used to sort a 1000
    values with a random number between 0 and 300. It prints the unsorted list and sorted list of a 1000 values.
    Next since merge_sort and quick_sort are imported at the beginning, we record the time process it takes for merge
    and quick sort to perform so we can compare them. Next, the function prints out the time it takes for merge sort,
    quick sort, and bumper sort to sort a randomized list of a 1000 values ranging from 0 to 300. Lastly it prints the
    time for each of these sorting methods takes to sort a randomized list of a 1000000 numbers ranging between
    0 and 300.
    """
    warmup_list = [2,5,3,0,2,3,0,3]
    print("Small list, unsorted: " + str(warmup_list))
    new_list = bumper_sort([2,5,3,0,2,3,0,3], 5)
    print("Small list, sorted: " + str(new_list))
    new_list2 = []
    for i in range(1000):
        new_list2.append(random.randrange(300))
    print("Large list, unsorted: " + str(new_list2))
    print("Large list sorted: " + str(bumper_sort(new_list2, 300)))

    print("")

    print("Sorted a randomized list of 1000 elements")
    for fn in (merge_sort, quick_sort, bumper_sort, sorted):
        start = time.process_time()
        fn(new_list2)
        end = time.process_time()
        print(str(fn.__name__) + " in: " + str(end - start) + " seconds")

    print("")

    new_list3 = []
    for i in range(1000000):
        new_list3.append(random.randrange(300))
    print("Sorted a randomized list of 1000000 elements")
    for fn in (merge_sort, quick_sort, bumper_sort, sorted):
        start = time.process_time()
        fn(new_list3)
        end = time.process_time()
        print(str(fn.__name__) + " in: " + str(end - start) + " seconds")

main()