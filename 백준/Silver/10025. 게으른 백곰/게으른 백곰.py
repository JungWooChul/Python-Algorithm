import sys
input = sys.stdin.readline

def lazy_bear(queue, max_x, k):
    ice = [0]*(max_x+1)
    for x,g in queue:
        ice[x] = g
    
    window_sum = 0
    window_size = 2*k+1
    
    # 초기 윈도우 계산
    for i in range(min(window_size, len(ice))):
        window_sum += ice[i]

    answer = window_sum

    # 슬라이딩 윈도우 이동
    for i in range(window_size, len(ice)):
        window_sum += ice[i]  # 새로운 위치 추가
        window_sum -= ice[i - window_size]  # 이전 위치 제거
        answer = max(answer, window_sum)
    
    print(answer)
    return

def main():
    n,k = map(int, input().split())
    queue = []
    max_x = 0
    for _ in range(n):
        g,x = map(int, input().split())
        queue.append((x,g))
        max_x = max(max_x,x)
    
    queue.sort()
    lazy_bear(queue, max_x, k)

if __name__ == '__main__':
    main()