def solution(triangle):
    dp = []
    answer = 0
    
    for i in range(len(triangle)):
        dp.append([0 for j in range(len(triangle[i]))])
    
    dp[0][0] = triangle[0][0]
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j < i:
                tmp = triangle[i][j] + dp[i-1][j]
                dp[i][j] = max(dp[i][j],tmp)
            if j > 0:
                tmp = triangle[i][j] + dp[i-1][j-1]
                dp[i][j] = max(dp[i][j],tmp)
    return max(dp[-1])
                
                
                
        