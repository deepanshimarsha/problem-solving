#time complexity - O(n)
#space complexity - O(h) where h is height of the tree
#improved algo - it checks the height while calculating it for left and right node for each node in tree
import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def CheckHeight(root):
    if root is None:
        return -1
    left_height = CheckHeight(root.left)
    if left_height == -sys.maxsize-1:
        return -sys.maxsize

    right_height = CheckHeight(root.right)
    if right_height == -sys.maxsize-1:
        return -sys.maxsize-1

    height_diff = abs(left_height-right_height)
    if height_diff > 1:
        return -sys.maxsize-1
    else:
        return max(1 + left_height, 1 + right_height)

def isBalanced(root):
    return CheckHeight(root) != -sys.maxsize-1

root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
root.left = a
root.right = b
a.left = c
a.right = d
print(isBalanced(root))
