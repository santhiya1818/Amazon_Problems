from collections import deque

class Node:
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None


def buildTree(s):

    if len(s) == 0 or s[0] == "N":
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


def isBST(root, low=float('-inf'), high=float('inf')):

    if root is None:
        return True

    if root.data <= low or root.data >= high:
        return False

    return (isBST(root.left, low, root.data) and
            isBST(root.right, root.data, high))


tree = input("Enter Tree: ")

root = buildTree(tree)

print(1 if isBST(root) else 0)