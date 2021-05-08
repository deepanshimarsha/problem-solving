#calculate hwight of left and right subtree for each node in a tree
#time complexity - O(n log n)

def getHeight(root):
    if root is None:
        return -1

    return max(1+getHeight(root.left), (1+getHeight(root.right)))

def isBalanced(root):
    if root is None:
        return True
    height_diff = abs(getHeight(root.left) - getHeight(root.right))
    if height_diff > 1:
        return False
    else: #recurse for each node in tree
        return isBalanced(root.left) and isBalanced(root.right)


