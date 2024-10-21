import sys
input = sys.stdin.readline

def main():
    a,b = map(int, input().split())
    
    answer = 0
    while a < b:
        if b%2 == 0:
            b = b//2
        elif b%10 == 1:
            b = b//10
        else:
            return -1
        
        answer += 1
        
    return answer + 1 if a==b else -1

if __name__ == '__main__':
    print(main())        