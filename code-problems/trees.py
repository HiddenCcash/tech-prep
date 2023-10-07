"""
Binary Tree

      1
    2   3
   5 6 7 8
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
