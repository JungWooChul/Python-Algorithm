import sys, copy
input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().strip().split()))

def balloon_bomb(N, balloons):
    answer = []
    index = 0
    indexes = [i+1 for i in range(N)] # 풍선의 자리
    while len(indexes) > 1:
        answer.append(indexes.pop(index))
        move = balloons.pop(index)  # 해당 풍선 값을 가져온 후 제거
        
        # 풍선을 pop한 후 리스트의 크기가 줄어들었으므로 이동할 인덱스를 계산
        if move > 0:  # 오른쪽으로 이동할 경우
            index = (index + (move - 1)) % len(indexes)
        else:  # 왼쪽으로 이동할 경우
            index = (index + move) % len(indexes)

    answer.append(indexes[0])  # 마지막 남은 풍선
    print(' '.join(map(str, answer)))
balloon_bomb(N,balloons)