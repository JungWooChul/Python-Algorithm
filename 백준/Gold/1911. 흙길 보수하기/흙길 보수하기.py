import sys
input = sys.stdin.readline

def main():
    N, L = map(int, input().split())
    puddles = [list(map(int, input().split())) for _ in range(N)]
    puddles.sort()

    answer = 0
    cover_end = 0

    for start, end in puddles:
        if cover_end < start:
            cover_end = start
        
        div = (end-cover_end)//L
        if (end-cover_end)%L == 0:
            cover_end += (div*L)
            answer += div
        else:
            cover_end += ((div+1)*L)
            answer += (div+1)    
    
    return answer

if __name__ == '__main__':
    print(main())