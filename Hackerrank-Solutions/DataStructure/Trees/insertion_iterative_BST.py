class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):

        if self.root is None:
            self.root = Node(val)
            self.root.left = None
            self.root.right = None
        ptr = self.root

        # infinite loop
        while True:
            if ptr.info > val:
                if ptr.left:
                    ptr = root.left
                else:
                    ptr.left = Node(val)

                    # escape the loop
                    break
            elif ptr.info < val:
                if ptr.right:
                    ptr = root.right
                else:
                    ptr.right = Node(val)

                    # escape the loop
                    break
            else:
                break


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    tree = BinarySearchTree()
    tree.root = root

    tree.insert(10)
    preOrder(root)

