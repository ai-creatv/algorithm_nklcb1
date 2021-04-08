import heapq

def prim(graph):
    mst = []
    heap = []
    weights = [float('inf')] * len(graph)
    connected = set()

    weights[0] = 0
    for node, weight in graph[0]:
        heapq.heappush(heap, (weight, 0, node))

    weight_sum = 0
    while heap:
        weight, a, b = heapq.heappop(heap)

        if weights[b] <= weight or b in connected:
            continue
        
        weights[b] = weight
        connected.add(b)
        weight_sum += weight
        mst.append((weight, a, b))

        adj_list = graph[b]
        for n, w in adj_list:
            if weights[n] > w:
                heapq.heappush(heap, (w, b, n))

    print(weight_sum)
    return mst

graph = [[(1, 28), (5, 10)], # (인접노드, 가중치)
         [(0, 28), (2, 16), (6, 14)],
         [(1, 16), (3, 12)],
         [(2, 12), (4, 22), (6, 18)],
         [(3, 22), (5, 25), (6, 24)],
         [(0, 10), (4, 25)],
         [(1, 14), (3, 18), (4, 24)]]
print(prim(graph))