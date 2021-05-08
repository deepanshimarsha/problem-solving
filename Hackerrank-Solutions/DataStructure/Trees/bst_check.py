class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST(root, min, max):
    if not root:
        return True
    if root.data >= max or root.data <= min:
        return False
    return checkBST(root.left, min, root.data) and checkBST(root.right, root.data, max)


def check_binary_search_tree_(root):
    return checkBST(root, -1, 10001)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(3)
    root.left.right = Node(5)

    print(check_binary_search_tree_(root))
