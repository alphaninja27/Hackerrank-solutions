def prims(n, edges, start):
    # Write your code here
    vertices = {start}
    result = 0
    while len(vertices) < n:
        newEdges = [e for e in edges if ((e[0] in vertices and e[1] not in vertices) or (e[1] in vertices and e[0] not in vertices))]
        edge = min(newEdges, key = lambda e: e[2])
        vertices.update(edge[:2])
        result += edge[2]
    return result
