from collections import deque
def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    idx, answer = 0, 0
    for a in A:
        if a < B[idx]:
            answer += 1
            idx += 1
    return answer