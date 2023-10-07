# DOCS
# https://docs.python.org/3.7/library/stdtypes.html#set

a = set([1, 2, 3, 4, 5, 6])
b = a
c = set([1, 3, 5])
d = set([1, 10])


print(b.issubset(c))  # False
print(c.issubset(b))  # True

print(b.issuperset(c))  # True

print(b.union(c))  # set([1, 2, 3, 4, 5, 6])
print(c.union(b))  # set([1, 2, 3, 4, 5, 6]) what is in both c and b
print(c.difference(d))  # set([3, 5]) what is in c but not d
print(c.intersection(d))  # set([1]) venn-diagram intersection
print(c.symmetric_difference(d))  # set([3, 5, 10])
