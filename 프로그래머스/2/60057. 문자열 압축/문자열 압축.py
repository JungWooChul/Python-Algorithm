def solution(s):
    answer = len(s)
    # 문자 압축 단위 설정
    for sep in range(1, len(s)//2+1):
        check = 0
        sep_tmp, tmp = '', ''
        for alp in [s[idx:idx+sep] for idx in range(0, len(s), sep)]:
            if tmp == '':
                tmp = alp
            else:
                if tmp == alp:
                    check += 1
                else:
                    if check == 0:
                        sep_tmp += tmp
                    else:
                        sep_tmp += str(check+1)+tmp
                    check = 0
                    tmp = alp
        if check == 0:
            sep_tmp += tmp
        else:
            sep_tmp += str(check+1)+tmp
            
        if len(sep_tmp) < answer:
            answer = len(sep_tmp)
    return answer