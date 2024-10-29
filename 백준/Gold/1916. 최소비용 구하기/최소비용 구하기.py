import sys, heapq

input = sys.stdin.readline
INF = float("inf")

def min_cost(start, end, graph):
    distances = {i:INF for i in graph.keys()}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if graph[current_node]=={} or distances[current_node] < current_distance:
            continue

        for new_node, new_distance in graph[current_node].items():
            distance = current_distance+new_distance
            if distances[new_node] > distance:
                distances[new_node] = distance
                heapq.heappush(queue, [distance, new_node])
    return distances[end]

def main():
    N = int(input())
    M = int(input())

    graph = {i:{} for i in range(N+1)}
    for _ in range(M):
        s, e, cost = map(int, input().strip().split())

        # 한 도시에서 다른 도시로 가는 버스가 여러 개
        try:
            if graph[s][e]:
                graph[s][e] = min(graph[s][e], cost)
        except:
            graph[s][e] = cost
        
    
    start, end = map(int, input().strip().split())
    print(min_cost(start, end, graph))

if __name__ == '__main__':
    main()