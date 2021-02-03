# import time
from resources.Graph import *
from resources.Node import *
from resources.PriorityQueue import *


def ucs(graph, start, goal):

    s = start
    visited = set()
    queue = PriorityQueue()

    start = Node(start, None)

    queue.insert(start, 0)
    path = []
    while queue:
        # cost, node = queue.get()
        node = queue.remove()
        # path.append(node.name)
        cost = node.f
        if node.name not in visited:
            visited.add(node.name)

            if node.name == goal:
                path = []
                # print(type(node.name))
                # print(type(start.name))
                # d = node.name
                while node != start:
                    path.append(node.name + ': ' + str(node.f))
                    node = node.parent
                    # d = node
                path.append(s + ': ' + str(start.f))
                print(path[::-1])
                # print(graph.)
                return
            for i in graph.get(node.name):
                if i not in visited:
                    total_cost = cost + graph.get(node.name, i)
                    tmp = Node(i, None)
                    tmp.f = total_cost
                    tmp.parent = node
                    queue.insert(tmp, total_cost)
    # print(graph.get(goal))

if __name__ == "__main__":

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

    ucs(graph, 'Arad', 'Bucharest')
