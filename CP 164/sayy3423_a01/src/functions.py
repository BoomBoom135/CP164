"""
-------------------------------------------------------
functions for assignement 1
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""

# function t01


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    count = 0
    list = []
    for i in range(len(values)):
        if values[i] in list:
            values[i] = "x"
            count += 1
        else:
            list.append(values[i])

    for j in range(count):
        values.remove("x")

    return

# function t02


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for num in subtrahend:
        count = 0
        for item in minuend:
            if item == num:
                count += 1
        for i in range(count):
            minuend.remove(num)

    return

# function t03


def dsmvwl(string):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(string)
    -------------------------------------------------------
    Parameters:
       string - a string (str)
    Returns:
       out - string with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ""
    vowels = ["a", "e", "i", "o", "u"]
    for c in string:
        if c.lower() not in vowels:
            out += c

    return out

# function t04


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    upp = low = dig = whi = rem = 0
    for line in fv:
        line = line.strip()
        for char in line:
            if char.isdigit():
                dig += 1
            elif char.isalpha():
                if char.islower():
                    low += 1
                else:
                    upp += 1
            elif char == " ":
                whi += 1
            else:
                rem += 1

    return upp, low, dig, whi, rem

# function t05


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    while year > 0:
        year -= 4
    if year == 0:
        leap_year = True
    else:
        leap_year = False

    return leap_year

# function for t06


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = False
    if name[0] == "_" or name[0].isalpha():
        valid = True

    for i in range(1, len(name)):
        if not name[i].isalnum() and name[i] != "_":
            valid = False

    return valid


# function t07
def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    md = 0
    for i in range(len(a)-1):
        if a[i] - a[i+1] > md:
            md = a[i] - a[i+1]

    return md

# function t08


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    total = count = 0
    small = large = a[0][0]
    for row in a:
        for num in row:
            total += num
            count += 1
            if num > large:
                large = num
            if num < small:
                small = num

    average = total / count

    return small, large, total, average


# function t09
def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a[i])):
            temp.append(a[i][j] + b[i][j])
        c.append(temp)

    return c
