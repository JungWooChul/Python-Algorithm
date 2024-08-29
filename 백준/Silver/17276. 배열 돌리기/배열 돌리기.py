import sys, copy
input = sys.stdin.readline

def clockwise(arr):
    # slicing을 통한 깊은 복사
    clockwise_arr = [a[:] for a in arr]
    
    for i in range(len(arr)):
        # 주 대각선을 가운데 열로 옮기기
        clockwise_arr[i][len(arr)//2] = arr[i][i]

        # 가운데 열을 부 대각선으로 옮기기
        clockwise_arr[i][len(arr)-i-1] = arr[i][len(arr)//2]

        # 부 대각선을 가운데 행으로 옮기기
        clockwise_arr[len(arr)//2][len(arr)-i-1] = arr[i][len(arr)-i-1]

        # 가운데 행을 주 대각선으로 옮기기
        clockwise_arr[i][i] = arr[len(arr)//2][i]
    
    return clockwise_arr

def counter_clockwise(arr):
    # slicing을 통한 깊은 복사
    counter_clockwise_arr = [a[:] for a in arr]
    
    for i in range(len(arr)):
        # 부 대각선을 가운데 열로 옮기기
        counter_clockwise_arr[i][len(arr)//2] = arr[i][len(arr)-i-1]

        # 가운데 열을 주 대각선으로 옮기기
        counter_clockwise_arr[i][i] = arr[i][len(arr)//2]

        # 주 대각선을 가운데 행으로 옮기기
        counter_clockwise_arr[len(arr)//2][i] = arr[i][i]

        # 가운데 행을 부 대각선으로 옮기기
        counter_clockwise_arr[len(arr)-i-1][i] = arr[len(arr)//2][i]
    return counter_clockwise_arr

def array_rotation():
    T = int(input())
    answer = []
    for _ in range(T):
        minus = False
        N, degree = input().strip().split()

        if degree[0] == '-':
            minus = True
            degree = int(degree[1:])
        else:
            degree = int(degree)

        arr = []
        for _ in range(int(N)):
            arr.append(list(map(int, input().strip().split())))
        
        if minus:
            for _ in range(degree//45):
                arr = counter_clockwise(arr)
        else:
            for _ in range(degree//45):
                arr = copy.deepcopy(clockwise(arr))

        answer.append(arr)
    
    for ans in answer:
        for a in ans:
            for b in a:
                print(b, end = ' ')
            print()
    return

array_rotation()