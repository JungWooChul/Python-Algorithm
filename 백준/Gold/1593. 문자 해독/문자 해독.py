import sys
from collections import Counter
input = sys.stdin.readline

def decoding(g, len_s, w,s):
    answer = 0
    countW = Counter(w)
    countWindow = Counter(s[:g])  # 초기 윈도우의 문자 빈도 계산
    
    answer = 0

    for i in range(len_s - g + 1):
        # 현재 윈도우와 W의 빈도 비교
        if countW == countWindow:
            answer += 1
        
        if i + g < len_s:
            countWindow[s[i]] -= 1  # 윈도우의 첫 문자 제거
            if countWindow[s[i]] == 0:
                countWindow.pop(s[i], None)  # 빈도 0인 문자는 제거
            
            countWindow[s[i + g]] += 1  # 윈도우의 새로운 문자 추가

    print(answer)
    return

def main():
    g, len_s = map(int, input().split())
    w = input().strip()
    s = input().strip()
    decoding(g, len_s, w,s)

if __name__ == '__main__':
    main()