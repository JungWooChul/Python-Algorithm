import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

distances = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            distances[i][j] = 0

for _ in range(M):
    a, b, cost = map(int, input().split())
    if distances[a-1][b-1] > cost:
        distances[a-1][b-1] = cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

for distance in distances:
    for dist in distance:
        if dist == float('inf'):
            print(0, end = " ")
        else:
            print(dist, end = " ")
    print()