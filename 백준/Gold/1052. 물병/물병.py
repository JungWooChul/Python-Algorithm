import sys
input = sys.stdin.readline

def bottle(N, K):
    if K >= N:
            return 0

    bottles = N
    answer = 0

    while bin(bottles).count('1') > K:
        answer += 1
        bottles += 1

    return answer

N, K = map(int, input().split())
print(bottle(N,K))