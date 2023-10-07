import collections
from trees import root

"""
Given a root node to a binary tree... 

       1
     2  3
   5 6 7 8

return the values Preorder - recursively - [1, 2, 5, 6, 3, 7, 8]
return the values Preorder - iteratively - [1, 2, 5, 6, 3, 7, 8]
return the values Inorder - recursively - [5, 2, 6, 1, 7, 3, 8]
return the values Inorder - iteratively - [5, 2, 6, 1, 7, 3, 8]
return the values Postorder - recursively - [5, 6, 2, 7, 8, 3, 1]
return the values Postorder - iteratively - [5, 6, 2, 7, 8, 3, 1]
return the values Level order - recursively - [[1], [2, 3], [5, 6, 7, 8]]
return the values Level order - iteratively - [[1], [2, 3], [5, 6, 7, 8]]


Version 0.2 - Nov 6 - 0:45
Version 0.2 - Oct 29th - 0:46
Version 0.2 - Oct 26th - 0:54
Version 0.1 - Oct 24th - 1:04

Version 0.2
    Add two more problems: Binary Tree Level Order recur and iter

Version 0.1
    Total of 6 problems, 3 problems each with recur and iter ways to solve
"""


def solution_pre_rec(root):
    output = []
    if not root:
        return output

    def traverse(root, output):
        output.append(root.val)
        if root.left:
            traverse(root.left, output)
        if root.right:
            traverse(root.right, output)

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
    output = []
    if not root:
        return output

    def traverse(root, output):
        if root.left:
            traverse(root.left, output)
        output.append(root.val)
        if root.right:
            traverse(root.right, output)

    traverse(root, output)
    return output


def solution_in_iter(root):
    output, nodes = [], []
    if not root:
        return output

    curr = root
    while nodes or curr:
        while curr:
            nodes.append(curr)
            curr = curr.left
        node = nodes.pop()
        output.append(node.val)
        curr = node.right
    return output


def solution_post_rec(root):
    output = []
    if not root:
        return output

    def traverse(root, output):
        if root.left:
            traverse(root.left, output)
        if root.right:
            traverse(root.right, output)
        output.append(root.val)

    traverse(root, output)
    return output


def solution_post_iter(root):
    output, nodes = [], root and [root, ]
    if not root:
        return output

    while nodes:
        node = nodes.pop()
        output.append(node.val)
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
    return output[::-1]


def solution_level_recur(root):
    levels = []
    if not root:
        return levels

    def traverse(root, level):
        if len(levels) < level + 1:
            levels.append([])
        levels[level].append(root.val)
        if root.left:
            traverse(root.left, level+1)
        if root.right:
            traverse(root.right, level+1)

    traverse(root, 0)
    return levels


def solution_level_iter(root):
    levels, level = [], 0
    queue = collections.deque()
    if not root:
        return levels
    queue.appendleft(root)

    while queue:
        if len(levels) < level + 1:
            levels.append([])
        for _ in range(len(queue)):
            node = queue.pop()
            levels[level].append(node.val)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        level += 1
    return levels
