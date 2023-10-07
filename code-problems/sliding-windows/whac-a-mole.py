"""
Given an int array of holes where 1 means a mole and 0 is no mole.
Find out the max number of moles you can hit with a mallet of width w.

http://leetcode.com/discuss/interview-question/350139/Google-or-phone-screen-or-whac-a-mole
"""

# ans = 4
holes1 = [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]
w1 = 5
holes2 = []
w2 = 1
holes3 = [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]
w3 = 10


def findMaxDuplicateWork(holes, w):
    """
    This version contains duplicate work inside the for loop with the use of sum().
    """
    # check bounds
    if w >= len(holes):
        return sum(holes)
    curr_max = 0
    # the number of steps the sliding window will take
    steps = len(holes) + 1 - w
    for idx in range(steps):
        curr_sum = sum(holes[idx: idx+w])  # duplicate work here
        curr_max = max(curr_sum, curr_max)
    return curr_max


assert findMaxDuplicateWork(holes1, w1) == 4
assert findMaxDuplicateWork(holes2, w2) == 0
assert findMaxDuplicateWork(holes3, w3) == 5


def findMax(holes, w):
    # check bounds
    if w >= len(holes):
        return sum(holes)

    # init vars
    curr_sum = curr_max = 0
    steps = len(holes)

    for start in range(steps):
        curr_sum += holes[start]
        if (start >= w):
            curr_sum -= holes[start-w]
        curr_max = max(curr_sum, curr_max)
    return curr_max


assert findMax(holes1, w1) == 4
assert findMax(holes2, w2) == 0
assert findMax(holes3, w3) == 5
