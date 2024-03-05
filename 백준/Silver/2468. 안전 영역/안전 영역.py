import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for i in range(N)]


def numSection(arr):
    def dfs(i, j):
        if (i<0 or i>=len(arr) 
            or j<0 or j>=len(arr[0]) 
            or arr[i][j]==0):
            return

        arr[i][j] = 0

        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i-1, j)

    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt += 1
    return cnt

answer = 1
maxHeight = max(map(max, matrix))
minHeight = min(map(min, matrix))

for height in range(minHeight, maxHeight):
    safe = [[(1 if matrix[i][j]>height else 0) 
            for j in range(len(matrix[0]))] 
            for i in range(N)]
    tmp = numSection(safe)
    answer = max(answer,tmp)
print(answer)

