"""

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

https://leetcode.com/problems/group-anagrams/

"""

import collections
ex1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

"""
My Solution with run time of O(nklogk) where n is number of strings
and k is the number chars in the string
"""


def createGroups(words):
    counts = {}

    for word in words:
        # Two strings are anagrams if and only if their sorted strings are equal.
        word_sort = ''.join(sorted(word))  # "eat" -> "aet"
        if word_sort not in counts:
            counts[word_sort] = [word]
        else:
            counts[word_sort].append(word)  # {"aet": ["eat", "ate", ...]}

    return [group for group in counts.values()]


print(createGroups(ex1))

"""
Ideal Solution with run time of O(nk) where n is number of strings
and k is the number chars in the string
"""


def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        # create a
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()
