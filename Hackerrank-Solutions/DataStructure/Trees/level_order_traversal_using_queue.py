class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_level_order(root):
    q = []
    q.append(root)

    while len(q) > 0:
        poped_node = q.pop(0)

        if poped_node.left:
            q.append(poped_node.left)
        if poped_node.right:
            q.append(poped_node.right)

        print(poped_node.data, end=" ")

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)



    print("Level order traversal of binary tree is -")
    print_level_order(root)