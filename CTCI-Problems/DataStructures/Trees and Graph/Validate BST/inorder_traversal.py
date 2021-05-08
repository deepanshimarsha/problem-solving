#tree cannot have DUPLICATE value

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

last_printed = None
def CheckBST(root):
    if root is None:
        return True

    #check / recurse left
    if not CheckBST(root.left):
        return False

    #check current
    if last_printed is not None and root.data <= last_printed:
        return False
    last_printed = root.data

    #check / recurse right
    if not CheckBST(root.right):
        return False

    return True

root = TreeNode(4)
a = TreeNode(2)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(3)
root.left = a
root.right = b
a.left = c
a.right = d
print(CheckBST(root))