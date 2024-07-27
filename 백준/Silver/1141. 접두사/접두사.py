import sys
input = sys.stdin.readline

def prefix(N, arr):
    arr = sorted(arr, key=lambda x:len(x))
    out = []

    for i in range(N-1):
        temp = arr[i]
        for j in range(i+1, N):
            if temp == arr[j][:len(temp)]:
                out.append(temp)
                break
    return N - len(out)

N = int(input())
arr = [input().strip() for _ in range(N)]
print(prefix(N,arr))