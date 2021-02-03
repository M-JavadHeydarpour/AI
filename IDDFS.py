edges = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'], 'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Oradea', 'RimnicuVilcea', 'Arad', 'Fagaras'],
    'Timisoara': ['Arad', 'Lugoj'], 'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'], 'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'RimnicuVilcea', 'Pitesti'],
    'RimnicuVilcea': ['Craiova', 'Sibiu', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Giurgiu', 'Pitesti', 'Urziceni'],
    'Giurgiu': ['Bucharest'], 'Pitesti': ['Bucharest', 'Craiova', 'RimnicuVilcea'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

visitedPaths = ""
# Contains final path from source to destination
finalPath = []
# Contains the total level of depth for each iteration
countOfDepth = 0
# Contains the source state
tempVar = ""


def iterativeDFS(source, destination, maxDepth, edges):

    global countOfDepth, visitedPaths, tempVar
    tempVar = source

    # Check to perform if the source and destination is not in edges list
    if source not in edges.keys() or destination not in edges.keys():
        finalPath.append('FAIL')
        return finalPath

    for limit in range(maxDepth):
        # visited = source
        # print(source)
        countOfDepth = limit
        if depthLimitSearch(source, destination, limit, edges):
            # prints all the visited states
            # print(visitedPaths)
            finalPath.append(tempVar)
            finalPath.reverse()
            return finalPath
    # State not found. Hence, Fail.
    finalPath.append("FAIL")
    return finalPath


def depthLimitSearch(source, destination, limit, edges):
    global countOfDepth, visitedPaths, tempVar, finalPath

    # Indents the visited states and appends the paths in visitedPaths
    if (countOfDepth - limit) <= 0:
        visitedPaths += '\n' + source
    else:
        visitedPaths += ('\n' + '\t' * (countOfDepth - limit)) + source

    # Checks if the the final destination has been reached
    if source == destination:
        return True

    # Checks whether all the depths have been traversed for the current iteration
    if limit < 1:
        return False

    # Temporary variable to remove the backward link from the edge-list data structure
    temp = []

    # Iterates over all connected states of a current state for a given depth
    for adjacentNode in edges[source]:
        # Removes the backward connection to visited nodes for eg.  connection between Arad - Zerind will remove Zering - Arad from the edges list
        temp = edges[adjacentNode]
        if source in temp:
            temp.remove(source)
            edges[adjacentNode] = temp
        #     Performs a recursive call to the DLS function with limit - 1
        if depthLimitSearch(adjacentNode, destination, limit - 1, edges):
            # Appends the final path once the destination state is reached
            finalPath.append(adjacentNode)
            return True
    return False

def main():
    start = 'Arad'
    goal = 'Bucharest'
    solution = iterativeDFS(start, goal, 1000, edges)

    print(solution)


# Execute the main program.
if __name__ == "__main__":
    main()
