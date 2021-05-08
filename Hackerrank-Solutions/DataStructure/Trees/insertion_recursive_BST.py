class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert(root,val):
    if root is None:
        root = Node(val)
    elif root.data>val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    insert(root, 10)
    preorder_traversal(root)
