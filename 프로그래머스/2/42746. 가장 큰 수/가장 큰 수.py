def solution(numbers):
    numbers = sorted([str(number) for number in numbers], reverse=True)
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(numbers)
    return  answer if answer[0] !='0' else '0'