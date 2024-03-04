import sys
input = sys.stdin.readline
        
stack = list(input().strip())
tmp_stack = list()

num = int(input())

for i in range(num):
    command = input().strip().split()
    if command[0] == 'L':
        try:
            tmp_stack.append(stack.pop())
        except:
            pass
    elif command[0] == 'D':
        try:
            stack.append(tmp_stack.pop())
        except:
            pass
    elif command[0] == 'B':
        try:
            stack.pop()
        except:
            pass        
    elif command[0] == 'P':
        stack.append(command[1])
        

print(''.join(stack) + ''.join(tmp_stack[::-1]))