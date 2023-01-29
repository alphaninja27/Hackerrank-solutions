def bfs(n, m, edges, s):
    # Write your code here
    result = [-1 for x in range(n)]
    # Store nodes (1-index) and their neighbours
    graph = {x:set() for x in range(1,n+1)}
    
    queue = [s]
    # Root node
    result[s-1] = 0

    # Populate neighbours
    for e in edges:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])

    while queue:
        node = queue.pop(0)
        for neighbour in graph[node]:
            # If node is not visited, add to queue and add distance
            if result[neighbour - 1] < 0:
                queue.append(neighbour)
                result[neighbour - 1] = 6 + result[node - 1]
    # Remove root distance
    return [i for idx,i in enumerate(result) if idx != s - 1]
