"""
Tyler Padrao
This program uses multiple functions to create a program to take an unsorted list and sort it within the same list using
selection sort. The program opens a file, and inputs the numbers from the file in a list. The program also has a function
to find the index of the greatest value within the list. A helper function is then used to swap the index of the
biggest number with the end index. Lastly, a function is then used to sort the whole list which outputs a sorted list.

Questions:

1. An insertion sort performs better than a biggie sort function when the values are already in increasing order.
Since insertion sort is linear, its going to perform quickest when the list is already in order.
2. Biggie sort performs worse than a insertion sort since each element is being swapped. If the index to the right is
largest than the index the left, it will swap the two indexes. This process has a Polynomial time compelxity which
performs O(N^x) times, as the time gets much worse for each swap.
"""
def open_file():
    """
    This function prompts the user to enter a name of a file, then opens the file. The function then takes the numbers
    from the fle, and adds them to a list.
    """
    file = input("Enter file name: ")
    print("Sorting File: " + file)
    file = open(file, "r")
    list = []
    for line in file:
        line = int(line.strip())
        list += [line]
    print("unsorted: " + str(list))
    return list

def find_max_from(a_list):
    """
    This function takes a list as a parameter, and finds the index of the largest value within the list. This function
    uses a for loop to iterate through the list and compares each index to the current number which is the maximum current
    number. After the loop is done iterating, the maximum number is found, which then returns the index of that largest
    value.
    """
    current_number = a_list[0]
    index = 0
    for i in range(1, len(a_list)):
        if a_list[i] > current_number:
            current_number = a_list[i]
            index = i
    return index

def swap(end_index, index_biggest_number, a_list):
    """
    This function takes the end index, the largest index, and the list as a parameter and sets the end index as a temp
    Then, the end index is set to the index of the biggest number. The index of the largest value is then set back to
    the temp value.
    """
    temp = a_list[end_index]
    a_list[end_index] = a_list[index_biggest_number]
    a_list[index_biggest_number] = temp

def biggiesort(a_list):
    """
    This function uses a while loop to iterate through the list, then calls the swap function to swap the index of the
    largest number with the end index, creating a list in sorted order. Lastly, the function prints the sorted list.
    """
    end_index = (len(a_list) - 1)
    while end_index > 0:
        index_biggest_number = find_max_from(a_list[0:end_index+1])
        swap(end_index, index_biggest_number, a_list)
        end_index-=1
    print("sorted: " + str(a_list))

def main():
    """
    This function stores the function to open a file in a variable and calls the variable as the parameter in the
    biggiesort function. This function is the main function that calls biggiesort.
    """
    file_in_list = open_file()
    biggiesort(file_in_list)

main()