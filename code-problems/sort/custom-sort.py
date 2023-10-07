"""
Given a list of alphanumeric words/numbers sort all alphabetic words preceed 
all numeric words

input = [45, 34, "bat", "ape", 46] -> ["bat", "ape", 45, 34, 46]

"""

import collections
words = [45, 34, "bat", "ape", "cat", 46]


def custom_sort(elem):

    # return 0 if type(a) == str else 1
    return (0,) if type(elem) == str else (1,)


print(sorted(words, key=custom_sort))

"""
Same as above, but also return alpha words in alphabetical order
and numeric words in numerical order

input = [45, 34, "bat", "ape", 46] -> ["ape", "bat", 34, 45, 46]
"""

words = [45, 34, "bat", "ape", "cat", 46]


def custom_sort_all(elem):

    # return 0 if type(a) == str else 1
    return (0, elem) if type(elem) == str else (1, elem)


print('Trying: ', words)
print(sorted(words, key=custom_sort_all))

"""
Sort a list of tuples based on frequecy. If there is a tie in frequency, 
then sort the words alphbetically.
Return a list of strings
 input = [('day', 1), ('apple', 1), ('is', 3), ('the', 4)]
 outpiut = ["the", "is", "apple", "day"]
"""

# I can sort based on frequency
input = [('day', 1), ('apple', 1), ('is', 3), ('the', 4)]
# [('the', 4), ('is', 3), ('day', 1), ('apple', 1)]
print(sorted(input, key=lambda kv: kv[1], reverse=True))
# but now, how to sort "day" and "apple" while prioritzing frequency


def custom_sort(elem):
    print('elem', elem)
    return (elem[1], elem[0])


input = [('day', 1), ('apple', 1), ('is', 3), ('the', 4)]
# [('the', 4), ('is', 3), ('day', 1), ('apple', 1)]
print(sorted(input, key=custom_sort, reverse=True))

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
count = collections.Counter(words)
candidates = count.keys()  # just the words
# here, candidates is a nested sort denoted by a tuple
# the sort prioritzes based on the index of the tuple
# the lower value goes first
# the first sort is prioritzied by the word count, so -4 goes before -3
# the second (nested) sort is if there is a tie during the first sort,
# then, we compare "day" and "apple" to see which one goes rirst
candidates.sort(key=lambda word: (-count[word], word))
print(candidates[-k:])
