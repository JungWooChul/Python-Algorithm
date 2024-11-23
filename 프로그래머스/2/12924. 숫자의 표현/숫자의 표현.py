def solution(n):
    answer = 0
    for i in range(1,n+1):
        tmp, idx= i, i+1
        while tmp < n:
            tmp += idx
            idx += 1
        if tmp == n:
            answer += 1
    return answer