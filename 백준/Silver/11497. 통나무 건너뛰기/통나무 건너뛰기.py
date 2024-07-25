import sys
from collections import deque
input = sys.stdin.readline

def jump_log(N, length):
    optimal = deque([])
    check,answer = 0, 0
    for l in length:
        if check%2 == 0:
            optimal.append(l)
            try:
                answer = max(answer, abs(optimal[-1] - optimal[-2]))
            except:
                pass
        else:
            optimal.appendleft(l)
            try:
                answer = max(answer, abs(optimal[0] - optimal[1]))
            except:
                pass
        check += 1
    
    try:
        answer = max(answer, abs(optimal[-1] - optimal[0]))
    except:
        pass

    return answer

def main():
    T = int(input())
    answer = []
    for _ in range(T):
        N = int(input())
        length = list(map(int, input().split()))
        length.sort(reverse=True)

        answer.append(jump_log(N, length))
    
    for i in answer:
        print(i)

main()
