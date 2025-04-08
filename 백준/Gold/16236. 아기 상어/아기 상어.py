import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().strip().split())) for _ in range(N)]

# 아기상어 초기 위치 확인
for i in range(N):
    for j in range(N):
        if sea[i][j]==9:
            x, y = i, j
            sea[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 구현
def bfs(x,y):
    # 1) queue, discovered 필요 자료형 생성
    queue = deque()
    discovered = [[0]*N for _ in range(N)]
    tlst = []

    # 2) queue에 초기데이터(들) 삽입, discovered 방문 표시
    queue.append((x,y))
    discovered[x][y] = 1
    dist = 0

    while queue:
        cx, cy = queue.popleft()
        # dist에 적힌 거리는 모두 큐에 넣었는지 확인(같은 거리 확인, 방문)
        if dist == discovered[cx][cy]:
            return tlst, dist-1


        # 4방향, 범위내, 미방문, 조건(나보다 같거나 작은 물고기)
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<=nx<N and 0<=ny<N and not discovered[nx][ny] and sea[nx][ny] <= size:
                # 전형적인 경우
                queue.append((nx, ny))
                discovered[nx][ny] = discovered[cx][cy] + 1

                # 문제 조건 : 나보다 작은 경우만 tlst 추가
                if size > sea[nx][ny] > 0:
                    tlst.append((nx, ny))
                    dist = discovered[nx][ny]

    # 방문을 모두 끝낸 경우(먹을 물고기 못찾음 : tlst 비어있음)
    return tlst, dist-1

# 잡아먹으러 다니는 시뮬레이션
queue = deque([x,y])            # 상어의 초기 위치
size = 2                        # 상어의 초기 크기
cnt = answer = 0                # 먹은 물고기 수, 정답
while True:
    tlst, dist = bfs(x,y)
    if not tlst:
        break
    tlst.sort(key = lambda x:(x[0], x[1]))
    x, y = tlst[0]
    sea[x][y] = 0               # 물고기 먹기
    cnt += 1
    answer += dist
    if size == cnt:             # 크기만큼 물고기 먹은 경우
        size += 1
        cnt = 0

print(answer)