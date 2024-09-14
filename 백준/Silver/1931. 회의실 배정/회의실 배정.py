import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

def meetingroom_assignment(N, meetings):
    # 회의 시간을 기준으로 회의 정렬
    meetings = sorted(meetings, key=lambda x:(x[1], x[0]))
    
    answer = 1
    check = meetings[0][1] # 가장 빨리 끝나는 회의의 끝나는 시간

    for i in range(1, N):
        if meetings[i][0] >= check:
            answer += 1
            check = meetings[i][1]
    
    print(answer)
    return
    
meetingroom_assignment(N, meetings)