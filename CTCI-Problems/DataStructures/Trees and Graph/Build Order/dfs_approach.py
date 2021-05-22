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
        self.E.add(frozenset((u, v)))

    def neighbours(self, v):
        return self.struct[v]




