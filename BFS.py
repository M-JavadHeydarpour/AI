# BFS
def bfs(graph, node='A', tag=None):
    if tag is None:
        tag = []

    queue = [node]
    # tag = [node]
    # tag.append(node)

    while queue:

        signed = queue.pop(0)
        # tag.append(signed)
        if signed not in tag:
            tag.append(signed)
            # print(signed, end=" ")

            for neighbour in graph[signed]:
                # if neighbour not in tag:
                queue.append(neighbour)
                # tag.append(neighbour)
    return tag


# test

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C'],
}

print(bfs(graph))
