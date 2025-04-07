import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    N = int(input())
    edge = int(input())
    graph = defaultdict(list)

    for _ in range(edge):
        v1, v2 = map(int, input().strip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(v, discovered):
        discovered.append(v)
        for v2 in graph[v]:
            if v2 not in discovered:
                discovered = dfs(v2, discovered)

        return discovered
    print(len(dfs(1, [])) - 1) # 1번 컴퓨터 제외

main()