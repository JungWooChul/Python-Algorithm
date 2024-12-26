import sys
input = sys.stdin.readline

def eight(L, R):
    answer = 0
    # 자릿수가 다른 경우 : L = 8, R = 80 -> 8이 들어가지 않는 숫자 무조건 존재
    if len(L) != len(R):
        return answer

    for l,r in zip(L,R):
        if l == r:
            if l == '8':
                answer += 1
        else:
            break
    
    return answer

def main():
    L, R = map(str, input().split())
    print(eight(L,R))

if __name__ == "__main__":
    main()