from collections import deque, defaultdict
def solution(n, edge):
    # 그래프 구성
    graph = defaultdict(list)
    for ed in edge:
        s,e = ed
        graph[e].append(s)
        graph[s].append(e)
    
    visited = [0] * (n+1)
    dist = [-1] * (n+1)
    dist[1] = 0
    
    queue = deque([1])
    while queue:
        node = queue.popleft()
        r = dist[node]
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                if dist[i] == -1 or dist[i] > r+1:
                    dist[i] = r+1
    
    max_dist = max(dist)
    answer = 0
    for d in dist:
        if max_dist == d:
            answer += 1
    return answer