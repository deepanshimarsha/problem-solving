class Graph:
    def __init__(self, V, E):
        #make unordered pair of edges
        self.E = set(frozenset((u, v)) for u, v in E)
        self.struct = {}
        for v in V:
            self.addVertex(v)
        for u, v in self.E:
            self.addEdge(u, v)

    def addVertex(self, v):
        if v not in self.struct:
            self.struct[v] = set()

    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        self.struct[u].add(v)
        self.struct[v].add(u)
        self.E.add(frozenset((u, v)))

    def degree(self, v):
        return len(self.struct[v])

    def neighbours(self, v):
        return self.struct[v]

    def numEdges(self):
        return len(self.E)

    def numVertex(self):
        return len(self.struct)

    def dfsutil(self,visited,node, stack):
        if node not in visited:
            visited.add(node)
            if len(self.struct[node]) == 0 or :
                stack.append(node)
            else:
                for nbrs in self.struct[node]:
                    self.dfsutil(visited, nbrs)
