"""
Given an array of integers, find if the array contains any duplicates.
Return True if there are duplicates
"""

input = [1, 2, 2, 3]

# my attempt #1
hashset = set()


def isDups(input):
    for val in input:
        if val in hashset:
            return True
        else:
            hashset.add(val)

# my attempt #2


def isDups2(input):
    return False if len(input) == len(set(input)) else True


def test_1():
    assert isDups(input)


def test_2():
    assert isDups2(input)
