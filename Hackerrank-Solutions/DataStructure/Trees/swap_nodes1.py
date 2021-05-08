import os
import sys


#
# Complete the swapNodes function below.
#
class Node:
    def __init__(self, data):
        self.data = str(data) + ' '
        self.left = None
        self.right = None


def build_tree(indexes):
    root = Node(1)
    ptr = root
    queue = []
    queue.append(ptr)

    for child_pair in indexes:
        if child_pair[0] == -1:
            node_left = None
        else:
            node_left = Node(child_pair[0])
        if child_pair[1] == -1:
            node_right = None
        else:
            node_right = Node(child_pair[1])

        ptr.left = node_left
        ptr.right = node_right

        poped_node = queue.pop(0)
        if ptr.left is not None:
            queue.append(poped_node.left)
        if ptr.right is not None:
            queue.append(poped_node.right)
        if len(queue) > 0:
            ptr = queue[0]
    return root



def inorder_traversal(root,s):
    if root:
        sl = inorder_traversal(root.left, s)
        sc = root.data
        sr = inorder_traversal(root.right, s)
        return sl+sc+sr
    else:
        return ''


def given_level(root, level):
    if root is None:
        return
    if level == 1:
        return root
    elif level > 1:
        given_level(root.left, level - 1)
        given_level(root.right, level - 1)



def swap(root, queries):
    # print(queries)

    for i in range(0, len(queries)):
        # print(level)
        level_order_nodes_list = []
        inorder_list = []
        level_order_nodes_list.append(given_level(root, queries[i]))
        #print(level_order_nodes_list)
        for nodes in level_order_nodes_list:
            if nodes is not None:
                if nodes.left is not None and nodes.right is not None:
                    nodes.left, nodes.right = nodes.right, nodes.left
        print(inorder_traversal(root, ''))



original_tree = build_tree([[2,3],[4,-1],[5,-1],[6,-1],[7,8],[-1,9],[-1,-1],[10,11]])
swap(original_tree, [2,4])
