from collections import deque

class Node:

    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None


def buildTree(s):

    if not s or s[0] == "N":
        return None

    values = s.split()

    root = Node(values[0])

    q = deque([root])

    i = 1

    while q and i < len(values):

        curr = q.popleft()

        if values[i] != "N":
            curr.left = Node(values[i])
            q.append(curr.left)

        i += 1

        if i >= len(values):
            break

        if values[i] != "N":
            curr.right = Node(values[i])
            q.append(curr.right)

        i += 1

    return root


first_leaf = -1


def check(node, level):
    global first_leaf

    if node is None:
        return True

    if node.left is None and node.right is None:

        if first_leaf == -1:
            first_leaf = level

        return level == first_leaf

    return check(node.left, level + 1) and check(node.right, level + 1)


tree = input("Enter Tree: ")

root = buildTree(tree)

print(1 if check(root, 0) else 0)