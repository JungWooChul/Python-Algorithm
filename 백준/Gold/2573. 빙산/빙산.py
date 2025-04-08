import sys
sys.setrecursionlimit(100000)
from collections import deque
input = sys.stdin.readline

def main():
    n,m = map(int, input().strip().split())
    ice = [list(map(int, input().strip().split())) for _ in range(n)]

    queue = deque([])
    for i in range(n):
        for j in range(m):
            if ice[i][j]:
                queue.append((i,j))

    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y, visited):
        q = deque([(x, y)])
        visited[x][y] = 1

        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and ice[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
        return visited

    while True:
        team = len(queue)  # 빙산 하나를 이루는 얼음의 수(기준)
        if team==0 or team==1:
            print(0)
            return

        discovered = [[0] * m for _ in range(n)]
        check = 0
        for i in range(team):  # 빙산 분리 확인
            x, y = queue.popleft()
            if discovered[x][y] == 0 and ice[x][y]:
                discovered = bfs(x, y, discovered)
                check += 1
            queue.append((x, y))

        if check != 1:
            print(answer)
            return

        answer += 1
        discovered = [[0] * m for _ in range(n)]
        for i in range(team): # 얼음 녹는 시뮬레이션
            x,y = queue.popleft()
            discovered[x][y] = 1

            cnt = 0
            for i in range(4):
                if not ice[x+dx[i]][y+dy[i]] and not discovered[x+dx[i]][y+dy[i]]:
                    cnt+=1
            if ice[x][y] <= cnt:
                ice[x][y] = 0
            else:
                ice[x][y] -= cnt
                queue.append((x,y))

    return

main()