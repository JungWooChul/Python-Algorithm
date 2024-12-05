def solution(n, times):
    answer = 0
    start = min(times)
    end = max(times)*n
    while start <= end:
        mid = (start+ end) // 2
        people = 0
        for t in times:
            people += mid // t
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            end = mid - 1
        elif people < n:
            start = mid + 1
            
    return answer
