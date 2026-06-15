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


prev = None
head = None


def convert(root):
    global prev, head

    if root is None:
        return

    convert(root.left)

    if prev is None:
        head = root
    else:
        prev.right = root
        root.left = prev

    prev = root

    convert(root.right)


tree = input("Enter Tree: ")

root = buildTree(tree)

convert(root)

curr = head

while curr:
    print(curr.data, end=" ")
    curr = curr.right