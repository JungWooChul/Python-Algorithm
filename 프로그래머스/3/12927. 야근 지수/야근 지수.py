import heapq
def solution(n, works):
    works = [-1*work for work in works]
    heapq.heapify(works)
    
    while n:
        work = heapq.heappop(works)
        if work == 0:
            return 0
        
        heapq.heappush(works, work+1) # 최대힙이기 때문에 -1이 아닌 +1
        n -= 1
    
    answer = 0
    for work in works:
        answer += work**2
    
    return answer