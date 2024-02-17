class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}

        for i in range(vertices):
            self.graph[i] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    def transpose(self):
        transposed_graph = Graph(self.vertices)
        for i in self.graph:
            for j in self.graph[i]:
                transposed_graph.add_edge(j, i)
        return transposed_graph

    def dfs_scc(self, v, visited, result):
        visited[v] = True
        result.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_scc(i, visited, result)

    def find_scc(self):
        stack = []
        visited = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)

        transposed_graph = self.transpose()

        visited = [False] * self.vertices
        strongly_connected_components = []

        while stack:
            i = stack.pop()
            if not visited[i]:
                current_scc = []
                transposed_graph.dfs_scc(i, visited, current_scc)
                strongly_connected_components.append(current_scc)

        return strongly_connected_components

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

scc_result = g.find_scc()
print("Strongly Connected Components:")
print(scc_result)
