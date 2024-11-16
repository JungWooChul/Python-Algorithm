def solution(operations):
    answer = []
    for operation in operations:
        pram, number = operation.split()
        if pram == 'I':
            answer.append(int(number))
            answer.sort()
        elif pram == 'D':
            if not answer:
                continue
                
            if number == '1':
                answer.pop(-1)
            elif number == '-1':
                answer.pop(0)
                
    return [answer[-1], answer[0]] if answer else [0,0]