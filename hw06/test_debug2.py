"""
This program includes a function to find and return
the length of a longest common consecutive substring
shared by two strings.

If the strings have nothing in common, the longest
common consecutive substring has length 0.

For example, if string1 = "established", and
string2 = "ballistic", the function returns the
integer 3, as the string "lis" is the longest common
consecutive substring shared by the two strings.

The function tests all possible pairs of starting points
(starting point for string 1, and starting point for string 2),
and measures the match from each.  It keeps
track of the length of the best match seen,
and returns that when finished checking all starting points.

The function has bug(s).

There are no tests (yet).

Your job is to
1) include in this program a sufficient
suite of pass/fail tests to thoroughly
test the function and expose all error(s).

2) Generate a screenshot that
demonstrates your use of a debugger
to step through the function. Specifically it should
illustrate the execution point of a test at
which the function makes (or is about to make)
a mistake.

3) fix the code and document your fix(es).
Include additional tests if you feel it
necessary to thoroughly test the function.

You will submit your updated version of this
file (along with a separate document containing
the screenshot and answered questions).

File:  test_debug2.py
Author: CS @ RIT
Author: (Tyler Padrao)

"""

def match(string1, string2):
    """
    Identifies and returns the length of a longest
    common consecutive substring shared
    by the two input strings.
    :param string1: The first string.
    :param string2: The second string.
    :return: length of a longest shared consecutive string.
    """
    #Note: This code is the updated/fixed code, Thus all tests will pass.
    best_length = 0
    # for all possible string1 start points
    if string1 == string2:
        return len(string1)
    for idx1 in range(len(string1)-1):
        # for all possible string2 start points
        for idx2 in range(len(string2)-1):
            # check if these characters match
            if string1[idx1] == string2[idx2]:
                this_match_count = 1
                # see how long the match continues
                while idx1 + this_match_count < len(string1) and \
                        idx2 + this_match_count < len(string2) and string2[idx2 + this_match_count] == string1[idx1 + this_match_count]:

                    this_match_count += 1

                # compare to best so far
                if this_match_count > best_length:
                    best_length = this_match_count

    # now return the result
    return best_length

def test_function1(string1, string2, expected):
    """
    This is a test function that takes 3 parameters: original word, code word, and the expected value. The test function
    provides a print statement with all of these parameters. If the program fails, it will print the expected value,
    the original and code word. If the test passed, it will print passed.
    """
    result = match(string1, string2)
    if result == expected:
        print("Passed")
    else:
        print("failed; expected", expected, "got", result)

def run_all_tests():
    """
    This is a test function that runs all of the tests, when the user inputs the two strings, and an expected value for the
    longest consecutive string, it will print passed. If the test has failed, it will print the actual result and expected
    value.
    """
    test_function1("established", "ballistic", 3)
    test_function1("bookkeeper", "bookkeeping", 8)
    test_function1("hhjkfhbkjgghihivdfv", "hsgfjgghihieh", 7)
    test_function1("", "", 0)
    test_function1("hh", "hh", 2)
    test_function1("a", "h", 0)
    test_function1("ddd", "ddd", 3)
    test_function1("aaa", "HHH", 0)
    test_function1("bookkeeper", "bookkeeper", 10)
    test_function1("h", "h", 1)
    test_function1("abcabcd", "abcd", 4)
    test_function1("abcd", "abcabcd", 4)

if __name__ == "__main__":
    run_all_tests()