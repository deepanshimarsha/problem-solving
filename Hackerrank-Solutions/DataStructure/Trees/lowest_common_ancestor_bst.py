class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, v1, v2):
    if root:
        if root.data> v1 and root.data> v2:
            return lca(root.left, v1, v2)
        elif root.data< v1 and root.data < v2:
            return lca(root.right, v1, v2)
        else:
            return root.data

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(lca(root, 5, 3))




