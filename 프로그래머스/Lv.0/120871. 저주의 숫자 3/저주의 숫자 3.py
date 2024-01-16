def solution(n):
    answer = 0
    for num in range(1,n+1):
        # 바꾼 숫자가 3x마을에서 쓰는 숫자에 만족하지 않을 경우
        while(1):
            # 숫자에 3이 들어있거나 3의 배수인 수의 개수 확인
            if '3' in str(num+answer) or (num+answer)%3 == 0:
                answer += 1
            else:
                break
    return answer + n
