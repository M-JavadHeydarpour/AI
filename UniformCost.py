# import time
from resources.Graph import *
from resources.Node import *
from resources.PriorityQueue import *


# def ucs(graph, key_node_start='', key_node_goal='', verbose=True):
#     # UCS lookalikes Dijkstra Algorithm
#
#     queue = PriorityQueue()  # init a pQueue
#
#     key_node_start = Node(key_node_start, None)
#     key_node_goal = Node(key_node_goal, None)
#     key_node_goal.g = 500
#     # get the neighbours of initial node
#     neighbours = graph.get(key_node_start.name)
#
#     # adds the keys of successors in priority queue
#
#     for key, value in neighbours.items():
#         neighbour = Node(key, key_node_start)
#         # each item of queue is a tuple (key, cumulative_cost)
#         queue.insert((neighbour, neighbour.g), neighbour.g)
#
#     reached_goal, cumulative_cost_goal = False, -1
#
#     while not queue.is_empty():
#         # remove item of queue, remember: item of queue is a tuple (key, cumulative_cost)
#         key_current_node, cost_node = queue.remove()
#         # print(key_current_node, 'key current node')
#         print(key_node_goal)
#         # key_current_node = Node(key_current_node[0], key_current_node[1])
#         if key_current_node == key_node_goal:
#             reached_goal, cumulative_cost_goal = True, key_current_node.g
#             break
#
#         if verbose:
#             # shows a friendly message
#             print('Expands node \'%s\' with cumulative cost %s ...' % (key_current_node, cost_node))
#             # time.sleep(2)
#
#         # get all successors of key_current_node
#         # print(key_current_node)
#         neighbours = graph.get(key_current_node.name)
#
#         if neighbours:  # checks if contains successors
#             # insert all successors of key_current_node in the queue
#             for neighbour in neighbours:
#                 cumulative_cost = key_current_node.g \
#                                   + graph.get(key_current_node.name, neighbour)
#                 # cumulative_cost = graph.getWeightEdge(key_current_node, neighbour) + cost_node
#                 queue.insert((neighbour, cumulative_cost), cumulative_cost)
#
#     if reached_goal:
#         print('\nReached goal! Cost: %s\n' % cumulative_cost_goal)
#     else:
#         print('\nUnfulfilled goal.\n')
# class Graph:
#     def __init__(self):
#         self.edges = {}
#         self.weights = {}
#
#     def neighbors(self, node):
#         return self.edges[node]
#
#     def get_cost(self, from_node, to_node):
#         return self.weights[(from_node + to_node)]

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
