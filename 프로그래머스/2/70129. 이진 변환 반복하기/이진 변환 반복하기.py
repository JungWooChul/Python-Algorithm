def solution(s):
    cnt, del_zero = 0,0
    while s != '1':
        del_zero += (len(s) - s.count('1'))
        s = bin(s.count('1'))[2:]
        cnt += 1
    return [cnt, del_zero]