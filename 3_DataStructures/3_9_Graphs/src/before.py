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
        pass

    def bfs(self, vert_ind, value):
        return False

    def dfs(self, vert_ind, value):
        return False
