import sys
from collections import deque
input = sys.stdin.readline

def main():
    F, S, G, U, D = map(int, input().strip().split()) # 총 층수, 현재, 도착, up, down

    discovered = [0]*(F+1)
    queue = deque([S])
    discovered[S] = 1

    answer = 0
    while queue:
        x = queue.popleft()
        if x == G:
            print(discovered[x]-1)
            return
        for dx in [U, -D]:
            nx = x+dx
            if 0<nx<=F and not discovered[nx]:
                discovered[nx] = discovered[x]+1
                queue.append(nx)

    
    print("use the stairs")
    return
    
main()