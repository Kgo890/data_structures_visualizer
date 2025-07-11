class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()

    def unconnected_vertices(self):
        unconnected = []
        for node, neighbors in self.graph.items():
            if len(neighbors) == 0:
                unconnected.append(node)
        return unconnected

    def search(self, node):
        for n in self.graph:
            if n == node:
                return True
        return False

    def reset(self):
        self.graph = {}

    def get_graph(self):
        return {node: list(neighbors) for node, neighbors in self.graph.items()}

