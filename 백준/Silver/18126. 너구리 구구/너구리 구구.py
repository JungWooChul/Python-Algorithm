import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
graph = defaultdict(dict)

# 입력값 끝까지 받기
for _ in range(N-1):
    a,b,c = map(int, input().split())
    graph[a][b] = c 
    graph[b][a] = c 

distances = {i+1 : float('inf') for i in range(N)}
distances[1] = 0

queue = []
heapq.heappush(queue, [0, 1])

while queue:
    current_dist, current_pos = heapq.heappop(queue)
    if distances[current_pos] < current_dist:
        continue

    for next_pos, next_dist in graph[current_pos].items():
        distance = current_dist + next_dist
        if distance < distances[next_pos]:
            distances[next_pos] = distance
            heapq.heappush(queue, [distance, next_pos])

print(max(distances.values()))