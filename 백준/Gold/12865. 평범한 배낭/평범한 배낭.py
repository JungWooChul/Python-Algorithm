import sys
input  = sys.stdin.readline

def common_bag(N, K, arr):
    dp = [0] * (K + 1)
    for weight, value in arr:
        for j in range(K, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[K]

def main():
    N, K = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    
    print(common_bag(N, K, arr))

if __name__ == '__main__':
    main()