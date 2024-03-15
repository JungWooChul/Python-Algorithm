from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    
    # 양방향 그래프 생성
    graph = defaultdict(dict)
    for i in road:
        try:
            if graph[i[0]][i[1]] > i[2]:
                graph[i[0]][i[1]] = i[2]
        except:
            graph[i[0]][i[1]] = i[2]
        try:
            if graph[i[1]][i[0]] > i[2]:
                graph[i[1]][i[0]] = i[2]
        except:
            graph[i[1]][i[0]] = i[2]
        
    # 최단경로저장
    distances = {node:float('inf') for node in graph}
    distances[1] = 0
    
    # 우선순위 큐
    queue = []
    heapq.heappush(queue, [distances[1], 1])
    
    while queue:
        cur_distance, cur_node = heapq.heappop(queue)
        if distances[cur_node] < cur_distance:
            continue
        for next_node, next_distance in graph[cur_node].items():
            distance = cur_distance + next_distance
            if distances[next_node] >= distance:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
    answer = 0
    for val in distances.values():
        if val <= K:
            answer += 1
    return answer