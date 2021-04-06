import heapq

def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n
    


graph = [[(2, 5), (3, 2)], # (인접노드, 가중치)
         [(3, 5), (4, 3)],
         [(0, 3), (4, 9)],
         [(0, 10), (4, 2)],
         [(2, 13), (1, 3)]]