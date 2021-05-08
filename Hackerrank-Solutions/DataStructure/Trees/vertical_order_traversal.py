import collections

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_vertical_order(root):
    q = []
    m = {}
    hd_node = {}

    q.append(root)
    hd_node[root] = 0
    m[0] = [root.data]

    while len(q) > 0:
        poped_node = q.pop(0)
        if poped_node.left:
            q.append(poped_node.left)
            hd_node[poped_node.left] = hd_node[poped_node] - 1
            hd = hd_node[poped_node.left]
            if m.get(hd) is None:
                m[hd] = []
            m[hd].append(poped_node.left.data)

        if poped_node.right:
            q.append(poped_node.right)
            hd_node[poped_node.right] = hd_node[poped_node] + 1
            hd = hd_node[poped_node.right]
            if m.get(hd) is None:
                m[hd] = []
            m[hd].append(poped_node.right.data)

    sorted_m = collections.OrderedDict(sorted(m.items()))

    print((sorted_m.values()))

    for i in sorted_m.values():
        for j in i:
            print(j,end=" ")
        

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)



    print("Vertical order traversal of binary tree is -")
    print_vertical_order(root)
