from resources.Graph import *
from resources.Node import *


def AStar(graph, heuristics, start, end):
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # graph.get
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add the start node
    open.append(start_node)

    # if not open node then break loop
    while len(open) > 0:

        # select lowest node
        open.sort()

        # Get the node with the lowest cost
        current_node = open.pop(0)

        # Add the current node to the closed list
        closed.append(current_node)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))

            # because stack
            return path[::-1]

        # Get neighbours
        neighbors = graph.get(current_node.name)

        # Loop neighbors
        for key, value in neighbors.items():

            # Create a neighbor node
            neighbor = Node(key, current_node)

            # Check if the neighbor is in the closed list
            if neighbor in closed:
                continue

            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h

            # Check if neighbor is in open list and if it has a lower f value
            if add_to_open(open, neighbor):
                # Everything is green, add neighbor to open list
                open.append(neighbor)

    return None  # no path


def add_to_open(open, neighbor):
    for node in open:
        if neighbor == node and neighbor.f > node.f:
            return False
    return True


def main():
    graph = Graph()

    Romania = [['Arad', 'Zerind', 75], ['Arad', 'Timisoara', 118], ['Arad', 'Sibiu', 140],
               ['Zerind', 'Oradea', 71], ['Timisoara', 'Lugoj', 111], ['Oradea', 'Sibiu', 151],
               ['Sibiu', 'Rimnicu Vilcea', 80], ['Sibiu', 'Fagaras', 99], ['Lugoj', 'Mehadia', 70],
               ['Mehadia', 'Drobeta', 75], ['Drobeta', 'Craiova', 120], ['Craiova', 'Rimnicu Vilcea', 146],
               ['Craiova', 'Pitesti', 138], ['Rimnicu Vilcea', 'Pitesti', 97], ['Pitesti', 'Bucharest', 101],
               ['Bucharest', 'Fagaras', 211], ['Bucharest', 'Giurgiu', 90], ['Bucharest', 'Urziceni', 85],
               ['Urziceni', 'Hirsova', 98], ['Urziceni', 'Vaslui', 142], ['Hirsova', 'Eforie', 82],
               ['Vaslui', 'Iasi', 92], ['Iasi', 'Neamt', 87]
               ]
    for city in Romania:
        graph.connect(city[0], city[1], city[2])

    graph.make_undirected()

    # heuristics
    heuristics = {'Zerind': 75, 'Oradea': 146, 'Sibiu': 140, 'Fagaras': 230, 'Timisoara': 118, 'Lugoj': 229,
                  'Mehadia': 299, 'Drobeta': 374, 'Craiova': 494, 'Rimnicu Vilcea': 220, 'Pitesti': 317,
                  'Bucharest': 418, 'Giurgiu': 508, 'Urziceni': 503, 'Hirsova': 601, 'Eforie': 687, 'Vaslui': 645,
                  'Iasi': 737, 'Neamt': 824, 'Arad': 0}

    path = AStar(graph, heuristics, 'Arad', 'Bucharest')
    print(path)


if __name__ == "__main__":
    main()
