import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def represent_dp(arr):
    dp = [1]*len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(represent_dp(arr))