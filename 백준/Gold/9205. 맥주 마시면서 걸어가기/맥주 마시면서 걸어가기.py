import sys
from collections import deque

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        locations = [tuple(map(int, input().split())) for _ in range(n + 2)]  # 집 + 편의점들 + 페스티벌
        visited = [False] * (n + 2)

        queue = deque()
        queue.append(0)  # 집 인덱스
        visited[0] = True

        while queue:
            current = queue.popleft()
            cx, cy = locations[current]

            for i in range(1, n + 2):  # 나 자신 제외하고
                if not visited[i]:
                    nx, ny = locations[i]
                    distance = abs(cx - nx) + abs(cy - ny)
                    if distance <= 1000:
                        visited[i] = True
                        queue.append(i)

        print("happy" if visited[-1] else "sad")

main()