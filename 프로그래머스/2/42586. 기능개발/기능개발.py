from collections import deque
def solution(progresses, speeds):
    answer, tmp = [], []
    for prog, speed in zip(progresses, speeds):
        tmp.append((100-prog+speed-1)//speed)
    
    queue = deque(tmp)
    cnt = 0
    while queue:
        check = queue.popleft()
        cnt += 1
        while queue:
            if check >= queue[0]:
                queue.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
        cnt = 0
            
    return answer