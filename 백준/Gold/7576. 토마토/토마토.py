import sys
from collections import deque
input = sys.stdin.readline

def main():
    m,n = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()

    # 익은 토마토 위치를 큐에 넣기
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                queue.append((i, j))

    def bfs():
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1  # 날짜를 증가시켜 저장
                    queue.append((nx, ny))
    
    bfs()
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1  # 익지 않은 토마토가 남아있는 경우
            answer = max(answer, arr[i][j])

    return answer - 1

if __name__ == "__main__":
    print(main())