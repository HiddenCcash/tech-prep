"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space
"""

# sorting
# counter = collections.Counter(words)
# candidates = counter.keys()
# candidates.sort(key=lambda word: (-counter[word], word))
# return candidates[:k]

# heap
# counter = collections.Counter(words)
# heap = [(-count, word) for word, count in counter.items()]
# heapq.heapify(heap)
# [item[1] for item in heapq.nsmallest(k, heap)]

string = "12345"

for idx in range(len(string)-1, -1, -1):
    print(string[idx])
