import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # 반복문에서 pop을 두 번 해야함
    while len(scoville)>1:
        k1 = heapq.heappop(scoville)
        # 우선순위큐이므로 스코빌 지수가 가장 낮은 것만 확인
        if k1 >= K:
            break
        else:
            k2 = heapq.heappop(scoville)
            heapq.heappush(scoville, k1 + (k2*2))
            answer += 1

    return answer if scoville[0]>=K else -1