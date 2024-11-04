import sys
input  = sys.stdin.readline

def common_bag(N, K, arr):
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1,K+1):
            if arr[i-1][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1][0]] + arr[i-1][1])

    return dp[N][K]

def main():
    N, K = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[0])
    
    print(common_bag(N, K, arr))

if __name__ == '__main__':
    main()