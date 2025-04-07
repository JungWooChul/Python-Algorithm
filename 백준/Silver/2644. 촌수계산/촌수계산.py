import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    a,b = map(int, input().strip().split())
    m = int(input())
    graph = defaultdict(list)
    for _ in range(m):
        v1, v2 = map(int, input().strip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    def family(a, cnt, discovered):
        discovered[a] = cnt
        for v in graph[a]:
            if v not in discovered.keys():
                discovered = family(v, cnt+1,discovered)

        return discovered

    fam = family(a,0,{})
    try:
        print(fam[b])
        return
    except:
        print(-1)
        return

main()