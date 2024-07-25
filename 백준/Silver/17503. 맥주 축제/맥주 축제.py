import sys, heapq
input = sys.stdin.readline

def beer_festival(N, M, beers):
    pick, manjok_sum = [], 0
    heapq.heapify(pick)
    
    for beer in beers:
        if len(pick) < N:
            heapq.heappush(pick, beer)
            manjok_sum += beer[0]
        else:
            tmp = heapq.heappop(pick)
            heapq.heappush(pick, beer)
            
            manjok_sum = manjok_sum - tmp[0] + beer[0]

        if manjok_sum >= M and len(pick) == N:
            answer = heapq.heappop(pick)[1]
            while pick:
                answer = max(answer, heapq.heappop(pick)[1])
            return answer
        
    return -1


N, M, K = map(int, input().split()) # N:축제기간, M:선호도의 합, K:맥주 종류 수

beers = [tuple(map(int, input().split())) for _ in range(K)] # 각 맥주의 선호도, 도수 레벨
beers.sort(key=lambda x:x[1]) # 맥주 도수를 기준으로 오름차순 정렬

print(beer_festival(N, M, beers))