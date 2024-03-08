import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]

def tetromino(n,m,matrix):
    # 최댓값 따라서 그대로 탐색
    def dfs(i,j,sum,depth):
        if (depth >= 5
            or i<0 or i>=n 
            or j<0 or j>=m
            or matrix[i][j]==0):
            return 0
        
        # 중복 탐색 방지를 위한 초기화
        val = matrix[i][j]
        matrix[i][j] = 0

        # 동서남북 네 방향 탐색
        max_dfs = max(dfs(i,j+1,sum,depth+1), dfs(i,j-1,sum,depth+1), dfs(i+1,j,sum,depth+1), dfs(i-1,j,sum,depth+1))

        # ㅓ,ㅏ,ㅗ,ㅜ 와 같은 특수한 블록 탐색
        max_special = 0
        if depth == 2:
            arr = [dfs(i,j+1,sum,depth+2), dfs(i,j-1,sum,depth+2), dfs(i+1,j,sum,depth+2), dfs(i-1,j,sum,depth+2)]
            arr.sort()

            max_special = arr[-1] + arr[-2]

        matrix[i][j] = val
        return val + max(max_dfs, max_special)
    
    # 행렬 순회
    maxTet = 0
    for i in range(n):
        for j in range(m):
            maxTet = max(maxTet, dfs(i,j,0,1))
    return maxTet

print(tetromino(n,m,matrix))