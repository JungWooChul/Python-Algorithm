def solution(n, s):
    if s < n:
        return [-1]
    
    answer = [s//n]*n
    remainder = s%n
    check = len(answer) - 1
    while remainder:
        answer[check] += 1
        check -= 1
        remainder -= 1
    return answer