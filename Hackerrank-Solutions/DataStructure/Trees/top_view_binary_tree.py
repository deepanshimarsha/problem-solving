class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = None

def print_top_view(root):
    q = []
    m = {}
    q.append(root)
    hd = 0
    root.hd = hd

    while len(q) > 0:
        root = q[0]
        hd = root.hd

        if hd not in m:
            m[hd] = root.data
        if root.left:
            q.append(root.left)
            root.left.hd = hd - 1

        if root.right:
            q.append(root.right)
            root.right.hd = hd + 1

        q.pop(0)

    for i in sorted(m):
        print(m[i],end=" ")

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print_top_view(root)

