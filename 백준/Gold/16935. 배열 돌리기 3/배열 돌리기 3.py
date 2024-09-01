import sys, copy
input = sys.stdin.readline

# 상하반전 연산
def cal1(arr):
    return [arr[i][:] for i in range(len(arr)-1, -1, -1)]

# 좌우반전 연산
def cal2(arr):
    return [arr[i][::-1] for i in range(len(arr))] # 각 행 역순정렬하여 반환

def cal3(arr):
    arr_tmp = []
    for j in range(len(arr[0])): # 열 순회
        arr_tmp.append([arr[i][j] for i in range(len(arr)-1, -1, -1)]) # 행 역순 순회
    return arr_tmp

def cal4(arr):
    arr_tmp = []
    for j in range(len(arr[0])-1, -1, -1): # 열 역순 순회
        arr_tmp.append([arr[i][j] for i in range(len(arr))]) # 행 순회
    return arr_tmp

# 4등분 후 시계방향 회전 연산
def cal5(arr):
    arr_tmp = []
    n, m = len(arr), len(arr[0])

    # 최종 결과값의 4열까지의 원소들 먼저 추가
    for i in range(n//2,n):
        arr_tmp.append(arr[i][:m//2])
    for i in range(n//2,n):
        arr_tmp.append(arr[i][m//2:])
    
    # 나머지 원소들 추가
    for i in range(len(arr_tmp)):
        if i<n//2:
            arr_tmp[i].extend(arr[i%(n//2)][:m//2])
        else:
            arr_tmp[i].extend(arr[i%(n//2)][m//2:])
    
    return arr_tmp

# 4등분 후 반시계방향 회전 연산
def cal6(arr):
    arr_tmp = []
    n, m = len(arr), len(arr[0])

    # 최종 결과값의 4열까지의 원소들 먼저 추가
    for i in range(n//2):
        arr_tmp.append(arr[i][m//2:])
    for i in range(n//2):
        arr_tmp.append(arr[i][:m//2])
    
    # 나머지 원소들 추가
    for i in range(len(arr_tmp)):
        if i<n//2:
            arr_tmp[i].extend(arr[i%(n//2) + n//2][m//2:])
        else:
            arr_tmp[i].extend(arr[i%(n//2) + n//2][:m//2])
    
    return arr_tmp

def array_rotation3():
    n,m,r = map(int, input().strip().split(' '))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split(' '))))
    
    cals = list(map(int, input().strip().split(' ')))
    for cal in cals:
        if cal == 1:
            arr = cal1(arr)
        elif cal == 2:
            arr = cal2(arr)
        elif cal == 3:
            arr = cal3(arr)
        elif cal == 4:
            arr = cal4(arr)
        elif cal == 5:
            arr = cal5(arr)
        elif cal == 6:
            arr = cal6(arr)
    
    for ar in arr:
        for a in ar:
            print(a, end = ' ')
        print()

array_rotation3()