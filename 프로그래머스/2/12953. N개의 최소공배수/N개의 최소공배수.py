def solution(arr):
    lcm = 1
    for a in arr:
        lcm *= a
    for i in range(max(arr), lcm+1):
        check = 1
        for a in arr:
            # 나누어 떨어지지 않는 원소가 있는지 확인
            if i%a != 0:
                check = 0
                break
                
        if check:
            return i
