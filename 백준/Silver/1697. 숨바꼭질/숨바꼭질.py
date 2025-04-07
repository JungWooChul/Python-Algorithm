import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    n,k = map(int, input().strip().split())

    if n < k:
        graph = [float('inf')] * (2*k+1)
        discovered = [0]*(2*k+1)
        queue = deque()

        if n == 0:
            graph[n] = 0
            discovered[n] = 1
            queue.append(n)
        else:
            mul, cnt = n, 0
            while mul < k:
                graph[mul] = cnt
                discovered[mul] = 1
                queue.append(mul)
                mul *= 2
                cnt += 1

        while queue:
            x = queue.popleft()
            for nx in [x-1, x+1, 2*x]:
                if 0 <= nx <= 2*k and not discovered[nx]:
                    queue.append(nx)
                    discovered[nx] = 1

                    graph[nx] = graph[x]+1
    elif n > k:
        graph = [float('inf')] * (2*n + 1)
        discovered = [0] * (2*n + 1)

        queue = deque([n])
        discovered[n] = 1
        graph[n] = 0

        while queue:
            x = queue.popleft()
            for nx in [x - 1, x + 1, 2 * x]:
                if 0<= nx<=2*n:
                    if not discovered[nx]:
                        queue.append(nx)
                        discovered[nx] = 1

                        graph[nx] = graph[x] + 1

    else:
        print(0)
        return
    print(graph[k])

main()