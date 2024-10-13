import sys
input = sys.stdin.readline

def friend(arr, N):
    answer = [0]*N
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            else:
                if arr[i][j] == 'N':
                    for k in range(N):
                        if arr[i][k]=='Y' and arr[j][k]=='Y':
                            answer[i] += 1
                            break
                else:
                    arr[j][i] = 'Y'
                    answer[i] += 1

    return max(answer)



def main():
    N = int(input())
    
    arr = []
    for _ in range(N):
        arr.append(list(input().strip()))
    
    print(friend(arr, N))

if __name__ == '__main__':
    main()