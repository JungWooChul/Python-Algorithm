import sys
input = sys.stdin.readline

def library(n,m,books):
    minus, plus = [], []
    for book in books:
        if book < 0:
            minus.append(abs(book))
        else:
            plus.append(book)
    # 거리 내림차순 정렬(음수는 절댓값을 취해서 이미 완료)
    plus.sort(reverse=True)

    answer = 0
    max_dist = 0
    # 음수 그룹 처리
    for i in range(0, len(minus), m):
        answer += 2 * minus[i]
        max_dist = max(max_dist, minus[i])
    
    # 양수 그룹 처리
    for i in range(0, len(plus), m):
        answer += 2 * plus[i]
        max_dist = max(max_dist, plus[i])
    
    # 가장 먼 거리는 마지막에 놔두고 돌아오지 않아도 됨
    answer -= max_dist

    print(answer)
    return

def main():
    n,m = map(int, input().split())
    books = list(map(int, input().split()))
    books.sort()
    
    library(n,m,books)
    return

if __name__ == "__main__":
    main()