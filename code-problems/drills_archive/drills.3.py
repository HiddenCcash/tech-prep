import collections
from trees import root

"""
      1
    2   3
   5 6 7 8

Given a root node to a binary tree... 
    return the values Preorder - recursively - [1, 2, 5, 6, 3, 7, 8]
    return the values Preorder - iteratively - [1, 2, 5, 6, 3, 7, 8]
    return the values Inorder - recursively - [5, 2, 6, 1, 7, 3, 8]
    return the values Inorder - iteratively - [5, 2, 6, 1, 7, 3, 8]
    return the values Postorder - recursively - [5, 6, 2, 7, 8, 3, 1]
    return the values Postorder - iteratively - [5, 6, 2, 7, 8, 3, 1]
    return the values Level order - recursively - [[1], [2, 3], [5, 6, 7, 8]]
    return the values Level order - iteratively - [[1], [2, 3], [5, 6, 7, 8]]

Version 0.2 - Oct 26th - 0:54
Version 0.1 - Oct 24th - 1:04

Version 0.2
    Add two more problems: Binary Tree Level Order recur and iter

Version 0.1
    Total of 6 problems, 3 problems each with recur and iter ways to solve
"""


def solution_pre_rec(root):
    if not root:
        return []

    def traverse(root, output):
        if root:
            output.append(root.val)
            traverse(root.left, output)
            traverse(root.right, output)

    output = []
    traverse(root, output)
    return output


def solution_pre_iter(root):
    output, nodes = [], root and [root, ]

    while nodes:
        node = nodes.pop()
        output.append(node.val)
        if node.right:
            nodes.append(node.right)
        if node.left:
            nodes.append(node.left)
    return output


def solution_in_rec(root):
    if not root:
        return []

    def traverse(root, output):
        if root:
            traverse(root.left, output)
            output.append(root.val)
            traverse(root.right, output)

    output = []
    traverse(root, output)
    return output


def solution_in_iter(root):
    output, nodes = [], []

    curr = root
    while nodes or curr:
        while curr:
            nodes.append(curr)
            curr = curr.left
        curr = nodes.pop()
        output.append(curr.val)
        curr = curr.right

    return output


def solution_post_rec(root):
    if not root:
        return []

    def traverse(root, output):
        if root:
            output.append(root.val)
            traverse(root.right, output)
            traverse(root.left, output)

    output = []
    traverse(root, output)
    return output[::-1]


def solution_post_iter(root):
    output, nodes = [], root and [root, ]

    while nodes:
        node = nodes.pop()
        output.append(node.val)
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return output[::-1]


def solution_level_recur(root):
    if not root:
        return []

    def traverse(node, level):
        if len(output) == level:
            output.append([])

        output[level].append(node.val)

        if node.left:
            traverse(node.left, level+1)
        if node.right:
            traverse(node.right, level+1)

    output = []
    traverse(root, 0)
    return output


def solution_level_iter(root):
    if not root:
        return []

    queue = collections.deque()
    output = []

    queue.appendleft(root)
    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.pop()
            temp.append(node.val)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        output.append(temp)
    print(output)
    return output
