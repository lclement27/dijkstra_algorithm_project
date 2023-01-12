from heapq import *
from typing import List
import copy

def print_adjacency(adjacency: List[int]) -> None:
    ''' prints an adjacency matrix in easy-to-read format
    Args:
        adj: a 2D list of edge weights for a graph
    '''
    print("   ", end = "")
    for c in range(len(adjacency)):
        print(f"{c:>2} ", end = '')
    print()
    for r in range(len(adjacency)):
        print(f"{r:>2} ", end = '')
        for c in range(len(adjacency[r])):
            value = adjacency[r][c]
            if value == float("Inf"): value = "∞"
            print(f"{value:>2} ", end = '')
        print()
    print('---' * (len(adjacency) + 1))

def dijkstra(adjacency: List[List[int]], start: int, dest: int) -> float:
    ''' implements Dijkstra's algorithm on the graph represented by
        the given adjacency matrix, finding the shortest path from
        vertex with index start to vertex with index dest, returning
        the cost/distance of that shortest path
    Args:
        adjacency: a 2D adjacency matrix representing the graph, with entries
                    corresponding to edge weights
        start:     the index (between 0 and # vertices - 1) of the origin vertex
        dest:      the index (between 0 and # vertices - 1) of the destination vertex
    Returns:
        the length of the shortest path from start to dest
    '''
    # YOUR CODE GOES HERE
    d = [float("Inf")] * len(adjacency) # list of distances, initially set to infinity
    d[start] = 0        # first vertex has distance 0 from itself
    U = [start]         # list of indices added
    u = start           # most recently added index

    while u != dest:        # until destination is reached
        for v in range(len(adjacency)):
            if v not in U:
                if adjacency[u][v] != float("Inf"):
                    d[v] = min(d[v], d[u] + adjacency[u][v])

        min_dist = float("Inf")
        for v in range(len(adjacency)):
            if v not in U:
                if d[v] < min_dist:
                    u = v
                    min_dist = d[v]
        U.append(u)
    return d


def main():
    '''
    num_vertices = 6
    adj = [[float("Inf")] * num_vertices for i in range(num_vertices)]
    adj[0][1] = adj[1][0] = 7
    adj[0][3] = adj[3][0] = 2
    adj[1][2] = adj[2][1] = 2
    adj[1][4] = adj[4][1] = 3
    adj[2][5] = adj[5][2] = 4
    adj[3][4] = adj[4][3] = 1
    adj[4][5] = adj[5][4] = 10
    '''
    num_vertices = 15
    adj = [[float("Inf")] * num_vertices for i in range(num_vertices)]
    adj[0][1] = adj[1][0] = 7
    adj[0][3] = adj[3][0] = 5
    adj[0][6] = adj[6][0] = 3
    adj[1][4] = adj[4][1] = 2
    adj[2][4] = adj[4][2] = 3
    adj[2][5] = adj[5][2] = 9
    adj[2][8] = adj[8][2] = 1
    adj[3][4] = adj[4][3] = 6
    adj[3][7] = adj[7][3] = 2
    adj[4][8] = adj[8][4] = 3
    adj[5][8] = adj[8][5] = 7
    adj[5][11] = adj[11][5] = 4
    adj[6][7] = adj[7][6] = 5
    adj[6][9] = adj[9][6] = 3
    adj[7][8] = adj[8][7] = 8
    adj[7][9] = adj[9][7] = 6
    adj[7][10] = adj[10][7] = 4
    adj[7][13] = adj[13][7] = 3
    adj[8][11] = adj[11][8] = 1
    adj[9][12] = adj[12][9] = 2
    adj[9][13] = adj[13][9] = 5
    adj[10][13] = adj[13][10] = 2
    adj[10][14] = adj[14][10] = 5
    adj[11][14] = adj[14][11] = 3
    adj[12][13] = adj[13][12] = 7




    print_adjacency(adj)

    #start = 1
    #end   = 5
    #distances = dijkstra(adj, start, end)
    #print(distances[end])


    start = input("Enter a starting vertex ('q' to quit): ")
    while start.lower() != 'q':
        end = input("Enter a destination vertex ('q' to quit): ")
        if end.lower() == 'q': break
        try:
            start = int(start)
            end = int(end)
            if 0 <= start < num_vertices and \
               0 <= end   < num_vertices:
                distances = dijkstra(adj, start, end)
                print(f"The shortest path from {start} to {end} is length {distances[end]}")
            else:
                print(f"Invalid indices: {start}, {end}")
        except:
            pass
        start = input("Enter a starting vertex ('q' to quit): ")


main()
