import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())
K = int(input())
apple = [tuple(map(int, input().strip().split())) for _ in range(K)]
L = int(input())

direction = []
for _ in range(L):
    X, C = input().strip().split()
    direction.append((int(X), C))

graph = [[0]*N for _ in range(N)]
graph[0][0] = 1
queue = [(0,0)]

# 사과위치 저장
for x,y in apple:
    graph[x-1][y-1] = 2

# 방향 저장(반시계방향 순서)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
di = 3

x,c = direction.pop(0)
answer = 0
while queue:
    answer += 1
    cx,cy = queue[-1]
    nx,ny = cx+dx[di], cy+dy[di]

    # 종료조건
    if nx<0 or nx>=N or ny<0 or ny>=N:
        break
    if graph[nx][ny]==1:
        break

    if graph[nx][ny]==2:        # 사과 있는 경우
        graph[nx][ny] = 1
        queue.append((nx,ny))
    else:                       # 사과 없는 경우
        graph[nx][ny] = 1
        queue.append((nx, ny))

        # 꼬리 땡겨오기
        tail_x, tail_y = queue.pop(0)
        graph[tail_x][tail_y] = 0

    if x==answer:
        if c=='D':
            di = (di-1)%4
        elif c=='L':
            di = (di+1)%4
        if direction:
            x,c = direction.pop(0)

print(answer)