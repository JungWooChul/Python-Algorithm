import sys
import heapq
from collections import defaultdict
input  = sys.stdin.readline

N, maxlen = map(int, input().split())

graph = defaultdict(dict)
for i in range(maxlen):
    graph[i][i+1] = 1
graph[maxlen]

for i in range(N):
    k, vertex, edge = map(int, input().split())
    if vertex > maxlen:
        continue
    try:
        if graph[k][vertex] > edge:
            graph[k][vertex] = edge
    except:
        graph[k][vertex] = edge

distances = {node:float('inf') for node in range(maxlen+1)}
distances[0] = 0

queue = []
heapq.heappush(queue, [distances[0], 0])

while queue:
    current_distance, current_node = heapq.heappop(queue)
    
    if distances[current_node] < current_distance:
        continue

    for new_node, new_distance in graph[current_node].items():
        distance = current_distance + new_distance
        if distances[new_node] > distance:
            distances[new_node] = distance
            heapq.heappush(queue, [distance, new_node])

print(distances[maxlen])