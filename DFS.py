# DFS
def dfs(graph, node='A', tag=[]):
    if node not in tag:
        tag.append(node)

        for n in graph[node]:
            dfs(graph, n, tag)

    return tag

# test

# graph = {
#     'A': ['B', 'D'],
#     'B': ['A', 'C'],
#     'C': ['B', 'D'],
#     'D': ['A', 'C'],
# }
#
# print(dfs(graph))
