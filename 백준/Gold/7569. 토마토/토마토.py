import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    m,n,h = map(int, input().split())
    box = []
    for _ in range(h):
        box.append([list(map(int, input().split())) for i in range(n)])


    discovered = [[[0]*m for _ in range(n)] for _ in range(h)]

    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]

    queue = deque([])
    def tomato():
        while queue:
            z,x,y = queue.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nz<h and 0<=nx<n and 0<=ny<m and box[nz][nx][ny]==0 and not discovered[nz][nx][ny]:
                    queue.append((nz, nx, ny))
                    box[nz][nx][ny] = box[z][x][y]+1
                    discovered[nz][nx][ny] = 1

        return

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k]==1 and not discovered[i][j][k]:
                    queue.append([i,j,k])
                    discovered[i][j][k] = 1

    tomato()

    answer = 0
    for i in range(h):
        for j in range(n):
            if 0 in box[i][j]:
                print(-1)
                return
            answer = max(answer, max(box[i][j])-1)

    print(answer)
    return

main()