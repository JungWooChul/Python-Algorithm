import sys
input = sys.stdin.readline

n = int(input())
strides = list(map(int, input().split()))
start = int(input())

def jumpx2(n, strides, start):
    visited = [0]*n

    def dfs(idx):
        if (idx<0 
            or idx>=n
            or visited[idx]==1):
            return

        visited[idx]=1

        dfs(idx-strides[idx])
        dfs(idx+strides[idx])

    dfs(start-1)
    return visited.count(1)

print(jumpx2(n, strides, start))