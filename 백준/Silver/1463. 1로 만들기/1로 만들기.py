import sys
input = sys.stdin.readline

N = int(input())
dp = [0,0,1,1] # [인덱스 맞춤, N이 1일 때의 출력값, N이 2일 때의 출력값, N이 3일 때의 출력값]

for i in range(4,N+1):
    dp.append(dp[i-1]+1) # 조건 3 : 1을 뺀다
    if i%2 == 0:    
        dp[i] = min(dp[i//2]+1, dp[i]) # 조건 2 : 2로 나누어 떨어지면 2로 나눈다.
    if i%3 == 0:    
        dp[i] = min(dp[i//3]+1, dp[i]) # 조건 1 : 3으로 나누어 떨어지면 3으로 나눈다.

print(dp[N])