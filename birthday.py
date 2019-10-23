"""
Tyler Padrao
This program uses multiple functions to create a program that finds birthdays that occured at least a certain number of
times. This program uses classes to represent instances within a birthday and also uses dictionaries to store the
instances.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Birthday:
    """
    Class Birthday creates a class that has instances of a month which is casted to a string, day and year which are
    casted to integers.
    """
    month: str
    day: int
    year: int

    def month_to_number(self):
        """
        This function creates a dictionary that maps the 12 months to their associated number value. There is a
        variable named "value" that casts the dictionary to a string. Lastly the dictionary is returned.
        """
        month_dict = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8,
                      "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}

        value = str(month_dict[self.month])
        return value

    def __str__(self):
        """
        This function casts all of the instances within a class to a string so they can be printed in the correct
        format.
        """
        return (self.month_to_number() + '/' + str(self.day) + '/' + str(self.year))

def build_dictionary(filename):
    """
    This function builds a dictionary based off of birthdays in a text file. This function opens a given file in read
    mode then reads each line in the file, then closes the file. Next, the function creates a new dictionary. Next, the
    function calls a for loop to iterate through each row in the file and splits the white space. Then, a new birthday
    object is created which passes in it's instances. Lastly, we have to check to see if a birthday is already in the
    dictionary and if it is we increment the occurance of the birthday and if its not we will insert a new value. The
    function then returns the dictionary.
    """
    file = open(filename, mode='r')
    file_contents = file.readlines()  # EX: ["MAY 25 2018", "JAN 3 2016", "MAY 25 2018"]
    file.close()

    bd_dict = {}  # {BirthdayObj: int, BirthdayObj: int, ...}
    for file_row in file_contents:
        # file_row = "MAY 25 2018"
        content = file_row.split(" ")  # EX: ["MAY", "25", "2018"]
        month = content[0]
        day = int(content[1])
        year = int(content[2])
        bd1 = Birthday(month, day, year)

        # See if a birthday is already in the dictionary
        # If it is, increment. Otherwise, insert a new value
        if bd1 in bd_dict:
            bd_dict[bd1] = bd_dict[bd1] + 1
        else:
            bd_dict[bd1] = 1

    return bd_dict

def birthdays_atleast(bd_counts, min_count):
    """
    This function passes two parameters in that's a dictionary and a minimum count. The first thing the function does
    is create a new birthday list. Next, we have to iterate through the dictionary "bd_counts" which was passed in the
    parameter. We then compare the occurances of each birthday to the minimum count, then append the birthday object
    to the list. lastly, we return the list outside the for loop.
    """
    bday_list = []
    for birthday_obj, bd_occurrances in bd_counts.items():
        if bd_occurrances >= min_count:
            bday_list.append(birthday_obj)
    return bday_list

def to_strings(list_birthdays):  # list_birthdays = [Birthday(), Birthday(), ...]
    """
    This function takes the birthday class instances and creates a list of strings to represent the corresponding
    birthdays. We create a new list, then iterate through the list of birthdays(defined in the parameter), then append
    the content to the new list. Lastly, we return the new list outside the for loop.
    """
    bday_list2 = []
    for content in list_birthdays:
        bday_list2.append(str(content))
    return bday_list2

def main():
    """
    This function is a main function which passes the given text file into our "build_dictionary()" function to build
    our dictionary. Next, for our "birthday_atleast()" function, we input the user for the minimum occurances they want
    to find for each birthday. Next, we print a how many times the birthdays occured. Lastly, we print all of the
    birthdays that occured the number of times the user inputed as a list. We then print the list of birthdays, but
    in "month/day/year" form.
    """
    bd_counts = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)

def main2():
    """
    This function is a second main function that acts as a test for the "to_strings()" function just to be sure it
    formats the occured birthdays in the "month/day/year" format correctly.
    """
    bd_counts = build_dictionary("data.txt")
    bd_list = birthdays_atleast(bd_counts, 2)
    string_list = to_strings(bd_list)

    print(string_list)

if __name__ == "__main__":
    main()