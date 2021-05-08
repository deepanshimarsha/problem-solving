from collections import deque

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


def inorder_traversal(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.data
            curr = curr.right


def swap(indexes, queries):
    root = build_tree(indexes)
    for k in queries:
        h = 1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if h % k == 0:
                    node.left, node.right = node.right, node.left
                q += filter(None, (node.left, node.right))
            h += 1
        yield inorder_traversal(root)









