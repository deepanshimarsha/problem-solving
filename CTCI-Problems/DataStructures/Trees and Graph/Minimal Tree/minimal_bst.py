class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def MinimalBST(array, start, end):
    if end < start:
        return
    mid = (start + end) // 2
    n = TreeNode(array[mid])
    n.left = MinimalBST(array, start, mid-1)
    n.right = MinimalBST(array, mid+1, end)
    return n

def Create(array):
    return MinimalBST(array, 0, len(array)-1)

def preOrder(node):
    if not node:
        return

    print(node.value)
    preOrder(node.left)
    preOrder(node.right)

root = Create([1,2,3,4,5,6,7])
preOrder(root)
