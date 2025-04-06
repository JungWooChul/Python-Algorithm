import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
discovered = [[0]*M for _ in range(N)]
def bfs(x,y):
    global discovered
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))
    discovered[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1 and discovered[nx][ny]==0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1

    return graph[N-1][M-1]

print(bfs(0,0))