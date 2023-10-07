
import collections
"""
Given a tree, return the a list of the sum of column nodes.

      1
    2   3
   5 6 7 8

Where the left child's colum count is +1
While the right child's colum count is -1

                0col 1
           1col 2   -1col 3
   2col 5  0col 6   0col 7    -2col 8

"""


class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)

"""
Problem 1
Use DFS to printout all values, in any order
"""


def print_node(root):
    print(root.val)
    return (root.left and print_node(root.left)) \
        or (root.right and print_node(root.right))


print_node(root)


"""
Problem 2
Given a tree, return the a list of the sum of column nodes.

                0col 1
           1col 2   -1col 3
   2col 5  0col 6   0col 7    -2col 8

Answer should be: [8, 3, 14, 2, 5]

Solved in 10 minutes
"""


def store_values(root, col, colmap):
    # 1st approach
    # colmap[col].append(root.val)
    # return (root.left and store_values(root.left, col+1, colmap)) \
    #     or (root.right and store_values(root.right, col-1, colmap))

    # 2nd approach
    colmap[col].append(root.val)
    if not root.left:
        return False
    if not root.right:
        return False
    return store_values(root.left, col+1, colmap) \
        or store_values(root.right, col-1, colmap)


def compute_col_sums(colmap):
    return [sum(item[1]) for item in sorted(colmap.items())]


def main():
    colmap = collections.defaultdict(list)
    col = 0  # start with col index of zero
    store_values(root, col, colmap)
    result = compute_col_sums(colmap)
    print(result)


main()
