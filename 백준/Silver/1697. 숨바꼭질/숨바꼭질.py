import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    n, k = map(int, input().strip().split())
    max_num = 100000
    discovered = [0]*(max_num+1)

    def bfs(n,k):
        queue = deque()
        queue.append(n)

        while queue:
            x = queue.popleft()
            if x == k:
                print(discovered[x])
                return
            for nx in [x-1, x+1, 2*x]:
                if 0<=nx<=max_num and not discovered[nx]:
                    discovered[nx] = discovered[x]+1
                    queue.append(nx)
    bfs(n,k)
main()