"""
https://www.pramp.com/challenge/jKoA5GAVy9Sr9jGBjz04

Array Index & Element Equality
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.

Pseudocode:

function indexEqualsValueSearch(arr):
    start = 0
    end = arr.length - 1

    while (start <= end):
        i = round((start+end)/2)
        if (arr[i] - i < 0):
            start = i+1
        else if (arr[i] - i == 0) and ((i == 0) or (arr[i-1] - (i-1) < 0)):
            return i
        else:
            end = i-1

    return -1

"""

arr = [-8, 0, 2, 5]
#       0  1  2  3
#      -8 -1  0  2


def find_index(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] - mid < 0:
            start = mid + 1
        elif:
            pass
        else:
            end = mid - 1


""" Naive Solution """
nums = [-8, 0, 2, 5, 7, 8, 9]

print(nums)
print([nums[idx] - idx for idx in range(len(nums))])
