from trees import root

"""
Given a root node to a binary tree... 
    return the values Preorder - recursively - [1, 2, 5, 6, 3, 7, 8]
    return the values Preorder - iteratively
    return the values Inorder - recursively - [5, 2, 6, 1, 7, 3, 8]
    return the values Inorder - iteratively
    return the values Postorder - recursively - [5, 6, 2, 7, 8, 3, 1]
    return the values Postorder - iteratively - 
"""


def solution_pre_rec(root):

    def search(root, stack):
        if root:
            stack.append(root.val)
            search(root.left, stack)
            search(root.right, stack)
        # if not root:
        #     return False
        # stack.append(root.val)
        # return search(root.left, stack) or search(root.right, stack)

    stack = []
    if root:
        stack.append(root.val)
    else:
        return []
    search(root.left, stack)
    search(root.right, stack)
    return stack


def solution_pre_iter(root):
    output, nodes = [], []

    if root:
        nodes.append(root)
    else:
        return []

    while nodes:
        node = nodes.pop()
        output.append(node.val)

        if node.right:
            nodes.append(node.right)
        if node.left:
            nodes.append(node.left)

    return output


def solution_in_rec(root):

    def traverse(root, output):
        if root.left:
            traverse(root.left, output)
        output.append(root.val)
        if root.right:
            traverse(root.right, output)

    if not root:
        return []
    output = []
    traverse(root, output)
    return output


def solution_in_iter(root):
    output, nodes = [], []

    # Version 2 - avoids three nestings
    while root or nodes:
        while root:
            nodes.append(root)
            root = root.left
        node = nodes.pop()
        output.append(node.val)
        root = node.right
    return output

    # Version 1
    while nodes:
        node = nodes[-1]

        if node.left:
            nodes.append(node.left)
        else:
            _node = nodes.pop()
            output.append(_node.val)
            if nodes:
                _node = nodes.pop()
                output.append(_node.val)
                if _node.right:
                    nodes.append(_node.right)
    return output


def solution_post_rec(root):

    def traverse(root, output):
        if root:
            traverse(root.left, output)
            traverse(root.right, output)
            output.append(root.val)

    output = []
    traverse(root, output)
    return output


def solution_post_iter(root):
    # Version 2
    output, nodes = [], root and [root]
    while nodes:
        node = nodes.pop()
        output.append(node.val)
        nodes += [child for child in (node.left, node.right) if child]
    return output[::-1]

    # Version 1
    if not root:
        return []
    nodes, output = [root, ], []

    while nodes:
        node = nodes.pop()
        if node:
            output.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)

    return output[::-1]
