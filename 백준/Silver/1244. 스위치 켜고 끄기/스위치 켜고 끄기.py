import sys, copy
input = sys.stdin.readline

def male(arr, num):
    for i in range(len(arr)//num):
        arr[num*(i+1) - 1] = (arr[num*(i+1) - 1] + 1)%2
    return arr

def female(arr, num):
    num -= 1
    left, right = num - 1, num + 1
    arr[num] = (arr[num]+1)%2
    while left >= 0 and right < len(arr):
        if arr[left] == arr[right]:
            arr[left], arr[right] = (arr[left]+1)%2, (arr[right]+1)%2
            left -= 1
            right += 1
        else:
            break
    return arr

def switch_on_off():
    n = int(input())
    arr = list(map(int, input().strip().split()))

    student_num = int(input())
    for _ in range(student_num):
        s, num = map(int, input().strip().split())
        if s == 1:
            arr = male(arr, num)
        else:
            arr = female(arr, num)
    
    if len(arr) <= 20:
        print(*arr)
    else:
        for i in range((len(arr)//20)+1):
            print(*arr[i*20:(i+1)*20])

switch_on_off()