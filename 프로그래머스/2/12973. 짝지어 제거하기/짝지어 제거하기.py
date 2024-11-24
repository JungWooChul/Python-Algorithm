from collections import deque
def solution(s):
    alpha = deque(s)
    stack = []
    
    while alpha:
        alp = alpha.popleft()
        
        # 스택이 비어있는 경우
        if not stack:
            stack.append(alp)
        else:
            if stack[-1] == alp:
                stack.pop()
            else:
                stack.append(alp)
    
    return 0 if stack else 1
            