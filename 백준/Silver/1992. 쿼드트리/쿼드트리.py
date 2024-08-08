import sys
input = sys.stdin.readline

def quad_tree(n, arr):
    if n ==1:
        return arr[0][0]

    # new_arr = [[0]*(n//2)]*(n//2) -> 각 행이 동일한 리스트 객체를 참조하게 되어 한 행의 값을 바꾸면 모든 행의 값이 같이 바뀌는 현상 발생
    new_arr = [[0 for _ in range(n//2)] for _ in range(n//2)]
    for i in range(n//2):
        for j in range(n//2):
            temp = [arr[2*i][2*j], arr[2*i][2*j+1], arr[2*i+1][2*j], arr[2*i+1][2*j+1]]
            try:
                mat_sum = sum(temp)
                if mat_sum == 4:
                    new_arr[i][j] = 1
                elif mat_sum == 0:
                    new_arr[i][j] = 0
                else:
                    new_arr[i][j] = '('+''.join(list(map(str, temp)))+')'
            except:
                new_arr[i][j] = '('+''.join(list(map(str, temp)))+')'
    return quad_tree(n//2, new_arr)

N = int(input())
matrix = [list(map(int,list(input().strip()))) for _ in range(N)]

print(quad_tree(N, matrix))