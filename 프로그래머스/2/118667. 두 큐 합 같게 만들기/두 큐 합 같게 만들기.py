from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    limit = len(queue1) + len(queue2)
    
    while(2*limit+1 > answer):
        if q1_sum < q2_sum:
            tmp = queue2.popleft()
            queue1.append(tmp)
            q1_sum, q2_sum = q1_sum + tmp, q2_sum - tmp
            answer += 1
        elif q1_sum > q2_sum:
            tmp = queue1.popleft()
            queue2.append(tmp)
            q1_sum, q2_sum = q1_sum - tmp, q2_sum + tmp
            answer += 1
        else:
            return answer
    return -1
    