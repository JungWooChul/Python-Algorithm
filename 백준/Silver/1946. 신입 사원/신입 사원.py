import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수
arr = [] # 테스트 케이스별 지원자 점수
for _ in range(T):
    N = int(input()) # 지원자 수
    arr.append([list(map(int, input().split())) for _ in range(N)])

def new_employee(arr):
    answer = 1
    arr = sorted(arr, key=lambda x:x[0]) # 1차 점수를 기준으로 정렬(2차 점수만 비교)

    min2 = arr[0][1] # 1차 1등의 2차 점수
    for i in range(1, len(arr)):
        if min2 >= arr[i][1]:
            min2 = arr[i][1]
            answer += 1
        
    return answer

for a in arr:
    print(new_employee(a))