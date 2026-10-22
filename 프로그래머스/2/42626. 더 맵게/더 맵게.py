import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for scov in scoville:
        heapq.heappush(heap, scov)
        
    while len(heap) > 1 and heap[0] < K:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b*2)
        answer += 1
    
    if heapq.heappop(heap) < K:
        return -1
    return answer