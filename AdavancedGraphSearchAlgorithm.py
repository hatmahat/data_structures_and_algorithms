from heapq import heappop, heappush
from math import  inf

graph = {
    'A': [('B', 10), ('C', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('B', 15)],
}

for vertex in graph:
    print(f"\nVertext {vertex} connects to: ")
    for edge in graph[vertex]:
        print(f"vertext {edge[0]} with a weight of {edge[1]}")

# Dijkstra's Algorithm
def dijkstras(graph, start):
    distances = {}
    for vertex in graph:
        # print(vertex) -> printed dict's keys
        distances[vertex] = inf # set all vertex's value to infinite
    distances[start] = 0 # set to 0
    vertices_to_explore = [(0, start)] # make list of tuples to explore

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore) # pop vertices_to_explore variable
        for neighbor, edge_weight in graph[current_vertex]: # check neigbors and weights
            new_distance = current_distance + edge_weight # sum all distances
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    return distances

# Test Code
distances_from_a = dijkstras(graph, 'A')
print("\n\nShortest Distances: {0}".format(distances_from_a))

# The A* Algoritm
