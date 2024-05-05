import sys
input = sys.stdin.readline

def inf_assignment(N):
    score = 0
    assignment = []
    for _ in range(N):
        tmp = input().rstrip().split(' ')
        
        # 과제 유무 여부 확인
        if tmp[0] == '0':
            if assignment:
                assignment[-1][1] -= 1
        elif tmp[0] == '1':
            assignment.append([int(tmp[1]), int(tmp[2])])
            assignment[-1][1] -= 1
        
        # 완료한 과제가 있는지 확인
        if assignment and assignment[-1][1] == 0:
            score += assignment.pop()[0]
            
    return score


N = int(input())
print(inf_assignment(N))