import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,cnt):
    graph[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny]==1:
                cnt = bfs(nx,ny,cnt+1)
        else:
            continue

    return cnt

answer = 0
apt_cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            answer += 1
            apt_cnt.append(bfs(i,j,1))
apt_cnt.sort()

print(answer)
for cnt in apt_cnt:
    print(cnt)