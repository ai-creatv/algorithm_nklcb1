def kruskal(graph):
    edges = set()
    for node, adj_list in enumerate(graph):
        for adj_node, weight in adj_list:
            if node < adj_node:
                node, adj_node = adj_node, node
            edges.add((weight, node, adj_node))
    edges = list(edges)
    edges.sort()

    parents = [i for i in range(len(graph))]

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parents[b] = a
        else:
            parents[a] = b

    mst = []
    sum_weight = 0
    for edge in edges:
        weight, a, b = edge
        if find(a) != find(b):
            union(a, b)
            mst.append(edge)
            sum_weight += weight
    
    print(sum_weight)
    return mst


graph = [[(2, 5), (3, 2)], # (인접노드, 가중치)
         [(3, 5), (4, 3)],
         [(0, 3), (4, 9)],
         [(0, 10), (4, 2)],
         [(2, 13), (1, 3)]]

print(kruskal(graph))