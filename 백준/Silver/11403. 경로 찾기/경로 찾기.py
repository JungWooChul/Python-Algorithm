import sys
input = sys.stdin.readline

N = int(input())
distances = [list(map(int, input().split())) for i in range(N)]

# 자기 자신을 제외하고 0인 값 무한으로 초기화
for i in range(len(distances)):
    for j in range(len(distances[0])):
        if distances[i][j] == 0 and i != j:
            distances[i][j] = float('inf')

# 최단거리 갱신
for k in range(N):
    for i in range(len(distances)):
        for j in range(len(distances[0])):
            # 자기자신에서 출발해서 자기자신으로 돌아오는 경우
            if i==j:
                if distances[i][k] + distances[k][j] != float('inf'):
                    distances[i][j] = distances[i][k] + distances[k][j]
            # 한 정점을 거쳐서 가는 경우
            else:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

for i in range(len(distances)):
    for j in range(len(distances[0])):
        if distances[i][j]:
            if distances[i][j] == float('inf'):
                print(0, end=" ")
            else:
                print(1, end=" ")
        else:
            print(distances[i][j], end=" ")
    print()