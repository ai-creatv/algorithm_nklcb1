class Vertex:
    def __init__(self, value, adj_list=None):
        self.value = value
        if adj_list is None:
            adj_list = []
        self.adj_list = adj_list


class Graph:
    def __init__(self):
        self.vertices = []

    def insert(self, value, adj_list):
        self.vertices.append(Vertex(value, adj_list))
        for adj_ind in adj_list:
            self.vertices[adj_ind].adj_list.append(len(self.vertices) - 1)

    def bfs(self, vert_ind, value):
        return False

    def dfs(self, vert_ind, value):
        return False

graph = Graph()
graph.insert(0, [])
graph.insert(1, [0])
graph.insert(2, [1])
graph.insert(3, [2])
graph.insert(4, [0, 2, 3])

print(graph.bfs(0, 2))
print(graph.dfs(0, 3))