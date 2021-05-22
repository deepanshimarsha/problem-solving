# in-degree approach
# time complexity - O(P + D)
class Node:
    def __init__(self, val):
        self.val = val
        self.in_degree = 0
        self.children = set()

# directed graph
class Graph:
    def __init__(self, vertices, edges):
        self.edges = set(frozenset((u, v) for u, v in edges))
        self.struct = {}
        for v in vertices:
            self.addVertex(v)
        for u, v in self.edges:
            self.addEdge(u, v)


    def addVertex(self, v):
        new_node = Node(v)
        for node in self.struct:
            if node.val == new_node.val:
                # vertex already present
                return
        # otherwise add it
        self.struct[new_node] = set()

    def get_node(self, val):
        for node in self.struct:
            if node.val == val:
                return node

    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        node1 = self.get_node(u)
        node2 = self.get_node(v)
        self.struct[node1].add(node2)
        node2.in_degree += 1

    def inDegree(self, vertex):
        node = self.get_node(vertex)
        return node.in_degree

    def get_children(self, vertex_node):
        return self.struct[vertex_node]

def BuildOrder(projects, dependencies):
    graph = Graph(projects, dependencies)
    res =[]
    for proj in projects:
        buildorder = non_dependent_nodes(graph)
        if len(buildorder) == 0:
            if len(res) == 0:
                return "error"
            return res
        for node in buildorder:
            toBeProcessed(node, graph)
            res.append(node.val)
    return res

def toBeProcessed(node, graph):
    for child in graph.get_children(node):
        child.in_degree -= 1

def non_dependent_nodes(graph):
    lst = []
    for proj_node in graph.struct:
        if proj_node.in_degree == 0:
            lst.append(proj_node)
            proj_node.in_degree = -1
    return lst

if __name__ == "__main__":
    print(BuildOrder([1,2,3,4,5,6,7,8], {(1,5),(2,5),(2,1),(2,8),(3,1),(4,7),(6,3),(6,2),(6,1)}))










