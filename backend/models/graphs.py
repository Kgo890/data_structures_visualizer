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

    def breadth_first_search(self, v):
        self.visited_vertices = []
        self.waiting_queue = []

        self.waiting_queue.append(v)

        while len(self.waiting_queue) != 0:
            current = self.waiting_queue.pop(0)
            self.visited_vertices.append(current)
            list_of_neighbors = sorted(self.graph[current])
            for i in list_of_neighbors:
                if i not in self.waiting_queue and i not in self.visited_vertices:
                    self.waiting_queue.append(i)
        return self.visited_vertices

    def depth_first_search(self, start_vertex):
        visited_vertices = []
        self.depth_first_search_r(visited_vertices, start_vertex)
        return visited_vertices

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        list_of_neighbors = sorted(self.graph[current_vertex])
        for neighbor in list_of_neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)