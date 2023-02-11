def quickestWayUp(ladders, snakes):
    # Write your code here
    graph = {s[0]: s[1] for s in snakes}
    graph.update({l[0]: l[1] for l in ladders})
    
    visited = set([1])
    queue = [1]
    rolls = {}
    
    while queue:
        idx = queue.pop(0)
        for i in range(1, 7):
            # If neighbour is a snake/ladder, jump to its end point
            # else, increment as is
            neighbour = graph.get(idx + i, idx + i)
            if neighbour not in visited:
                rolls[neighbour] = rolls.get(idx, 0) + 1
                visited.add(neighbour)
                queue.append(neighbour)
            if neighbour == 100:
                return rolls[neighbour]
    return -1
