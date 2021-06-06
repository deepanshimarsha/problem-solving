class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, lst):
        self.lst = lst
        self.dict = {}
        self.root = None

    def create_tree_from_array(self):
        for i in range(len(self.lst)):

            #create nodes
            if len(self.dict) == 0 or i not in self.dict:
                parent = Node(self.lst[i])
            else:
                parent = self.dict[i]

            if parent.val == None:
                continue

            left_child = Node(self.lst[i*2 + 1])
            right_child = Node(self.lst[i*2 + 2])

            #store in dict
            self.dict[i] = parent
            self.dict[i*2 + 1] = left_child
            self.dict[i*2 + 2] = right_child

            #link
            parent.left = left_child
            parent.right = right_child

            if ((i*2) + 1) == len(self.lst)-1 or ((i*2) + 2) == len(self.lst)-1:
                break

        self.root = self.dict[0]

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

    def get_node(self,val):
        idx = self.lst.index(val)
        return self.dict[idx]

    def leftmost_node(self, node):
        if node.left:
            return self.leftmost_node(node.left)
        else:
            return node
    
    def get_parent(self,node):
        idx = self.lst.index(node.val)
        return self.dict[idx // 2]



#obj.inorder_traversal(obj.root)

def successor(node):
    if node == obj.dict[len(obj.lst)-1]:
        return None
    if node.right:
        return obj.leftmost_node(node.right).val
    return next_ancestor(node)   
    
def next_ancestor(node):
    parent = obj.get_parent(node)
    if parent.left == node:
        return parent.val
    return next_ancestor(parent)

obj = Tree([4,2,6,1,3,5,7])
obj.create_tree_from_array()
print(successor(obj.get_node(1)))

        
