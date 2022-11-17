# This graph problem uses Dijkstra's Shortest Path Algo:
import heapq

def networkDelayTime(times, n, k):

    adjList = [[] for i in range(n)]
    for node, connectedNode, weight in times:
        # In our adjacency list, we need to take "node - 1" to access
        # node n's list:
        adjList[node - 1].append((connectedNode, weight))

    # Initialize a set to prevent loops:
    visited = set()
    # For Dijkstra's Algorithm, we use Min-Heap to traverse the graph.
    # The heap will initially contain the starting node, with 0 weight.
    # REMEMBER to add weight first. heapq uses first value in tuple to
    # compare against other elements:
    hp = [(0, k)]
    heapq.heapify(hp)

    # Variable to keep track of time:
    time = 0

    while hp:

        # Pop the path taken with least weight:
        current_weight, current_node = heapq.heappop(hp)

        # If this node was already visited, skip:
        if current_node in visited:
            continue

        # Mark this node as visited:
        visited.add(current_node)
        # Update the time. Because of the nature of MinHeap, the last node
        # to be processed will give us the total time elapsed:
        time = current_weight

        # Traverse down neighboring nodes from here:
        for next_node, next_weight in adjList[current_node - 1]:
            # Remember to add the "weight" when adding to the MinHeap:
            heapq.heappush(hp, (next_weight + current_weight, next_node))

    # If all nodes were traversed, return the time elapsed. If not, return -1:
    return time if len(visited) == n else -1
