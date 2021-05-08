class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1
    return max(1 + height(root.left),1 + height(root.right) )

def print_level_order(root):
    h = height(root)
    for i in range(1, h+2):
        print_given_level(root, i)

def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")

    elif level > 1:
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)



    print("Level order traversal of binary tree is -")
    print_level_order(root)