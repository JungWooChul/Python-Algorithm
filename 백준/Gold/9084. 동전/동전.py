import sys
input  = sys.stdin.readline

def coin(N, coins, money):
    coins = [i for i in coins if i<money+1]
    dp = [0]*(money+1)
    dp[0] = 1
    
    
    for i in coins:
        for j in range(money+1):
            if j >= i:
                dp[j] += dp[j-i]
    
    return dp[money]

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        coins = list(map(int, input().split()))
        money = int(input())
        
        print(coin(N, coins, money))

if __name__ == '__main__':
    main()