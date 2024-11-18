def solution(m, n, puddles):
    roots = [[0]*m for _ in range(n)]
    
    for x,y in puddles:
        roots[y-1][x-1] = -1 # 집의 위치가 (m,n)이므로 웅덩이의 위치도 (y,x)
    
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    dx = [0, 1]
    dy = [1, 0]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 물에 잠긴 지역 처리, 시작점 건너뛰기
            if roots[i-1][j-1] == -1 or (i==1 and j==1):
                continue
            
            for idx in range(2):
                dp[i][j] = (dp[i][j] + dp[i-dx[idx]][j-dy[idx]])%1000000007 
    
    return dp[n][m]