class Node:
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None

def decodeHuff(root, s):
    ans = ''
    curr = root
    for i in range(0,len(s)):
        if(s[i] == '0'):
            curr = curr.left
        else:
            curr = curr.right
        if(curr.left == None and curr.right == None):
            ans = ans+str(curr.data)
            curr = root
    return ans

if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node("a")
    root.left.left = Node("b")
    root.left.right = Node("c")

    print(decodeHuff(root, "1001011"))

