from trees import root

"""
      1
    2   3
   5 6 7 8

Given a root node to a binary tree... 
    return the values Preorder - recursively - [1, 2, 5, 6, 3, 7, 8]
    return the values Preorder - iteratively
    return the values Inorder - recursively - [5, 2, 6, 1, 7, 3, 8]
    return the values Inorder - iteratively
    return the values Postorder - recursively - [5, 6, 2, 7, 8, 3, 1]
    return the values Postorder - iteratively - 

Version 0.1 - Oct 24th - 1:04

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

    print()

    def traverse(root, output):
        if root.left:
            traverse(root.left, output)
        output.append(root.val)
        if root.right:
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
        output.append(root.val)
        if root.right:
            traverse(root.right, output)
        if root.left:
            traverse(root.left, output)

    output = []
    traverse(root, output)
    return output[::-1]


def solution_post_iter(root):
    output, nodes = [], root and [root, ]

    while nodes:
        curr = nodes.pop()
        output.append(curr.val)
        if curr.left:
            nodes.append(curr.left)
        if curr.right:
            nodes.append(curr.right)

    return output[::-1]
