import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m, x, y, k = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
direction = list(map(int, input().strip().split()))

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 : 가로(r)/세로(c)

# [4,1,3,6]
dice_r = [0, 0, 0, 0] # 가로의 끝 원소가 바닥
# [2,1,5,6]
dice_c = [0, 0, 0, 0] # 가로와 세로의 두번째 원소(공통)가 윗 면

for idx, d in enumerate(direction):
    nx = x + dx[d - 1]
    ny = y + dy[d - 1]
    # print(f'idx:{idx}, direction:{d}')
    # print(nx, ny)
    # 범위 밖: 명령 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    # 동,서
    if d <= 2:
        tmp = [0]*4
        for i in range(4):
            tmp[(i + dy[d-1]) % 4] = dice_r[i]

        dice_r = tmp
        dice_c[1], dice_c[3] = dice_r[1], dice_r[3]

    # 북,남
    else:
        tmp = [0] * 4
        for i in range(4):
            tmp[(i + dx[d - 1]) % 4] = dice_c[i]

        dice_c = tmp
        dice_r[1], dice_r[3] = dice_c[1], dice_c[3]

    # 칸의 수가 0인 경우
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice_r[3] # 주사위 바닥면 복사
    else:
        dice_r[3] = graph[nx][ny]
        dice_c[3] = graph[nx][ny]
        graph[nx][ny] = 0

    x,y = nx, ny
    # print(dice_r, dice_c)
    print(dice_r[1])