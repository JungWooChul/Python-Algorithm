def solution(s):
    answer = ''
    
    # 입력 문자열 전체를 소문자로 변환
    s = s.lower()
    
    # 공백 확인
    check = 1
    
    # 전체 탐색
    for alp in s:
        # 공백인 경우는 문자열에 그대로 포함시키고, check
        if alp == ' ':
            answer += alp
            check = 1
        # check가 1인 경우(공백 다음 오는 단어)에는 문자를 대문자로 변경하여 포함
        else:
            if check == 1:
                answer += alp.upper()
                check = 0
            else:
                answer += alp
    return answer