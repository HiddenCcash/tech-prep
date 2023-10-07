"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""

from collections import Counter

s = "cbaebabacd"
p = "abc"


def findIndices(s, p):
    # TODO: find sum of values

    hashmap = Counter(p)  # {"a": 1, "b": 1, "c", 1}
    p_len = len(p)
    s_len = len(s)
    curr_sum = p_len
    indices = []

    for start in range(s_len):
        char = s[start]
        if char in hashmap:
            hashmap[char] -= 1

        # window has shifted beyond p_len
        if start >= p_len:
            char_expired = s[start+1-p_len]
            if char_expired in hashmap:
                hashmap[char_expired] += 1

        curr_sum = sum(hashmap.values())

        # check if all hashmap values are zero.
        # if so, there is a match and save beginning index
        if curr_sum == 0:
            print(start)
            indices.append(start + 1 - p_len)

    return indices


print(findIndices(s, p))
