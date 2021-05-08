class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def height(root):
    if root is None:
        return -1
    return max(1 + height(root.left), 1 + height(root.right))




if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    print(height(root))
