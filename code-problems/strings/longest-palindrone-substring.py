"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

WIKI - https://en.wikipedia.org/wiki/Longest_palindromic_substring
"""


""" Brute Force O(n^3) """


def longestPalindrome(s: str):

    # if length of input string is less than 2 return the string as it is
    if len(s) < 2:
        return s

    # if length is 2
    if len(s) == 2:
        # check if the string of length two is a palindrome
        if s == s[::-1]:
            return s
        # else return the first character from the string
        return s[0]

    # save longest palindrome
    final = ''

    # i will traverse from 0 to len(s)
    for i in range(len(s)):

        # j will traverse backwards
        # j will traverse from len(s) to i
        for j in range(len(s)-1, i, -1):

            # check if string is palindrome
            if s[i:j+1] == s[i:j+1][::-1]:

                # if it is palindrome check if it longer than previously found palindrome
                if len(final) < len(s[i:j+1]):
                    final = s[i:j+1]

    # if no palindrome is found return the first character as any character is palindrome of itself
    if not final:
        return s[1]

    # else return the palindromic string of lengeth more than 1
    return final


""" Expand Around Center O(n^2) Version #1 """
# https://leetcode.com/problems/longest-palindromic-substring/discuss/351327/Python3-Expand-from-center


def longestPalindrome(s: str):
    if not s:
        return ""
    longest = ""

    for m in range(len(s)):
        # palindrome expands at the center m
        sub = palindrome(s, m, m)
        if len(sub) > len(longest):
            longest = sub
        # palindrome expands at the center between m and m + 1
        sub = palindrome(s, m, m + 1)
        if len(sub) > len(longest):
            longest = sub
    return longest


def palindrome(s, l, r):
    # palindrome function finds the longest palindrome in string s from center
    # m or center m and m+1.
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


""" Expand Around Center O(n^2) Version #2 """


def longestPalindrome(self, s):  # version 2
    max_string = ''
    N = len(s)
    for i in range(N):
        j = 0
        while i-j >= 0 and i+j < N and s[i+j] == s[i-j]:
            new_string = s[i-j:i+j+1]
            j += 1
        if len(new_string) > len(max_string):
            max_string = new_string
        j = 0
        while i-j-1 >= 0 and i+j < N and s[i+j] == s[i-j-1]:
            new_string = s[i-j-1:i+j+1]
            j += 1
        if len(new_string) > len(max_string):
            max_string = new_string

    return max_string


"""
DP Solution

To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

https://leetcode.com/problems/longest-palindromic-substring/discuss/297375/Python-easy-to-understand-DP-solution
"""

# "babad"
# "cbbd"


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    # create a boolena matrix of size length X length all values set to False
    arr_2d = [[False for _ in range(length)] for _ in range(length)]

    max_sub_len = 0
    substring = (0, 0)

    # Trivial case
    # Set diagnoal to True
    for i in range(length):
        arr_2d[i][i] = True

    # Two chars base case
    for i in range(length-1):
        j = i + 1
        arr_2d[i][j] = s[i] == s[j]
        if arr_2d[i][j] and (max_sub_len < 2):
            max_sub_len = 2
            substring = (i, j)

    # General case
    step = 2
    for _ in range(length-2):  # why length-2?
        i = 0
        j = i+step
        while (i < length) and (j < length):
            arr_2d[i][j] = (s[i] == s[j]) and arr_2d[i+1][j-1]
            if arr_2d[i][j] and (j-i+1 > max_sub_len):
                max_sub_len = j-i+1
                substring = (i, j)
            i += 1
            j += 1
        step += 1
    return s[substring[0]: substring[1]+1]
