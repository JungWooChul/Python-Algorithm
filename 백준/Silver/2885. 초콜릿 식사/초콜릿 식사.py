import sys
input = sys.stdin.readline

def chocolate_eat(N):
    stack = []
    check = 0
    while N > 1:
        for i in range(N):
            if N < 2**i:
                N -= 2**(i-1)
                check += 1
                stack.append(i-1)
                break
            elif N == 2**i:
                if check == 0:
                    print(N, 0)
                    return
                N -= 2**i
                check += 1
                stack.append(i)
                break
    
    if N == 1:
        if check == 0:
            print(2,1)
            return
        stack.append(0)

    # print(stack)
    chocolate = 2**stack[0] * 2
    div = stack[0] - stack[-1] + 1

    print(chocolate, div)
    return 

N = int(input())
chocolate_eat(N)