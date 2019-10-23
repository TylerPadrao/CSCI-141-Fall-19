from dataclasses import dataclass

@dataclass(frozen=True)
class Birthday:
    month: str
    day: int
    year: int

    def month_to_number(self):
        month_dict = {"JAN":1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8,
                     "SEP":9, "OCT":10, "NOV":11, "DEC":12}

        value = str(month_dict[self.month])
        return value



    def __str__(self):
        return (self.month_to_number() + '/' + str(self.day) + '/' + str(self.year))


def build_dictionary(filename):
    file = open(filename, mode='r')
    file_contents = file.readlines()  # ["MAY 25 2018", "JAN 3 2016", "MAY 25 2018"]
    file.close()

    bd_dict = {}  # {BirthdayObj: int, BirthdayObj: int, ...}
    for file_row in file_contents:
        # file_row = "MAY 25 2018"
        content = file_row.split(" ")  # ["MAY", "25", "2018"]
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
    bday_list = []
    for birthday_obj, bd_occurrances in bd_counts.items():
        if bd_occurrances >= min_count:
            bday_list.append(birthday_obj)
    return bday_list

def to_strings(list_birthdays):  # list_birthdays = [Birthday(), Birthday(), ...]
    bday_list2 = []
    for content in list_birthdays:
        bday_list2.append(str(content))
    return bday_list2

def main():
    bd_counts = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)

def main2():
    bd_counts = build_dictionary("data.txt")
    bd_list = birthdays_atleast(bd_counts, 2)
    string_list = to_strings(bd_list)

    print(string_list)

    """
    List - [1,2,3]
    Dictionary - {'key1':4, 'key2':5}
    
    Add item to List - List.append("hi")
    Add item to Dict - Dictionary["key"] = "value"
    
    Get value at index 3 from List - List[3]
    Get value with key "three" from Dict - Dict['three']
    
    Set value at index 3 to "hello" List - list[3] = "hello"
    Set value at key "three" to "hello" Dict - Dict['three'] = "hello"
    """



if __name__ == "__main__":
    main()