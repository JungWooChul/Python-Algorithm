def solution(s):
    if s[0] == '-':
        return -1*int(s[1:])
    else:
        return int(s)