"""
Recursive functions.
"""


def product(lst, idx=0):
    """
    returns the product of a list of numbers
    """
    if idx == len(lst):
        return 1

    return lst[idx] * product(lst, idx+1)


def longest(lst, idx=0):
    """
    returns the longest string in given a list of strings
    """
    if idx == len(lst):
        return 0

    return max(len(lst[idx]), longest(lst, idx+1))


def every_other(str, idx=0):
    """
    returns a string of every other character of the input string
    """
    if idx == len(str):
        return ""

    new_char = str[idx] if idx%2 == 0 else ""
    return new_char + every_other(str, idx+1)


def is_palendrome(str, idx=0):
    """
    returns true if the given string is a palendrome, otherwise false
    in this implementation, letter case must match
    """
    if idx > len(str)/2 - 1:
        return True

    if str[idx] != str[-idx-1]:
        return False

    return is_palendrome(str, idx+1)*True
    

def find_index(lst, str, idx=0):
    """
    returns the index of a string in an array
    returns -1 if string not found
    """
    if idx == len(lst):
        return -1

    if lst[idx] == str:
        return idx

    return find_index(lst, str, idx+1)


def reverse_string(str, idx=0):
    """
    returns the string in reverse order
    """
    if idx == len(str):
        return ""

    return reverse_string(str, idx+1) + str[idx]


def gather_strings(obj, out=[]):
    """
    given a dictionary, returns a list of all the strings in the dictionary
    """
    if isinstance(obj, str):
        out.append(obj)
        return out

    if isinstance(obj, dict):
        for key in obj:
            gather_strings(obj[key], out)
        return out

    return out

