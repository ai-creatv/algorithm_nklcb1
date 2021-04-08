def kruskal(graph):
    edges = set()
    for node, adj_list in enumerate(graph):
        for adj_node, weight in adj_list:
            if node < adj_node:
                edges.add((weight, adj_node, node))
            else:
                edges.add((weight, node, adj_node))
    edges = list(edges)
    edges.sort()

    parents = [i for i in range(len(graph))]
    rank = [0 for _ in range(len(graph))]

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x]) # path compression
        return parents[x]
    
    def union(a, b):
        if rank[a] < rank[b]: # union-by-rank
            parents[b] = a
        else:
            parents[a] = b
        
        if rank[a] == rank[b]:
            rank[a] += 1

    mst = []
    sum_weight = 0
    for edge in edges:
        weight, a, b = edge
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            union(root_a, root_b)
            mst.append(edge)
            sum_weight += weight
    
    print(sum_weight)
    return mst


graph = [[(1, 28), (5, 10)], # (인접노드, 가중치)
         [(0, 28), (2, 16), (6, 14)],
         [(1, 16), (3, 12)],
         [(2, 12), (4, 22), (6, 18)],
         [(3, 22), (5, 25), (6, 24)],
         [(0, 10), (4, 25)],
         [(1, 14), (3, 18), (4, 24)]]

print(kruskal(graph))